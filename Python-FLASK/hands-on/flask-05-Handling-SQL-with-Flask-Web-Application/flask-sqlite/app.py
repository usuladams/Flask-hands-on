from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(80))
    date_added = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html",users=users)

@app.route("/add",methods=["GET","POST"])
def adduser():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        
        if request.form['submit_button'] == 'add-button':
            newuser = User(username=username, email=email,password=password)
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for("index"))
        
        elif request.form['submit_button'] == 'find-button':
            finduser = User.query.filter_by(username=username).first()
            return render_template("index.html",finduser=finduser)

@app.route("/delete/<string:id>")
def deleteuser(id):
    
    deleteuser = User.query.filter_by(id=id).first()
    db.session.delete(deleteuser)
    db.session.commit()
    return redirect(url_for("index"))

        
    

if __name__ == "__main__":
    app.run(debug=True,port=2000)
    #app.run(host='0.0.0.0', port=80)