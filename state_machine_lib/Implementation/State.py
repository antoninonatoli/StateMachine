from state_machine_lib.Abstract.AbcState import State


class State_0(State):
    def __call__(self, *args, **kwds):
        print("Output of state 0") 

class State_1(State):
    def __call__(self, *args, **kwds):
        print("Output of state 1")

class State_2(State):
    def __call__(self, *args, **kwds):
        print("Output of state 2")

class State_3(State):
    def __call__(self, *args, **kwds):
        print("Output of state 3")
        