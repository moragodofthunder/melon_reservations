"""Models for Melon Tasting Reservation Web App"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###----------------------------USER-CLASS---------------------------###
class User(db.Model):
    """User data"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True,
                        nullable= False)
    username = db.Column(db.String(50), unique= True, nullable= False)
    password = db.Column(db.String, nullable= False)

    reservations = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.username}>"

###------------------------RESERVATION-CLASS-------------------------###
class Reservation(db.Model):
    """Reservation data"""

    __tablename__ = "reservations"   

    res_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True,
                        nullable= False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"),
                        nullable= False)
    res_date = db.Column(db.Date, nullable= False)
    res_time = db.Column(db.Date, nullable= False)

    user = db.relationship("User", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation: res_id={self.res_id} user_id={self.user_id} date ={self.res_date} time={self.res_time}>"