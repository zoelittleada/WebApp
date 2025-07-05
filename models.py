# models.py
from datetime import datetime
from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """
    Loads a user from the database given their ID.
    Required by Flask-Login to manage user sessions.
    """
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    User model for authentication and job ownership.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    # Relationship to Job model: a user can have many jobs
    jobs = db.relationship('Job', backref='author', lazy=True)

    def set_password(self, password):
        """
        Hashes the provided password and stores it.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks if the provided password matches the stored hash.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        String representation of the User object.
        """
        return f"User('{self.username}', '{self.email}')"

class Job(db.Model):
    """
    Job model to store details about various jobs (deliveries, engineering jobs).
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    # Foreign key to link job to a user (the author)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
        String representation of the Job object.
        """
        return f"Job('{self.title}', '{self.date_posted}', 'Completed: {self.is_completed}')"

