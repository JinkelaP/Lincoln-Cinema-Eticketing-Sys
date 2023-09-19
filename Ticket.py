from datetime import datetime

class Ticket:
    nextID = 1000000
    def __init__(self, userID: int, screeningID: int, dateT: datetime, seat: str, paymentType: str) -> None:
        self.__userID = userID
        self.__screeningID = screeningID
        self.__dateT = dateT
        self.__seat = seat
        self.__paymentType = paymentType

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
