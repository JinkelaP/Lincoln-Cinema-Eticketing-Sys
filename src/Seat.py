
class Seat:
    """@class Seat"""
    """! @brief Represents a cinema seat with an ID, availability status, and an associated user if occupied."""

    
    def __init__(self, column: str, row: int, available: bool = True) -> None:
        """! @brief Constructor for the Seat class.
     @param column The column for the seat.
     @param row The row number for the seat.
     @param available An optional parameter indicating whether the seat is available or occupied. 
     By default, it is set to True."""
        self.__available = available
        self.__seatID = f"{column}{row}"
        self.__userID = None

    
    def __str__(self) -> str:
        """! @brief A string representation of the seat."""
        return f'{self.__seatID} {str(self.__available)}'
    
    # getter and setter needed
    
    @property
    def available(self) -> bool:
        """! @brief Getter for the availability status of the seat."""
        return self.__available
    
    
    @property
    def seatID(self) -> str:
        """! @brief Getter for the seatID."""
        return self.__seatID
    
    
    @property
    def userID(self) -> str:
        """! @brief Getter for the associated user ID, if any."""
        return self.__userID

    
    @available.setter
    def available(self, availability: bool):
        """! @brief Setter for the availability status of the seat."""
        self.__available = availability

    
    @userID.setter
    def userID(self, userID: int):
        """! @brief Setter for associating a user ID with the seat."""
        self.__userID = userID
    
