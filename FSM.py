class FSM:
    def __init__(self):
        self.current_state = None
        self.states = set()
        self.initial_state = None
        self.final_states = set()
        self.transitions = set()
    
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
    
    def next(self):
        if self.current_state in self.final_states:
            return
        
        next_state = self.get_transition(self.current_input).target_state
        self.current_state = next_state

    def get_transition(self, input_value):
        # I know the input_value and current state...
        #Supposing the FSM is deterministic...
        
        transitions_iter = iter(self.transitions)
        while not (
          (transition:=next(transitions_iter)).source_state == self.current_state 
          and transition.input_value==input_value
        ):
            continue
        return transition


    def __call__(self, input_values):
        self.current_state = self.initial_state
        for arg in input_values:
            self.current_input = arg
            #self.curent_state()
            self.next()
        if self.current_state in self.final_states:
            return True
        return False
    
        #while not self.current_state in self.final_states:
        #    print(f"Running state: {self.state.__class__.__name__}")
        #    self.current_input = arg
        #    # self.state()
        #    self.next()
        #print(f"Running final state: {self.state.__class__.__name__}")
        ##self.state()
