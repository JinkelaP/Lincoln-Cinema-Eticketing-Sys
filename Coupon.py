from datetime import date

class Coupon:
    nextID = 1000000
    def __init__(self, userID: int, exp: date, discount: int, valid=True) -> None:
        self.__userID = userID
        self.__expireDate = exp
        self.__discount = discount
        self.__valid = valid

        self.__couponID = Coupon.nextID
        Coupon.nextID += 1

    def __str__(self) -> str:
        return f'{str(self.__userID)} {self.__expireDate.strftime("%m-%d-%Y")} {self.__discount}'
    
    # getter and setter needed
    @property
    def userID(self) -> int:
        return self.__userID
    
    @property
    def expireDate(self) -> date:
        return self.__expireDate
    
    @property
    def discount(self) -> int:
        return self.__discount
    
    @property
    def seat(self) -> str:
        return self.__seat
    
    @property
    def valid(self) -> bool:
        return self.__valid
    
    @valid.setter
    def validSet(self, status: bool) -> None:
        self.__valid = status
