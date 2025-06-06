from FSM import FSM
from AbcState import State
from AbcTransition import Transition
from State import State_1, State_2, State_3
from Transition import Transition_1, Transition_2, Transition_3, Transition_4

fsm = FSM()

states = [
    s0:=State_1(0, 'Initial State'),
    s1:=State_2(1, 'State 1'),
    s2:=State_3(2, 'State 2')
]

transitions = [
    Transition_1(s0, s1),
    Transition_2(s0, s2),
    Transition_3(s1, s2),
    Transition_4(s1, s0),
]

context = {
    "input": [
        1, 2, 1, 2, 1, 1
    ]
}


for each in states:
    fsm.add_state(each)
for each in transitions:
    fsm.add_transition(each)



fsm.set_initial_state(s0)
fsm.set_final_state(s2)
result = fsm(context)
print(result)
