from abc import ABC, abstractmethod
from Ticket import Ticket
from Coupon import Coupon

# @class User
# @brief This abstract class represents a user with a unique ID, username, and password. It also create a messege list.
class User(ABC):

    # @brief Class variable to generate unique user IDs.
    nextID = 10

    # @brief Constructor for the User class.
    # @param name The name (username) of the user.
    # @param psw The password for the user.
    def __init__(self, name: str, psw: str) -> None:
        self._username = name
        self._userID = User.nextID
        self._userPassword = psw
        self._userMsg = []
        User.nextID += 1

    # @brief A string representation of the user.
    def __str__(self) -> str:
        return str(self._userID) + " " + self._username
    
    # getter and setter needed
    # @brief Getter for the username.
    @property
    def username(self) -> str:
        return self._username

    # @brief Getter for the userID.
    @property
    def userID(self) -> int:
        return self._userID
    
    # @brief Getter for the userPassword.
    @property
    def userPassword(self) -> int:
        return self._userPassword
    
    # @brief Getter for the userMsg.
    @property
    def userMsg(self) -> int:
        return self._userMsg
    
    # @brief Setter for username.
    @username.setter
    def username(self, name: str) -> None:
        self._username = name

    # @brief Setter for password.
    @userPassword.setter
    def userPassword(self, psw: str) -> None:
        self._userPassword = psw

    # @brief add messege to the user.
    def userMsgAdd(self, msg: str) -> None:
        self._userMsg.append(msg)

# @class Customer
# @brief Represents a customer user, inheriting attributes and methods from the User class.
# Additional attributes include tickets and coupons.
class Customer(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)
        self.__ticket = []
        self.__coupon = []

    # @brief Getter for the ticket.
    @property
    def ticket(self) -> list:
        return self.__ticket
    
    # @brief Getter for the coupon.
    @property
    def coupon(self) -> list:
        return self.__coupon
    
    # @brief Adds a new ticket to the customer's ticket list.
    # @param ticket The Ticket object to be added.
    def addTicket(self, ticket: Ticket) -> None:
        self.__ticket.append(ticket)
    
    # @brief Marks a ticket as invalid in the customer's ticket list.
    # @param ticket The Ticket object to be marked as invalid.
    def removeTicket(self, ticket: Ticket) -> None:
        for i in self.__ticket:
            if i == ticket:
                i.valid = False

    # @brief Adds a new coupon to the customer's coupon list.
    # @param coupon The Coupon object to be added.
    def addCoupon(self, coupon: Coupon) -> None:
        self.__coupon.append(coupon)

    # @brief Marks a coupon as invalid in the customer's coupon list.
    # @param coupon The Coupon object to be marked as invalid.
    def removeCoupon(self, coupon: Coupon) -> None:
        for i in self.__coupon:
            if i == coupon:
                i.valid = False
                                                                 
# @class Staff
# @brief Represents a staff user, inheriting attributes and methods from the User class.
class Staff(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)

# @class Staff
# @brief Represents a admin user, inheriting attributes and methods from the User class.
class Admin(User):
    def __init__(self, name: str, psw: str) -> None:
        super().__init__(name, psw)