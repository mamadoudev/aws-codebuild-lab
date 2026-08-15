from flask import Flask
from app import additionner

application = Flask(__name__)


@application.route("/")
def home():
    resultat = additionner(2, 3)

    return f"""
    <h1>AWS CI/CD fonctionne !</h1>
    <p>Application déployée avec Elastic Beanstalk.</p>
    <p>2 + 3 = {resultat}</p>
    """


if __name__ == "__main__":
    application.run()