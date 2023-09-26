class Hall:
    def __init__(self, id: int, capacity: int) -> None:
        self.__hallID = id
        self.__hallCapacity = capacity
        # self.__isOccupied = None
        # self.__moviePlaying = ''

    def __str__(self) -> str:
        return f'Hall {self._hallNumber}. Max {self._halCapacity} people.'
    
    # getter and setter needed
    @property
    def hallID(self) -> int:
        return self.__hallID

    @property
    def hallCapacity(self) -> int:
        return self.__hallCapacity
    
    # @property
    # def isOccupied(self) -> bool:
    #     return self.__isOccupied
    
    # @property
    # def moviePlaying(self) -> str:
    #     return self.__moviePlaying
    
    # @isOccupied.setter
    # def isOccupied(self, occupy: bool)-> None:
    #     self.__isOccupied = occupy

