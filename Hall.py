class Hall:
    def __init__(self, id: int, capacity: int) -> None:
        self._hallNumber = id
        self._halCapacity = capacity
        self._isOccupied = None
        self._moviePlaying = ''

    def __str__(self):
        return f'Hall {self._hallNumber}. Max {self._halCapacity} people.'
    
    # getter and setter needed
    @property
    def hallNumber(self) -> int:
        return self._hallNumber

    @property
    def halCapacity(self) -> int:
        return self._halCapacity
    
    @property
    def isOccupied(self) -> bool:
        return self._isOccupied
    
    @property
    def moviePlaying(self) -> str:
        return self._moviePlaying
    
    @isOccupied.setter
    def isOccupied(self, occupy: bool)-> None:
        self._isOccupied = occupy

