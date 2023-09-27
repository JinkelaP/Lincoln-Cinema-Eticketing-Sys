from abc import ABC, abstractmethod
from Ticket import Ticket
from Coupon import Coupon


class User(ABC):
    """@class User
@brief This abstract class represents a user with a unique ID, username, and password. It also create a messege list."""
    
    nextID = 10
    """@brief Class variable to generate unique user IDs."""

    
    def __init__(self, name: str, psw: str) -> None:
        """! Constructor for the User class.
    @param name The name (username) of the user.
    @param psw The password for the user."""
        self._username = name
        self._userID = User.nextID
        self._userPassword = psw
        self._userMsg = []
        User.nextID += 1

    
    def __str__(self) -> str:
        """!@brief A string representation of the user."""
        return str(self._userID) + " " + self._username
    
    # getter and setter needed
    
    @property
    def username(self) -> str:
        """!@brief Getter for the username."""
        return self._username

    
    @property
    def userID(self) -> int:
        """!@brief Getter for the userID."""
        return self._userID
    
    
    @property
    def userPassword(self) -> int:
        """!@brief Getter for the userPassword."""
        return self._userPassword
    
    
    @property
    def userMsg(self) -> int:
        """!@brief Getter for the userMsg."""
        return self._userMsg
    
    
    @username.setter
    def username(self, name: str) -> None:
        """!@brief Setter for username."""
        self._username = name

    
    @userPassword.setter
    def userPassword(self, psw: str) -> None:
        """!@brief Setter for password."""
        self._userPassword = psw

    
    def userMsgAdd(self, msg: str) -> None:
        """!@brief add messege to the user."""
        self._userMsg.append(msg)


class Customer(User):
    """!@class Customer
@brief Represents a customer user, inheriting attributes and methods from the User class.
Additional attributes include tickets and coupons."""
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)
        self.__ticket = []
        self.__coupon = []

    
    @property
    def ticket(self) -> list:
        """!@brief Getter for the ticket."""
        return self.__ticket
    
    
    @property
    def coupon(self) -> list:
        """!@brief Getter for the coupon."""
        return self.__coupon
    
    
    def addTicket(self, ticket: Ticket) -> None:
        """!@brief Adds a new ticket to the customer's ticket list.
    @param ticket The Ticket object to be added."""
        self.__ticket.append(ticket)
    
    
    def removeTicket(self, ticket: Ticket) -> None:
        """!@brief Marks a ticket as invalid in the customer's ticket list.
    @param ticket The Ticket object to be marked as invalid."""
        for i in self.__ticket:
            if i == ticket:
                i.valid = False

    
    def addCoupon(self, coupon: Coupon) -> None:
        """!@brief Adds a new coupon to the customer's coupon list.
    @param coupon The Coupon object to be added."""
        self.__coupon.append(coupon)

    
    def removeCoupon(self, coupon: Coupon) -> None:
        """!@brief Marks a coupon as invalid in the customer's coupon list.
    @param coupon The Coupon object to be marked as invalid."""
        for i in self.__coupon:
            if i == coupon:
                i.valid = False
                                                                 

class Staff(User):
    """!@class Staff
@brief Represents a staff user, inheriting attributes and methods from the User class."""
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)


class Admin(User):
    """!@class Staff
@brief Represents a admin user, inheriting attributes and methods from the User class."""
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)