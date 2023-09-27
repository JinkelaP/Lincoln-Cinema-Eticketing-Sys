from datetime import datetime
from decimal import Decimal

# @class Ticket
# @brief This class represents a movie ticket.
# The ticket contains various details like user ID, screening ID, seat information, price, etc.
class Ticket:
    # @brief Class variable to generate unique ticket IDs.
    nextID = 1000000

    # @brief Constructor for the Ticket class.
    # @param userID The ID of the user who booked the ticket.
    # @param screeningID The ID of the screening.
    # @param dateT The date and time of the screening.
    # @param seat The seat number.
    # @param paymentType The type/method of payment used.
    # @param price The price of the ticket.
    # @param valid A boolean indicating if the ticket is valid or not.
    def __init__(self, userID: int, screeningID: int, dateT: datetime, seat: str, paymentType: str, price: Decimal, valid=True) -> None:
        self.__userID = userID
        self.__screeningID = screeningID
        self.__dateT = dateT
        self.__seat = seat
        self.__paymentType = paymentType
        self.__price = price
        self.__valid = valid

        # @brief Auto-generating unique ticket IDs.
        self.__ticketID = Ticket.nextID
        Ticket.nextID += 1

    # @brief A string representation of the ticket.
    # @return A formatted string containing user ID, date, and seat.
    def __str__(self) -> str:
        return f'{str(self.__userID)} {self.__dateT.strftime("%m-%d-%Y, %H:%M")} {self.__seat}'
    
    # getter and setter needed

    # @brief Getter method for userID.
    @property
    def userID(self) -> int:
        return self.__userID
    
    # @brief Getter method for screeningID.
    @property
    def screeningID(self) -> int:
        return self.__screeningID
    
    # @brief Getter method for dateT.
    @property
    def dateT(self) -> datetime:
        return self.__dateT
    
    # @brief Getter method for seat.
    @property
    def seat(self) -> str:
        return self.__seat
    
    # @brief Getter method for paymentType.
    @property
    def paymentType(self) -> str:
        return self.__paymentType
    
    # @brief Getter method for price.
    @property
    def price(self) -> Decimal:
        return self.__price
    
    # @brief Getter method for ticketID.
    @property
    def ticketID(self) -> Decimal:
        return self.__ticketID
    
    # @brief Getter method for valid.
    @property
    def valid(self) -> bool:
        return self.__valid
    
    # @brief Setter method for valid.
    @valid.setter
    def valid(self, status: bool) -> None:
        self.__valid = status