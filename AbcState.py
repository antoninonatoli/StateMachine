from abc import ABC, abstractmethod
from typing import Callable

class State:
    
    def __init__(self, id:int, output: Callable):
        self.id = id
        self.name = f"s{id}"
        self.output = output
    
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses implement __call__ method")
    
    def __eq__(self, other):
        if isinstance(other, State):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)
    
    def __str__(self):
        return self.name
    
    