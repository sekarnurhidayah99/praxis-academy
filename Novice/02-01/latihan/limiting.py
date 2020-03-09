from collections import namedtuple
VerbTenses = namedtuple('VerbTenses', ['past', 'present', 'future'])
# versus
class VerbTenses(object):
    def __init__(self, past, present, future):
        self.past = past,
        self.present = present
        self.future = future

class Bus(object):
     passengers = set()
     def add_passenger(self, person):
        self.passengers.add(person)

bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
bus1.passengers  
bus2.passengers  