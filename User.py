class User:
    nextID = 10
    def __init__(self, name: str) -> None:
        self._username = name
        self._userID = User.nextID
        User.nextID += 1

    def __str__(self):
        return str(self._movieID) + " " + self._movieName
    
    # getter and setter needed
    @property
    def movieName(self):
        return self._movieName

    @property
    def movieDirector(self):
        return self._movieDirector
    
    @property
    def movieType(self):
        return self._movieType
    
    @property
    def movieDuration(self):
        return self._movieDuration
    
    @property
    def movieID(self):
        return self._movieID