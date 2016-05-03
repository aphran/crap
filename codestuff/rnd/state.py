#!/usr/bin/env python

class NDFA:
    """Non-Deterministic Finite Automaton"""

    def __init__(self, Q, name):
        """Init; F is implied as the set of states that are present but not conducive
        Z is guessed from Q, q0 is always None, d is implemented in self.populate"""
        self.Q = Q
        self.name = name
        self.done = False
        #q0
        self.s = set([])
        self.options = set([])
        self.transition()

    def calculate_options(self):
        options = set([])
        for s in self.s:
            options = options.union(set(self.flatten(self.Q[s])))
        self.options = options.difference(self.s)

    def run(self):
        while(not self.done):
            self.calculate_options()
            print "\n\n(i) '%s' is '%s'" % (self.name, ', '.join([s for s in self.s]))
            print "(i) Options are: '%s'" % ', '.join(self.options)
            next_states = raw_input("\n\n  (?) What is next for '%s'?: " % self.name)
            if next_states == "nothing":
                self.done = True
                print "\n\nSayonara.\n\n"
                break
            else:
                next_state_set = set([s.strip() for s in next_states.split(',')])
                self.transition(next_state_set)

    def transition(self, next_states=set([None])):
        new_states = set([])
        bad_states = set([])
        for next_state in next_states:
            if next_state in self.Q:
                if self.s:
                    for s in self.s:
                        if next_state in self.options:
                            new_states.add(next_state)
                        else:
                            bad_states.add(next_state)
                else:
                    self.s = set(self.Q[next_state])
            else:
                print "\n  (!) '%s' is unknown to '%s'\n" % (next_state, self.name)
        if new_states:
            self.s = new_states
        if bad_states:
            print "\n  (!) '%s' can't start '%s' now, though!\n" % (self.name, ', '.join(bad_states))

    def flatten(self, l): 
        """Magic: the flattening - needed for intake sublists"""
        import collections
        flattened = []
        if isinstance(l, collections.MutableSequence):
            for i in l:
                for fi in self.flatten(i):
                    flattened.append(fi)
        else:
            flattened.append(l)
        return flattened

# run for a sample creature, which is a disgusting formless mass of an organism
# capable of feeding through its skin by seeping in nutrients as well as using
# light as an energy intake through photosynthesis. The creature has a large,
# yappy compound eye, can sense magnetic fields and reproduces asexually, using
# electromagnetic interference as genetic entropy. Obviously the state dict is
# incomplete and unnecessarily repetitive. Nested lists should be fine.
name = "The Creature"
states = {
    None: ["idling", "yapping"],
    "idling": ["seeping", "photosinthesizing", "yapping", "attacking", "retreating"],
    "yapping": ["idling", ["seeping", "photosinthesizing"], "retreating"],
    "seeping": ["idling", "retreating", "photosinthesizing"],
    "attacking": ["idling", "retreating"],
    "photosinthesizing": ["seeping", "idling", "yapping"],
    "retreating": ["idling", "attacking"]
}
a = NDFA(states, name)
print "\nHi, please use infinitives as actions (you may suggest many by using commas)"
a.run()

