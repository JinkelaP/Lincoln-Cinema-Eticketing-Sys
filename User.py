from abc import ABC, abstractmethod

class User(ABC):
    nextID = 10

    def __init__(self, name: str) -> None:
        self._username = name
        self._userID = User.nextID
        User.nextID += 1

    def __str__(self) -> str:
        return str(self._userID) + " " + self._username
    
    # getter and setter needed
    @property
    def username(self) -> str:
        return self._username

    @property
    def userID(self) -> int:
        return self._userID
    
    @username.setter
    def usernameSet(self, name: str) -> None:
        self._username = name

class Customer(User):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__ticket = []
        self.__coupon = []

