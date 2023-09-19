class Seat:
    nextID = 1
    def __init__(self, available: bool = True) -> None:
        self.__available = available
        self.__seatID = Seat.nextID
        Seat.nextID += 1

    def __str__(self) -> str:
        return f'{str(self.__seatID)} {self.__available}'
    
    # getter and setter needed
    @property
    def available(self) -> bool:
        return self.__available
    
    @property
    def seatID(self) -> int:
        return self.__seatID
    
