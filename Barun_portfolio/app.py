from flask import Flask, render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bxzod%400806@localhost:3306/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    subject = db.Column(db.Text)
    message = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        new_msg = Contact(firstname=firstname, lastname=lastname, email=email, subject=subject, message=message)
        db.session.add(new_msg)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
