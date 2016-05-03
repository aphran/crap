#!/usr/bin/env python

class Node:
    """Inconspicuous Node"""
    def __init__(self, name):
        self.name = str(name) if name else ''
        self.nodes = []

    def append(self, node):
        self.nodes.append(node)

    def show(self, d=0):
        print self.string()

    def string(self, d=0):
        strret = d*'  ' + self.name
        for node in self.nodes:
            strret += '\n' + node.string(d + 1)
        return strret

class NDFA:
    """Non-Deterministic Finite Automaton"""

    def __init__(self, Q):
        """Init; F is implied as the set of states that are present but not conducive
        Z is guessed from Q, q0 is always None, d is implemented in self.populate"""
        self.Q = Q
        self.node = self.populate()

    def populate(self, start=None):
        """Generate all possible end states"""
        if start in self.Q.keys():
            node = Node(start)
            next_states = self.Q[start]
            if next_states:
                for next_state in self.flatten(next_states):
                    node.append(self.populate(next_state))
            return node

    def show(self):
        """Print self"""
        self.node.show()
        print ''

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

# fill up decision dict, None is always the initial state
#advs = ["medio", "bien", "lo contrario de"]
#weyes = ["Alfredo", "Lux", "Kike", "Piceno"]
#adjectives = ["macho", "compa", "jotito"]
#states = {
#  None: weyes,
#  "es:": advs
#}
#for adj in adjectives:
#  states[adj] = None
#for wey in weyes:
#  states[wey] = "es:"
#for adv in advs:
#  states[adv] = adjectives

# fill up decision dict, None is always the initial state
idle = "idle"
roam = "alerted roam"
survive = ["retreat", "fight"]
sustain = ["seep", "photosynthesize", "rest"]
reproduce = ["seduce", "mate"]
parent = ["watch", "abandon"]
dominate = ["spray", "mark"]
states = { 
      None: idle,
      idle: roam,
      roam: "abandon",
      "abandon": None #final state
}
#for act in survive:
#    states[act] = [reproduce, move, sustain, dominate]
#for act in reproduce:
#    states[act] = [survive, move, sustain, dominate]
#for act in survive:
#    states[act] = [reproduce, move, sustain, dominate]
#for act in sustain:
#    states[act] = [reproduce, survive, move, dominate]
        

# init and run our automaton
#from pprint import pprint
a = NDFA(states)
#pprint(a.node)
#pprint(a.node.nodes)
a.show()

