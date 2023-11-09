# Imports
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# Configurations
bcrypt = Bcrypt()
db = SQLAlchemy()
# Configuration Functions
def connect_db(app):
    """Connects an application to a database"""
    db.app = app
    db.init_app(app)
# Models
class User(db.Model):
    """User Model"""
    __tablename__ = 'users'
    # Columns
    username = db.Column(db.String(20), primary_key=True,
                                        nullable=False,
                                        unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False,
                                     unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    # Relationships
    feedback = db.relationship("Feedback", 
                               backref="user", 
                               cascade="all, delete",
                               foreign_keys="Feedback.username")
    # Class Methods
    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register user w/ hashed password & return user"""
        # Hash password and convert it into a utf8 string
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        # Create new instance of User with the required attributes and hashed password
        user = cls(username=username, 
                   password=hashed_utf8, 
                   first_name=first_name, 
                   last_name=last_name,
                   email=email)
        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, uname, pwd):
        """Validate that user exists and password is correct, return user if valid, else return False"""
        u = User.query.filter_by(username=uname).first()
        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False


class Feedback(db.Model):
    """User feedback"""
    __tablename__ = 'feedback'
    # Columns
    id = db.Column(db.Integer, primary_key=True,
                               autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.ForeignKey('users.username'))