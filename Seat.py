# @class Seat
# @brief Represents a cinema seat with an ID, availability status, and an associated user if occupied.
class Seat:

    # @brief Constructor for the Seat class.
    # @param column The column for the seat.
    # @param row The row number for the seat.
    # @param available An optional parameter indicating whether the seat is available or occupied. 
    # By default, it is set to True.
    def __init__(self, column: str, row: int, available: bool = True) -> None:
        self.__available = available
        self.__seatID = f"{column}{row}"
        self.__userID = None

    # @brief A string representation of the seat.
    def __str__(self) -> str:
        return f'{self.__seatID} {str(self.__available)}'
    
    # getter and setter needed
    # @brief Getter for the availability status of the seat.
    @property
    def available(self) -> bool:
        return self.__available
    
    # @brief Getter for the seatID.
    @property
    def seatID(self) -> str:
        return self.__seatID
    
    # @brief Getter for the associated user ID, if any.
    @property
    def userID(self) -> str:
        return self.__userID

    # @brief Setter for the availability status of the seat.
    @available.setter
    def available(self, availability: bool):
        self.__available = availability

    # @brief Setter for associating a user ID with the seat.
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID
    
