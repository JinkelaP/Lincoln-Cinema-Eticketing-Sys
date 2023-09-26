from datetime import datetime
from decimal import Decimal

class Ticket:
    nextID = 1000000
    def __init__(self, userID: int, screeningID: int, dateT: datetime, seat: str, paymentType: str, price: Decimal, valid=True) -> None:
        self.__userID = userID
        self.__screeningID = screeningID
        self.__dateT = dateT
        self.__seat = seat
        self.__paymentType = paymentType
        self.__price = price
        self.__valid = valid

        self.__ticketID = Ticket.nextID
        Ticket.nextID += 1

    def __str__(self) -> str:
        return f'{str(self.__userID)} {self.__dateT.strftime("%m-%d-%Y, %H:%M")} {self.__seat}'
    
    # getter and setter needed
    @property
    def userID(self) -> int:
        return self.__userID
    
    @property
    def screeningID(self) -> int:
        return self.__screeningID
    
    @property
    def dateT(self) -> datetime:
        return self.__dateT
    
    @property
    def seat(self) -> str:
        return self.__seat
    
    @property
    def paymentType(self) -> str:
        return self.__paymentType
    
    @property
    def price(self) -> Decimal:
        return self.__price
    
    @property
    def ticketID(self) -> Decimal:
        return self.__ticketID
    
    @property
    def valid(self) -> bool:
        return self.__valid
    
    @valid.setter
    def validSet(self, status: bool) -> None:
        self.__valid = status