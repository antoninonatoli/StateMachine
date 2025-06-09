from Abstract.FSM import FSMBuilder
from Implementation.State import State_1, State_2, State_3
from Implementation.Transition import Transition_1, Transition_2, Transition_3, Transition_4

fsm = ( 
    FSMBuilder()
    .set_states(
        states=[
            s0:=State_1(0, 'Initial State'),
            s1:=State_2(1, 'State 1'),
            s2:=State_3(2, 'State 2')
        ]
    )
    .set_transitions(
        transitions=[
            Transition_1(s0, s1),
            Transition_2(s0, s2),
            Transition_3(s1, s2),
            Transition_4(s1, s0),
        ]
    )
    .set_initial_state(
        state=s0
    )
    .set_final_states(
        states=[
            s2
        ]
    ).build()
)

while not (res:=fsm.single_run_next(context={"input":[1], "iteration_number":0})):
    print(res)
print(res)
