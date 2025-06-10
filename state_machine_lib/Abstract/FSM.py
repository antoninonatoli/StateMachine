from typing import List
from .AbcState import State
from .AbcTransition import Transition

class FSM:
    def __init__(self):
        self.current_state = None
        self.states = set()
        self.initial_state = None
        self.final_states = set()
        self.transitions = set()
        self.iteration_number = 0
    
    def add_state(self, state):
        if state not in self.states:
            self.states.add(state)
    
    def add_transition(self, transition):
        if transition not in self.transitions:
            self.transitions.add(transition)

    def set_initial_state(self, state):
        if state not in self.states:
            raise Exception(f"State {state} not in FSM states")
        self.initial_state = state
    
    def set_final_state(self, state):
        if state not in self.states:
            raise Exception(f"State {state} not in FSM states")
        if state not in self.final_states:
            self.final_states.add(state)
    
    def next(self, context):
        if self.current_state in self.final_states:
            return True
        
        next_state = self.get_transition(context).target_state
        self.current_state = next_state
        self.iteration_number += 1
        return False

    def get_transition(self, context):
        #Supposing the FSM is deterministic...
        
        transitions_iter = iter(self.transitions)
        while not (
          (transition:=next(transitions_iter)).source_state == self.current_state 
          and transition.condition(context)
        ):
            continue
        return transition

    def single_run_next(self, context):
        self.current_state()
        is_final = self.next(context)
        return is_final
        

    def __call__(self, context):
        context.setdefault("iteration_number", self.iteration_number)
        self.current_state = self.initial_state
        try:
            while not self.current_state in self.final_states:
                print(f"Running state: {self.current_state.__class__.__name__}")
                self.current_state()    
                self.next(context)
                context["iteration_number"] = self.iteration_number
            
            print(f"Running final state: {self.current_state.__class__.__name__}")
            self.current_state()
            #self.current_state.output
        except StopIteration as e:
            print(f"Transition not found ! {str(e)}")
            return False
        


class FSMBuilder:

    def __init__(self):
        self.fsm = FSM()
    
    def set_states(self, states: List[State]):
        for each in states: 
            self.fsm.add_state(each)
        return self
    
    def set_transitions(self, transitions: List[Transition]):
        for each in transitions:
            self.fsm.add_transition(each)
        return self
    
    def set_initial_state(self, state:State):
        self.fsm.set_initial_state(state)
        return self
    
    def set_final_states(self, states: List[State]):
        for each in states:
            self.fsm.set_final_state(each)
        return self
    
    def set_additional_attributes(self, **kwargs):
        self.fsm.__dict__.update(kwargs)
        return self
    
    def build(self):
        self.fsm.current_state = self.fsm.initial_state
        return self.fsm
    