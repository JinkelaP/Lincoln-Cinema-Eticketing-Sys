
class Hall:
    """! Hall
@brief This class represents a hall with its unique ID and capacity.
The hall contains attributes specifying its ID and how many people it can accommodate."""

    
    def __init__(self, id: int, capacity: int) -> None:
        """! Constructor for the Hall class.
    @param id The unique ID of the hall.
    @param capacity The maximum number of people the hall can accommodate."""
        self.__hallID = id
        self.__hallCapacity = capacity

    
    def __str__(self) -> str:
        """!@brief A string representation of the hall."""
        return f'Hall {self.__hallID}. Max {self.__hallCapacity} people.'
    
    # getter and setter needed
    
    @property
    def hallID(self) -> int:
        """!@brief Getter for hallID."""
        return self.__hallID


    @property
    def hallCapacity(self) -> int:
        """!@brief Getter for the hallCapacity."""
        return self.__hallCapacity

