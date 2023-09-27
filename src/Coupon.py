from datetime import date


class Coupon:
    """!Represents a discount coupon with an associated user ID, expiration date, and discount value."""
    
    nextID = 1000000

    def __init__(self, userID: int, exp: date, discount: int, valid=True) -> None:
        """! Constructor for the Coupon class.
        @param userID The ID of the user to whom the coupon belongs.
        @param exp The expiration date of the coupon.
        @param discount The discount percentage represented by the coupon.
        @param valid An optional parameter indicating whether the coupon is valid or not. By default, it is set to True."""
        self.__userID = userID
        self.__expireDate = exp
        self.__discount = discount
        self.__valid = valid

        self.__couponID = Coupon.nextID
        Coupon.nextID += 1

    
    def __str__(self) -> str:
        """!A string representation of the coupon.""" 
        return f'{str(self.__userID)} {self.__expireDate.strftime("%m-%d-%Y")} {self.__discount}'
    
    # getter and setter needed
    
    @property
    def userID(self) -> int:
        """!Getter for the userID."""
        return self.__userID
    
    @property
    def expireDate(self) -> date:
        """!Getter for expireDate."""
        return self.__expireDate
    
    @property
    def discount(self) -> int:
        """!Getter for discount."""
        return self.__discount
    
    @property
    def valid(self) -> bool:
        """!Getter for valid."""
        return self.__valid
    
    @property
    def couponID(self) -> bool:
        """!Getter for couponID."""
        return self.__couponID
    
    @valid.setter
    def valid(self, status: bool) -> None:
        """!Setter for couponID."""
        self.__valid = status
