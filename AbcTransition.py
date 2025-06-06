from abc import abstractmethod

class Transition:
    def __init__(
            self,
            source_state,
            target_state,
        ):
        self.source_state = source_state
        self.target_state = target_state
    
    def __eq__(self, other):
        if isinstance(other, Transition):
            return (
                self.source_state == other.source_state and
                self.target_state == other.target_state
            )
    
    def __hash__(self):
        return hash((self.source_state, self.target_state))
    
    def __str__(self):
        return f"t_{self.source_state}_{self.target_state}"
    
    @abstractmethod
    def condition(self, context: dict) -> bool:
        raise NotImplementedError("Subclasses must implement this method")
    

