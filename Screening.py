from datetime import datetime
from Seat import Seat

class Screening:
    nextID = 100000
    def __init__(self, movieID: int, dateT: datetime, hallID: int, hallSeat: list) -> None:
        self.__movieID = movieID
        self.__dateT = dateT
        self.__hallID = hallID
        self.__hallSeat = []

        self.__screeningID = Screening.nextID
        Screening.nextID += 1

    def __str__(self) -> str:
        return str(self.__movieID) + " " + self.__dateT.strftime("%m-%d-%Y, %H:%M")
    
    def addSeat(self, seat: Seat) -> None:
        self.__hallSeat.append(seat)

    def markSeatFalse(self, seatID: str):
        for i in self.__hallSeat:
            if i.seatID == seatID:
                i.seated(False)
                break



    # getter and setter needed
    @property
    def movieID(self) -> int:
        return self.__movieID
    
    @property
    def screeningID(self) -> int:
        return self.__screeningID
    
    @property
    def dateT(self) -> datetime:
        return self.__dateT
    
    @property
    def hallID(self) -> int:
        return self.__hallID
    
    @property
    def hallSeat(self) -> list:
        return self.__hallSeat

    
