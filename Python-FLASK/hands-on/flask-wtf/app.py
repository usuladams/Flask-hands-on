from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY']="my secret"


#create a Form Class
class MyForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    email= StringField("What's Your Email Address")
    submit=SubmitField("Submit")


@app.route("/")


#Create Name Page 
@app.route('/name', methods=['GET', 'POST'])
def name():

    name=None
    email=None
    form = MyForm()
        
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
            
        form.name.data=''
        form.email.data=''
        
    return render_template('name.html',name=name,email=email,form=form)
    


if __name__ == "__main__":
    app.run(debug=True)
    