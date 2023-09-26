from abc import ABC, abstractmethod
from Ticket import Ticket
from Coupon import Coupon

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

    def userMsgAdd(self, msg: str) -> None:
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
    
    def addTicket(self, ticket: Ticket) -> None:
        self.__ticket.append(ticket)
    
    def removeTicket(self, ticket: Ticket) -> None:
        for i in self.__ticket:
            if i == ticket:
                i.valid = False

    def addCoupon(self, coupon: Coupon) -> None:
        self.__coupon.append(coupon)

    def removeCoupon(self, coupon: Coupon) -> None:
        for i in self.__coupon:
            if i == coupon:
                i.valid = False
                                                                 

class Staff(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)

class Admin(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)