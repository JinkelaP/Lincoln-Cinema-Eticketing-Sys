from datetime import datetime

class Screening:
    nextID = 100000
    def __init__(self, movieID: int, dateT: datetime) -> None:
        self.__movieID = movieID
        self.__dateT = dateT

        self.__screeningID = Screening.nextID
        Screening.nextID += 1

    def __str__(self) -> str:
        return str(self.__movieID) + " " + self.__dateT.strftime("%m-%d-%Y, %H:%M")
    
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
    
