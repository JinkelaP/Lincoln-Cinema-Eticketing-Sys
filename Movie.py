from datetime import date, datetime


# @class Movie
# @brief This class represents a movie with its attributes.
# The movie contains details like its name, language, genre, release date, and duration (min).
class Movie:

    # @brief Class variable to generate unique movie IDs.
    nextID = 1000

    # @brief Constructor for the Movie class.
    # @param name The name of the movie.
    # @param langauge The language of the movie.
    # @param genre The genre of the movie (e.g., action, drama).
    # @param releaseDate The official release date of the movie.
    # @param duration The duration of the movie in minutes.
    def __init__(self, name: str, langauge: str, genre: str, releaseDate: date, duration: int) -> None:
        self.__movieName = name
        self.__lang = langauge
        self.__genre = genre
        self.__releaseDate = releaseDate
        self.__durationMin = duration

        # @brief Auto-generating unique movieID.
        self.__movieID = Movie.nextID
        Movie.nextID += 1

    # @brief A string representation of the movie.
    # @return A formatted string containing movie ID and its name.
    def __str__(self) -> str:
        return str(self.__movieID) + " " + self.__movieName
    
    # getter and setter needed

    # @brief Getter for the movieName.
    @property
    def movieName(self) -> str:
        return self.__movieName

    # @brief Getter for the lang.
    @property
    def lang(self) -> str:
        return self.__lang
    
    # @brief Getter for the genre.
    @property
    def genre(self) -> str:
        return self.__genre
    
    # @brief Getter for releaseDate.
    @property
    def releaseDate(self) -> date:
        return self.__releaseDate
    
    # @brief Getter for duration.
    @property
    def duration(self) -> int:
        return self.__durationMin
    
    # @brief Getter for movieID.
    @property
    def movieID(self) -> int:
        return self.__movieID
