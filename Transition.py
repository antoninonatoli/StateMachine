class Transition:
    def __init__(
            self,
            source_state,
            target_state,
            input_value
        ):
        self.source_state = source_state
        self.target_state = target_state
        self.input_value = input_value
    
    def __eq__(self, other):
        # This implementation considers only Deterministic FSM.
        # NON Deterministic FSM will require to add 
        # self.target_state == other.target_state
        if isinstance(other, Transition):
            return (
                self.source_state == other.source_state and
                self.input_value == other.input_value
            )
    
    def __hash__(self):
        return hash((self.source_state, self.input_value))
    
    def __str__(self):
        return f"t_{self.source_state}_{self.target_state}_{self.input_value}"
    