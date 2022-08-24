from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

def largest(numbers):
    largest_num=numbers[0]
    for i in numbers:
        if largest_num<i:
            largest_num=i
    return largest_num

def lowest(numbers):
    lowest_num=numbers[0]
    for i in numbers:
        if lowest_num>i:
            lowest_num=i
    return lowest_num


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/findpage",methods=["GET","POST"])
def largest_html():
    if request.method=="POST":
        numberss=request.form.get("numbers").split()
        number_get=[]
        for i in numberss:
            try:
                number_get.append(int(i))
            except:
                return render_template("find.html",alert1="Please don't enter (a-z to A-Z) letters...")
               
            

       
    if request.form['submit_button'] == 'largest-button':
        if len(number_get)==0:
            return render_template("find.html",alert1='Please enter one number...')
        elif len(number_get)<2:
            return render_template("find.html",alert1='Please enter more than one number...')
        else:
            return render_template("find.html",thelargest=largest(number_get))
    else:
        if len(number_get)==0:
            return render_template("find.html",alert1='Please enter one number...')
        elif len(number_get)<2:
            return render_template("find.html",alert1='Please enter more than one number...')
        else:
            return render_template("find.html",thelowest=lowest(number_get))


if __name__=="__main__":
    app.run(debug=True)