from datetime import date, datetime



class Movie:
    """! Movie
@brief This class represents a movie with its attributes.
The movie contains details like its name, language, genre, release date, and duration (min)."""

    
    nextID = 1000
    """!@brief Class variable to generate unique movie IDs."""

    
    def __init__(self, name: str, langauge: str, genre: str, releaseDate: date, duration: int) -> None:
        """! Constructor for the Movie class.
    @param name The name of the movie.
    @param langauge The language of the movie.
    @param genre The genre of the movie (e.g., action, drama).
    @param releaseDate The official release date of the movie.
    @param duration The duration of the movie in minutes."""
        self.__movieName = name
        self.__lang = langauge
        self.__genre = genre
        self.__releaseDate = releaseDate
        self.__durationMin = duration

        
        self.__movieID = Movie.nextID
        """!@brief Auto-generating unique movieID."""
        Movie.nextID += 1

    
    def __str__(self) -> str:
        """! A string representation of the movie.
    @return A formatted string containing movie ID and its name."""
        return str(self.__movieID) + " " + self.__movieName
    
    # getter and setter needed

    
    @property
    def movieName(self) -> str:
        """!@brief Getter for the movieName."""
        return self.__movieName

    
    @property
    def lang(self) -> str:
        """!@brief Getter for the lang."""
        return self.__lang
    
    
    @property
    def genre(self) -> str:
        """!@brief Getter for the genre."""
        return self.__genre
    
    
    @property
    def releaseDate(self) -> date:
        """!@brief Getter for releaseDate."""
        return self.__releaseDate
    
    
    @property
    def duration(self) -> int:
        """!@brief Getter for duration."""
        return self.__durationMin
    
    
    @property
    def movieID(self) -> int:
        """!@brief Getter for movieID."""
        return self.__movieID
