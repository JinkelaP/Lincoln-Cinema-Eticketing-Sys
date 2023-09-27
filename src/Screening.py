from datetime import datetime
from Seat import Seat


class Screening:
    """! Screening
    @brief Represents a specific screening of a movie in a particular hall."""
    
    nextID = 100000
    """@brief Class variable to generate unique Screening IDs."""

    
    def __init__(self, movieID: int, dateT: datetime, dateTEnd: datetime, hallID: int, hallSeat: list) -> None:
        """! Constructor for the Screening class.
    @param movieID The ID of the movie being screened.
    @param dateT The start date and time of the screening.
    @param dateTEnd The end date and time of the screening.
    @param hallID The ID of the hall where the movie will be screened.
    @param hallSeat A list of seats in the hall."""
        self.__movieID = movieID
        self.__dateT = dateT
        self.__dateTEnd = dateTEnd
        self.__hallID = hallID
        self.__hallSeat = []
        self.__valid = True

        
        self.__screeningID = Screening.nextID
        """! Creating an unique screeningID"""
        Screening.nextID += 1

    
    def __str__(self) -> str:
        """! A string representation of the screening."""
        return str(self.__movieID) + " " + self.__dateT.strftime("%m-%d-%Y, %H:%M")
    
    
    def markSeatFalse(self, seatID: str, userID: int):
        """! Marks a seat as occupied and associates a user with it.
    @param seatID The ID of the seat to be marked.
    @param userID The ID of the user occupying the seat."""
        for i in self.__hallSeat:
            if i.seatID == seatID:
                i.seated(False)
                i.userID = userID
                break



    # getter and setter needed
    
    @property
    def movieID(self) -> int:
        """!@brief Getter for the movie ID."""
        return self.__movieID
    
    
    @property
    def screeningID(self) -> int:
        """!@brief Getter for the screening ID."""
        return self.__screeningID
    
    
    @property
    def dateT(self) -> datetime:
        """!@brief Getter for the start date and time of the screening."""
        return self.__dateT
    
    
    @property
    def dateTEnd(self) -> datetime:
        """!@brief Getter for the end date and time of the screening."""
        return self.__dateTEnd
    
    
    @property
    def hallID(self) -> int:
        """!@brief Getter for the hall ID."""
        return self.__hallID
    
    
    @property
    def hallSeat(self) -> list:
        """!@brief Getter for the list of seats in the hall."""
        return self.__hallSeat
    
    
    @property
    def valid(self) -> bool:
        """!@brief Getter for the validity status of the screening."""
        return self.__valid
    
    
    @valid.setter
    def valid(self, valid: bool) -> None:
        """!@brief Setter for the validity status of the screening."""
        self.__valid = valid

    
