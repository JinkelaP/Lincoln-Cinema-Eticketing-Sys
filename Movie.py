from datetime import date

class Movie:
    nextID = 1000
    def __init__(self, name: str, langauge: str, genre: str, releaseDate: date, duration: int) -> None:
        self._movieName = name
        self._lang = langauge
        self._genre = genre
        self._releaseDate = releaseDate
        self._durationMin = duration
        self._movieID = Movie.nextID
        Movie.nextID += 1

    def __str__(self):
        return str(self._movieID) + " " + self._movieName
    
    # getter and setter needed
    @property
    def movieName(self):
        return self._movieName

    @property
    def lang(self):
        return self._lang
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def releaseDate(self):
        return self._releaseDate
    
    @property
    def duration(self):
        return self._durationMin
    
    @property
    def movieID(self):
        return self._movieID