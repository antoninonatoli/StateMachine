from AbcState import State


class State_1(State):
    def __call__(self, *args, **kwds):
        return "Output of state 1"

class State_2(State):
    def __call__(self, *args, **kwds):
        return "Output of state 2"

class State_3(State):
    def __call__(self, *args, **kwds):
        return "Output of state 3"
        