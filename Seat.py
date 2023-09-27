class Seat:
    def __init__(self, column: str, row: int, available: bool = True) -> None:
        self.__available = available
        self.__seatID = f"{column}{row}"
        self.__userID = None

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
    def userID(self) -> str:
        return self.__userID

    
    @available.setter
    def available(self, availability: bool):
        self.__available = availability

    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID
    
