class Seat:
    def __init__(self, row: str, column: str, screeningID: int, available: bool = True) -> None:
        self.__available = available
        self.__seatID = f"{row}{column}"
        self.__screeningID = screeningID

    def __str__(self) -> str:
        return f'{self.__seatID} {str(self.__available)}'
    
    # getter and setter needed
    @property
    def available(self) -> bool:
        return self.__available
    
    @property
    def seatID(self) -> str:
        return self.__seatID
    
    @property
    def screeningID(self) -> str:
        return self.__screeningID
    
    @available.setter
    def seated(self, availability: bool):
        self.__available = availability
    
