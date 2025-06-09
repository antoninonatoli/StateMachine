from Abstract.FSM import FSMBuilder
from Implementation.State import State_1, State_2, State_3, State_0
from Implementation.Transition import Transition_0, Transition_1, Transition_2, Transition_3, Transition_4

fsm = ( 
    FSMBuilder()
    .set_states(
        states=[
            s0:=State_0(0, 'State 0'),
            s1:=State_1(1, 'State 1'),
            s2:=State_2(2, 'State 2')
        ]
    )
    .set_transitions(
        transitions=[
            Transition_0(s0, s1),
            Transition_1(s1, s0),
            Transition_2(s1, s2),
            Transition_3(s2, s2),
            Transition_4(s2, s0)
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

res=fsm.single_run_next(context={"input":[0], "iteration_number":0})
print(res)

res=fsm.single_run_next(context={"input":[1], "iteration_number":0})
print(res)

res=fsm.single_run_next(context={"input":[0], "iteration_number":0})
print(res)

res=fsm.single_run_next(context={"input":[1], "iteration_number":0})
print(res)

res=fsm.single_run_next(context={"input":[0], "iteration_number":0})
print(res)

res=fsm.single_run_next(context={"input":[0], "iteration_number":0})
print(res)

res=fsm.single_run_next(context={"input":[1], "iteration_number":0})
print(res)
