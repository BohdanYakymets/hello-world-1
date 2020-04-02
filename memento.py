
from abc import ABC, abstractmethod
from random import sample
from string import ascii_letters, digits
import copy
class Memento(ABC):
   
    def get_name(self)->list:
        pass



class Originator():
    
    _state = None
   
    def __init__(self, state:list)->None:
        self._state = state
        

    def do_something(self, func):

        self._state = func
        
    def __copy__(self):
        my_copy = self.save()
        return my_copy


    def save(self) -> Memento:
      
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento)->None:
        
        self._state = memento.get_state()
        




class ConcreteMemento(Memento):
    def __init__(self, state:list)->None:
        self._state = state
    def __copy__(self):
        my_copy = self
        return my_copy   
    
    def get_state(self)->list:
       
        return self._state

    def get_name(self)->str:
       
        return f"{str(self._state)}..."




class Caretaker():
   

    def __init__(self, originator: Originator)->None:
        self._mementos = []
        self._memredo = []
        self._originator = originator

    def backup(self)->None:
        
        st = copy.copy(self._originator.save())
        if len(self._mementos) == 5:
            self._mementos.pop(0)
        self._mementos.append(copy.deepcopy(st))

    def undo(self)->None:
        if not len(self._mementos):
            return
        self._memredo.append(copy.deepcopy(self._originator.save()))
        memento = self._mementos.pop()
        
        print(f"Restoring state to:\n{memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
    def redo(self):
        if not len(self._mementos):
            return
        memento = self._memredo.pop()
        print(f"Restoring state to:\n{memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.redo()
    def show_history(self)->None:
        
        for memento in self._mementos:
            print(memento.get_name())



