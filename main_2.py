from state_machine_lib.Abstract.FSM import FSMBuilder
from state_machine_lib.Implementation.State import State_1, State_2, State_3
from state_machine_lib.Implementation.Transition import Transition_1, Transition_2, Transition_3, Transition_4

fsm = ( 
    FSMBuilder()
    .set_states(
        states=[
            s0:=State_1(0),
            s1:=State_2(1),
            s2:=State_3(2)
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



result = fsm(
    context={
        "input": [
            1, 2, 1, 2, 1, 1
        ]
    }
)


print(result)
