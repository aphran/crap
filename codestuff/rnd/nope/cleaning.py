class Thing():
    """Defines a thing capable of being clean/dirty, there/hidden"""
    de_facto_cleanliness = 5
    de_facto_sneakiness = 2
    def __init__(self, name, cleanliness=de_facto_cleanliness, sneakiness=de_facto_sneakiness):
        self.name = name
        self.cleanliness = cleanliness # low values of this mean "covered in grimy slime"
        self.sneakiness = sneakiness # infinite here means "impossible to find"
    def is_clean(self, criterium=de_facto_cleanliness):
        """returns True if clean, criterium is the minimum cleanliness acceptable"""
        return True if self.cleanliness >= criterium else False
    def is_there(self, criterium=de_facto_sneakiness):
        """returns True if found, criterium is the max sneakiness for a findable item"""
        return True if self.sneakiness <= criterium else False
    def cleanliness_state(self):
        """express cleanliness"""
        return "clean" if self.is_clean() else "dirty"
    def __repr__(self):
        return "%s (%s)" % (self.name, self.cleanliness_state())
    def set_clean(self):
        self.cleanliness = self.de_facto_cleanliness

class Cleaner():
    """Defines an entity capable of cleaning"""
    from time import sleep as get_busy
    avg_cleaning_time=3
    def __init__(self, thing_list, name='unnamed entity'):
        self.name = name
        self.things = thing_list
    def clean(self, thing):
        """Takes thing and cleans it, no exceptions"""
        self.get_busy(self.avg_cleaning_time)
        thing.set_clean()
        print "  Cleaned the %s!" % thing.name

class Wife(Cleaner):
    """The Wife is a specific type of Cleaner"""
    def get_things_to_clean(self):
        return [thing for thing in self.things if not thing.is_clean()]
    def cleaning_run(self):
        things = self.get_things_to_clean()
        for thing in things:
            self.clean(thing)
        print "  Done cleaning!"

class NothingToCleanException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Except there is nothing to clean!"

class Husband(Cleaner):
    """The Husband is a specific type of Cleaner"""
    from random import choice as pick_from
    def clean(self, thing):
        """Takes thing, if all things are clean raise exception, else clean"""
        if sum(thing.is_clean() for thing in self.things) == len(self.things):
            print "  But there's nothing to clean!"
            raise NothingToCleanException
        elif not thing.is_clean():
            thing.set_clean()
            Cleaner.clean(self, thing)
    def clean_something(self):
        something = self.pick_from(things)
        self.clean(something)
    def cleaning_run(self):
        while True:
            try:
                self.clean_something()
            except NothingToCleanException:
                break
        print "  Done cleaning!"

# main losl
from random import randint as a_number_from
from copy import deepcopy as clone
things=[]
thing_names=['kitchen', 'room', 'bathroom', 'living room']
for thing_name in thing_names:
    things.append(Thing(thing_name, a_number_from(1,20)))
the_same_things = clone(things)
wife = Wife(things, "Shariana")
husband = Husband(the_same_things, "Me")
print "List of things:"
for thing in things:
    print " - %s" % repr(thing)
print "Wife cleaning algorithm"
wife.cleaning_run()
print "Husband cleaning algorithm"
husband.cleaning_run()

for thing in things:
    print " - %s" % repr(thing)
if sum(thing.is_clean() for thing in things) == len(things):
    print "  But there's nothing to clean!"

