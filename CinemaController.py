from Coupon import Coupon
from Hall import Hall
from Movie import Movie
from Screening import Screening
from Seat import Seat
from Ticket import Ticket
from User import Customer, Admin, Staff

from decimal import Decimal
from datetime import date, datetime

class Cinema:
    def __init__(self) -> None:
        self.allCustomer = []
        self.allStaff = []
        self.allAdmin = []
        self.allHall = [Hall(1, 120), Hall(2, 90), Hall(3, 110), Hall(4, 80)]
        self.allMovie = []
        self.allScreening = []

    def browseAllMovie(self) -> list:
        if self.allMovie == []:
            return self.allMovie
        else:
            return self.allMovie.sort(key = lambda movie: movie.releaseDate)
    
    # Handle all search except date
    def searchMovieByStr(self, searching: str) -> list:
        result = []
        for i in self.allMovie:
            if searching in i.movieName or searching in i.lang or searching in i.genre:
                result.append(i)
        return result
    
    # Handle date search
    def searchMovieByDateAfter(self, searching: date) -> list:
        result = []
        for i in self.allMovie:
            if i.releaseDate > searching :
                result.append(i)
        if result == []:
            return result
        else:
            return result.sort(key = lambda movie: movie.releaseDate)
        
    def movieDetail(self, movie: Movie) -> str:
        if movie in self.allMovie:
            return f'Title: {movie.movieName}\nLanguage: {movie.lang}\nGenre: {movie.genre}\nDate of Release: {movie.releaseDate}\nDuration: {movie.duration}'
        else:
            return f'Movie not found!'
    
    def movieSchedule(self, movie: Movie) -> list:
        result = []
        for i in self.allScreening:
            if i.movieID == movie.movieID:
                result.append(i)

        if result == []:
            return result
        else:
            return result.sort(key = lambda screening: screening.dateT, reverse = True)
        
    def checkSeatAvailability(self,screening: Screening) -> list:
        return screening.hallSeat
        
    def makeBooking(self, screening: Screening, user: Customer, seatID: str, paymentType: str, price: Decimal, coupon=None) -> str:
        # create the ticket + put it in user's list + mark unavailable in screening

        newTicket = Ticket(user.userID, Screening.screeningID, datetime.now, seatID, paymentType, price)
        if coupon != None:
            if coupon in user.coupon:
                user.removeCoupon(coupon)
        
        user.addTicket(newTicket)
        screening.markSeatFalse(seatID)
        msg = f'You have successfully purchased a ticket! No. {newTicket.ticketID}'
        user.userMsgAdd(msg)
        return msg

    def removeTicket(self, user: Customer, ticket: Ticket) -> str:
        for i in user.coupon:
            if i == ticket:
                user.removeTicket(ticket)
                break
        
        msg = f'You have successfully cancelled a ticket!'
        user.userMsgAdd(msg)
        return msg

    def addMovie(self, name: str, langauge: str, genre: str, releaseDate: date, duration: int) -> str:
        newMovie = Movie(name, langauge, genre, releaseDate, duration)
        self.allMovie.append(newMovie)
        msg = f'You have successfully added a movie!'
        return msg
    
    def addScreening(self, movieID: int, dateT: datetime, hallID: int, hallSeat: list) -> str:
        # validate datetime conflicts, generate seats

