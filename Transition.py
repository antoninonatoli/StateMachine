from AbcTransition import Transition

class Transition_1(Transition):
    def condition(self, context):
        return context.get('input')==1

class Transition_2(Transition):
    def condition(self, context):
        return context.get('input')==2

class Transition_3(Transition):
    def condition(self, context):
        return context.get('input')==1

class Transition_4(Transition):
    def condition(self, context):
        return context.get('input')==2


