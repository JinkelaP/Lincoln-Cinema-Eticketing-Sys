from datetime import date

# @class Coupon
# @brief Represents a discount coupon with an associated user ID, expiration date, and discount value.
class Coupon:

    # @brief Class variable to generate unique coupon IDs.
    nextID = 1000000

    # @brief Constructor for the Coupon class.
    # @param userID The ID of the user to whom the coupon belongs.
    # @param exp The expiration date of the coupon.
    # @param discount The discount percentage represented by the coupon.
    # @param valid An optional parameter indicating whether the coupon is valid or not. By default, it is set to True.
    def __init__(self, userID: int, exp: date, discount: int, valid=True) -> None:
        self.__userID = userID
        self.__expireDate = exp
        self.__discount = discount
        self.__valid = valid

        self.__couponID = Coupon.nextID
        Coupon.nextID += 1

    # @brief A string representation of the coupon.
    def __str__(self) -> str:
        return f'{str(self.__userID)} {self.__expireDate.strftime("%m-%d-%Y")} {self.__discount}'
    
    # getter and setter needed
    # @brief Getter for the userID.
    @property
    def userID(self) -> int:
        return self.__userID
    
    # @brief Getter for the expireDate.
    @property
    def expireDate(self) -> date:
        return self.__expireDate
    
    # @brief Getter for discount.
    @property
    def discount(self) -> int:
        return self.__discount
    
    # @brief Getter for valid.
    @property
    def valid(self) -> bool:
        return self.__valid
    
    # @brief Setter for the valid status.
    @valid.setter
    def valid(self, status: bool) -> None:
        self.__valid = status
