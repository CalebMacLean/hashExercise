from models import db, User, Feedback
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    User.query.delete()

    walsh = User.register(username="Walsh", password="baby", email="baby@email.com", first_name="Liz", last_name="Walsh")
    caleb = User.register(username="Caleb", password="baby", email="caleb@email.com", first_name="Caleb", last_name="MacLean")
    lance = User.register(username="Fraud", password="baby", email="loser@email.com", first_name="Lance", last_name="Armstrong")

    db.session.add_all([walsh, caleb, lance])
    db.session.commit()

    Feedback.query.delete()

    one = Feedback(title="First Post", content="This is feedback, right?", username="Walsh")
    two = Feedback(title="Cranberry", content="Not enough cranberries", username="Walsh")
    three = Feedback(title="Is My Name Caleb", content="I don't see my name", username="Caleb")

    db.session.add_all([one, two, three])
    db.session.commit()
