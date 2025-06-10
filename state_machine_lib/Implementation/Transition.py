from state_machine_lib.Abstract.AbcTransition import Transition


class Transition_0(Transition):
    def condition(self, context):
        iter_number = context.get('iteration_number')
        return context.get('input')[iter_number]==0
    
class Transition_1(Transition):
    def condition(self, context):
        iter_number = context.get('iteration_number')
        return context.get('input')[iter_number]==1

class Transition_2(Transition):
    def condition(self, context):
        iter_number = context.get('iteration_number')
        return context.get('input')[iter_number]==0

class Transition_3(Transition):
    def condition(self, context):
        iter_number = context.get('iteration_number')
        return context.get('input')[iter_number]==0

class Transition_4(Transition):
    def condition(self, context):
        iter_number = context.get('iteration_number')
        return context.get('input')[iter_number]==1


