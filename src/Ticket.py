from datetime import datetime
from decimal import Decimal


class Ticket:
    """! Ticket
      @brief This class represents a movie ticket.
      The ticket contains various details like user ID, screening ID, seat information, price, etc."""
    
    nextID = 1000000

    
    def __init__(self, userID: int, screeningID: int, dateT: datetime, seat: str, paymentType: str, price: Decimal, valid=True) -> None:
        """! Constructor for the Ticket class.
    @param userID The ID of the user who booked the ticket.
    @param screeningID The ID of the screening.
    @param dateT The date and time of the screening.
    @param seat The seat number.
    @param paymentType The type/method of payment used.
    @param price The price of the ticket.
    @param valid A boolean indicating if the ticket is valid or not."""
        self.__userID = userID
        self.__screeningID = screeningID
        self.__dateT = dateT
        self.__seat = seat
        self.__paymentType = paymentType
        self.__price = price
        self.__valid = valid

        
        self.__ticketID = Ticket.nextID
        """! @brief Auto-generating unique ticket IDs."""
        Ticket.nextID += 1

    
    def __str__(self) -> str:
        """! @brief A string representation of the ticket.
    @return A formatted string containing user ID, date, and seat."""
        return f'{str(self.__userID)} {self.__dateT.strftime("%m-%d-%Y, %H:%M")} {self.__seat}'
    
    # getter and setter needed

    
    @property
    def userID(self) -> int:
        """!@brief Getter method for userID."""
        return self.__userID
    
    
    @property
    def screeningID(self) -> int:
        """!@brief Getter method for screeningID."""
        return self.__screeningID
    
    
    @property
    def dateT(self) -> datetime:
        """!@brief Getter method for dateT."""
        return self.__dateT
    
    
    @property
    def seat(self) -> str:
        """!@brief Getter method for seat."""
        return self.__seat
    
    
    @property
    def paymentType(self) -> str:
        """!@brief Getter method for paymentType."""
        return self.__paymentType
    
    
    @property
    def price(self) -> Decimal:
        """!@brief Getter method for price."""
        return self.__price
    
    
    @property
    def ticketID(self) -> Decimal:
        """!@brief Getter method for ticketID."""
        return self.__ticketID
    
    
    @property
    def valid(self) -> bool:
        """!@brief Getter method for valid."""
        return self.__valid
    
    
    @valid.setter
    def valid(self, status: bool) -> None:
        """!@brief Setter method for valid."""
        self.__valid = status