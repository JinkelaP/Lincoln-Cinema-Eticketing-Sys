class Hall:
    def __init__(self, id: int, capacity: int) -> None:
        self.__hallNumber = id
        self.__halCapacity = capacity
        self.__isOccupied = None
        self.__moviePlaying = ''

    def __str__(self) -> str:
        return f'Hall {self._hallNumber}. Max {self._halCapacity} people.'
    
    # getter and setter needed
    @property
    def hallNumber(self) -> int:
        return self.__hallNumber

    @property
    def halCapacity(self) -> int:
        return self.__halCapacity
    
    @property
    def isOccupied(self) -> bool:
        return self.__isOccupied
    
    @property
    def moviePlaying(self) -> str:
        return self.__moviePlaying
    
    @isOccupied.setter
    def isOccupied(self, occupy: bool)-> None:
        self.__isOccupied = occupy

