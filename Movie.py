from datetime import date, datetime

class Movie:
    nextID = 1000
    def __init__(self, name: str, langauge: str, genre: str, releaseDate: date, duration: int) -> None:
        self.__movieName = name
        self.__lang = langauge
        self.__genre = genre
        self.__releaseDate = releaseDate
        self.__durationMin = duration

        self.__screening = []
        self.__movieID = Movie.nextID
        Movie.nextID += 1

    def __str__(self) -> str:
        return str(self.__movieID) + " " + self.__movieName
    
    # getter and setter needed
    @property
    def movieName(self) -> str:
        return self.__movieName

    @property
    def lang(self) -> str:
        return self.__lang
    
    @property
    def genre(self) -> str:
        return self.__genre
    
    @property
    def releaseDate(self) -> date:
        return self.__releaseDate
    
    @property
    def duration(self) -> int:
        return self.__durationMin
    
    @property
    def screening(self) -> list:
        return self.__screening
    
    @property
    def movieID(self) -> int:
        return self.__movieID
    
    @screening.setter
    def screening(self, screening: list) -> None:
        self.__screening.append(screening)