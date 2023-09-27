# @class Hall
# @brief This class represents a hall with its unique ID and capacity.
# The hall contains attributes specifying its ID and how many people it can accommodate.
class Hall:

    # @brief Constructor for the Hall class.
    # @param id The unique ID of the hall.
    # @param capacity The maximum number of people the hall can accommodate.
    def __init__(self, id: int, capacity: int) -> None:
        self.__hallID = id
        self.__hallCapacity = capacity

    # @brief A string representation of the hall.
    def __str__(self) -> str:
        return f'Hall {self.__hallID}. Max {self.__hallCapacity} people.'
    
    # getter and setter needed
    # @brief Getter for hallID.
    @property
    def hallID(self) -> int:
        return self.__hallID

    # @brief Getter for the hallCapacity.
    @property
    def hallCapacity(self) -> int:
        return self.__hallCapacity

