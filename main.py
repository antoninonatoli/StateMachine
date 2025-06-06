from FSM import FSM
from State import State
from Transition import Transition

fsm = FSM()

states = [
    s0:=State(0, 'Initial State'),
    s1:=State(1, 'State 1'),
    s2:=State(2, 'State 2')
]

transitions = [
    Transition(s0, s1, 1),
    Transition(s0, s2, 2),
    Transition(s1, s2, 1),
    Transition(s1, s0, 2),
]

inputs = [
    1, 2, 1, 2, 1, 1
]

for each in states:
    fsm.add_state(each)
for each in transitions:
    fsm.add_transition(each)



fsm.set_initial_state(s0)
fsm.set_final_state(s1)
result = fsm(inputs)
print(result)
