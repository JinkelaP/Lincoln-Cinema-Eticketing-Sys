from Coupon import Coupon
from Hall import Hall
from Movie import Movie
from Screening import Screening
from Seat import Seat
from Ticket import Ticket
from User import Customer, Admin, Staff

from decimal import Decimal
from datetime import date, datetime, timedelta

# @class Cinema
# @brief The controller of the cinema management sys.
class Cinema:

    # @brief Constructor for the controller.

    def __init__(self) -> None:
        self.allCustomer = []
        self.allStaff = []
        self.allAdmin = []
        self.allHall = [Hall(1, 120), Hall(2, 90), Hall(3, 110), Hall(4, 80)]
        self.allMovie = []
        self.allScreening = []
        self.loggedin = None
        self.loggedUser = None

    # @brief login function for the system. Any reasons of failed login will return the same msg.
    # @param userName the username.
    # @param psw the password.
    # @param userType the type of user.
    def login(self, userName: str, psw: str, userType: int) -> str:
        msg = 'Incorrect username or password!'
        if userType == 3:
            for i in self.allCustomer:
                if i.username == userName:
                    if i.userPassword == psw:
                        self.loggedin = 3
                        self.loggedUser = i.userID
                        return f'Welcome back, {i.username}!'
            else:
                return msg
        elif userType == 2:
            for i in self.allStaff:
                if i.username == userName:
                    if i.userPassword == psw:
                        self.loggedin = 2
                        self.loggedUser = i.userID
                        return f'Welcome back, {i.username}!'
            else:
                return msg
        else:        
            for i in self.allAdmin:
                if i.username == userName:
                    if i.userPassword == psw:
                        self.loggedin = 1
                        self.loggedUser = i.userID
                        return f'Welcome back, {i.username}!'
            else:
                return msg

    
    # @brief register function for the system. Can only register customer. No conficts allowed in username.
    # @param userName the username.
    # @param psw the password.
    def register(self, userName: str, psw: str) -> str:
        for i in self.allCustomer:
            if i.username == userName:
                return 'Registration failed. The username has been registered.'
        newCustomer = Customer(userName, psw)
        self.allCustomer.append(newCustomer)
        self.login(userName,psw)

        return 'You have registered and loggedin!'
            
    # @brief browse all movies in the list.
    def browseAllMovie(self) -> list:
        if self.allMovie == []:
            return self.allMovie
        else:
            return self.allMovie.sort(key = lambda movie: movie.releaseDate)
    
    # @brief Handle all search except date
    # @param searching the keyword user is searching
    def searchMovieByStr(self, searching: str) -> list:
        result = []
        for i in self.allMovie:
            if searching in i.movieName or searching in i.lang or searching in i.genre:
                result.append(i)
        return result
    
    # @brief Handle date search
    # @param searching the date user is searching
    def searchMovieByDateAfter(self, searching: date) -> list:
        result = []
        for i in self.allMovie:
            if i.releaseDate > searching :
                result.append(i)
        if result == []:
            return result
        else:
            return result.sort(key = lambda movie: movie.releaseDate)
    
    # @brief Show the movie detail
    # @param movie the movie object user chosed
    def movieDetail(self, movie: Movie) -> str:
        if movie in self.allMovie:
            return f'Title: {movie.movieName}\nLanguage: {movie.lang}\nGenre: {movie.genre}\nDate of Release: {movie.releaseDate}\nDuration: {movie.duration}'
        else:
            return f'Movie not found!'
    
    # @brief Show the movie screening
    # @param movie the movie object user chosed
    def movieSchedule(self, movie: Movie) -> list:
        result = []
        for i in self.allScreening:
            if i.movieID == movie.movieID:
                result.append(i)

        if result == []:
            return result
        else:
            return result.sort(key = lambda screening: screening.dateT, reverse = True)
    
    # @brief Show all seats in the screening
    # @param screening the screening object user chosed
    def checkSeatAvailability(self,screening: Screening) -> list:
        return screening.hallSeat

    # @brief Make a booking, creating the ticket
    # @param screening the screening user chosed
    # @param user the customer
    # @param seatID the seat customer chosed
    # @param paymentType could be cash or card
    # @param price could apply coupon
    def makeBooking(self, screening: Screening, user: Customer, seatID: str, paymentType: str, price: Decimal, coupon=None) -> str:
        # create the ticket + put it in user's list + mark unavailable in screening

        if coupon:
            price = price * coupon.discount * 0.01
            user.removeCoupon(coupon)

        newTicket = Ticket(user.userID, Screening.screeningID, datetime.now, seatID, paymentType, price)
        
        user.addTicket(newTicket)
        screening.markSeatFalse(seatID, user.userID)
        msg = f'You have successfully purchased a ticket! No. {newTicket.ticketID}'
        user.userMsgAdd(msg)
        return msg

    # @brief deactivate a ticket
    # @param user the customer
    # @param ticket the ticket
    def removeTicket(self, user: Customer, ticket: Ticket) -> str:
        for i in user.coupon:
            if i == ticket:
                user.removeTicket(ticket)
                break
        
        msg = f'You have successfully cancelled a ticket!'
        user.userMsgAdd(msg)
        return msg

    # @brief add a movie to the list
    # @param name The name of the movie.
    # @param langauge The language of the movie.
    # @param genre The genre of the movie (e.g., action, drama).
    # @param releaseDate The official release date of the movie.
    # @param duration The duration of the movie in minutes.
    def addMovie(self, name: str, langauge: str, genre: str, releaseDate: date, duration: int) -> str:
        newMovie = Movie(name, langauge, genre, releaseDate, duration)
        self.allMovie.append(newMovie)
        msg = f'You have successfully added a movie!'
        return msg
    
    # @brief create seats in the screening hall
    def hallSeatCreate(hall: Hall) -> list:
        maxRow = 15
        nowRow = 1
        nowCol = 'A'

        result = []
        for i in range(hall.hallCapacity):
            if nowRow <= maxRow:
                result.append(Seat(nowCol, nowRow))
            else:
                nowRow = 1
                nowCol = chr(ord(nowCol) + 1)
                result.append(Seat(nowCol, nowRow))
            nowRow +=1
        
        return result

    # @brief add a movie screening
    # @param movie the movie
    # @param dateT the start datetime
    # @param hall the hall
    def addScreening(self, movie: Movie, dateT: datetime, hall: Hall) -> str:
        # validate datetime conflicts, generate seats
        datetEndPlus = ((movie.duration / 30) + 1) * 30
        dateTEnd = dateT + timedelta(minutes=datetEndPlus)
        for i in self.allScreening:
            if dateT < i.dateTEnd and dateTEnd > i.dateT:
                if i.hallID == hall.hallID:
                    return 'Creat screening failed. Time Conflicts detected.'
        else:
            hallSeat = self.hallSeatCreate(hall)
            newScreening = Screening(movie.movieID, dateT, dateTEnd, hall.hallID, hallSeat)
            return 'Creat screening success.'
    
    # @brief remove a movie, including screenings
    # @param movie the movie
    def removeMovie(self, movie: Movie) -> str:
        # remove movie + deactivate screenings
        movieID = movie.movieID
        if movie in self.allMovie:
            self.allMovie.remove(movie)
        
        for i in self.allScreening:
            if i.movieID == movieID:
                msg = self.removeScreening(i)
        
        return 'Movie removed. Screenings cancelled (if available).'
    
    # @brief remove a screening
    # @param screening the screening
    def removeScreening(self, screening: Screening) -> str:
        for i in self.allScreening:
            if i == screening:
                i.valid = False
                for a in i.hallSeat:
                    if type(a.userID) is int:
                        for user in self.allCustomer:
                            if user.userID == a.userID:
                                user.userMsgAdd(f'The screening your booked on {screening.dateT.strftime("%d-%m-%Y, %H:%M")} has been cancelled.')
                                for ticket in user.ticket:
                                    if ticket.screeningID == screening.screeningID:
                                        ticket.valid = False

        return 'Screening cancelled. Customers has been notified.'
