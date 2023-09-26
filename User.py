from abc import ABC, abstractmethod

class User(ABC):
    nextID = 10

    def __init__(self, name: str, psw: str) -> None:
        self._username = name
        self._userID = User.nextID
        self._userPassword = psw
        self._userMsg = []
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
    
    @property
    def userPassword(self) -> int:
        return self._userPassword
    
    @property
    def userMsg(self) -> int:
        return self._userMsg
    
    @username.setter
    def usernameSet(self, name: str) -> None:
        self._username = name

    @userPassword.setter
    def userPasswordSet(self, psw: str) -> None:
        self._userPassword = psw

    @userMsg.setter
    def userMsgSet(self, msg: str) -> None:
        self._userMsg.append(msg)

class Customer(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)
        self.__ticket = []
        self.__coupon = []

    @property
    def ticket(self) -> list:
        return self.__ticket
    
    @property
    def coupon(self) -> list:
        return self.__coupon
                                                                 

class Staff(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)

class Admin(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)