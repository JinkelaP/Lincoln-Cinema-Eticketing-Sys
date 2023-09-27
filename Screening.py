from datetime import datetime
from Seat import Seat

# @class Screening
# @brief Represents a specific screening of a movie in a particular hall.
class Screening:
    # @brief Class variable to generate unique Screening IDs.
    nextID = 100000

    # @brief Constructor for the Screening class.
    # @param movieID The ID of the movie being screened.
    # @param dateT The start date and time of the screening.
    # @param dateTEnd The end date and time of the screening.
    # @param hallID The ID of the hall where the movie will be screened.
    # @param hallSeat A list of seats in the hall.
    def __init__(self, movieID: int, dateT: datetime, dateTEnd: datetime, hallID: int, hallSeat: list) -> None:
        self.__movieID = movieID
        self.__dateT = dateT
        self.__dateTEnd = dateTEnd
        self.__hallID = hallID
        self.__hallSeat = []
        self.__valid = True

        # @brief Creating an unique screeningID
        self.__screeningID = Screening.nextID
        Screening.nextID += 1

    # @brief A string representation of the screening.
    def __str__(self) -> str:
        return str(self.__movieID) + " " + self.__dateT.strftime("%m-%d-%Y, %H:%M")
    
    # @brief Marks a seat as occupied and associates a user with it.
    # @param seatID The ID of the seat to be marked.
    # @param userID The ID of the user occupying the seat.
    def markSeatFalse(self, seatID: str, userID: int):
        for i in self.__hallSeat:
            if i.seatID == seatID:
                i.seated(False)
                i.userID = userID
                break



    # getter and setter needed
    # @brief Getter for the movie ID.
    @property
    def movieID(self) -> int:
        return self.__movieID
    
    # @brief Getter for the screening ID.
    @property
    def screeningID(self) -> int:
        return self.__screeningID
    
    # @brief Getter for the start date and time of the screening.
    @property
    def dateT(self) -> datetime:
        return self.__dateT
    
    # @brief Getter for the end date and time of the screening.
    @property
    def dateTEnd(self) -> datetime:
        return self.__dateTEnd
    
    # @brief Getter for the hall ID.
    @property
    def hallID(self) -> int:
        return self.__hallID
    
    # @brief Getter for the list of seats in the hall.
    @property
    def hallSeat(self) -> list:
        return self.__hallSeat
    
    # @brief Getter for the validity status of the screening.
    @property
    def valid(self) -> bool:
        return self.__valid
    
    # @brief Setter for the validity status of the screening.
    @valid.setter
    def valid(self, valid: bool) -> None:
        self.__valid = valid

    
