from abc import ABC, abstractmethod

class User(ABC):
    nextID = 10

    def __init__(self, name: str) -> None:
        self._username = name
        self._userID = User.nextID
        User.nextID += 1

    def __str__(self):
        return str(self._userID) + " " + self._username
    
    # getter and setter needed
    @property
    def username(self) -> str:
        return self._username

    @property
    def userID(self) -> int:
        return self._userID
    
    @username.setter
    def username(self, name: str) -> None:
        self._username = name

class Customer(User):

    def __init__(self, name: str) -> None:


    # getter and setter needed
    @property
    def username(self) -> str:
        return self._username

    @property
    def userID(self) -> int:
        return self._userID
    
    @username.setter
    def username(self, name: str) -> None:
        self._username = name
        return self._username