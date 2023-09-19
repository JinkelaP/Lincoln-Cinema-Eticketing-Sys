class Movie:
    nextID = 1000
    def __init__(self, name: str, director: str, type: str, duration: int) -> None:
        self._movieName = name
        self._movieDirector = director
        self._movieType = type
        self._movieDuration = duration
        self._movieID = Movie.nextID
        Movie.nextID += 1

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