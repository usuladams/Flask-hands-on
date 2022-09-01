from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

def convert(number):
    ones_roman=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens_roman=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hundreds_roman=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thousands_roman=["","M","MM","MMM"]
    
    if int(number)<10:
        return str(ones_roman[int(number)])
    elif int(number)<100:
        tens=int(number[0])
        ones=int(number[1])
        return str(tens_roman[tens])+str(ones_roman[ones])
    elif int(number)<1000:
        hundreds=int(number[0])
        tens=int(number[1])
        ones=int(number[2])
        return str(hundreds_roman[hundreds])+str(tens_roman[tens])+str(ones_roman[ones])
    else:
        thousands=int(number[0])
        hundreds=int(number[1])
        tens=int(number[2])
        ones=int(number[3])
        return str(thousands_roman[thousands])+str(hundreds_roman[hundreds])+str(tens_roman[tens])+str(ones_roman[ones])



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert",methods=["GET","POST"])
def convert_html():
    if request.method=="POST":
        number1=request.form.get("number1")
        if int(number1)<1 or not number1.isdigit() or int(number1)>3999:
            return render_template("convert.html")
        else:
            return render_template("convert.html",convert=convert(number1),number=number1)
    else:
        return redirect(url_for("index"))

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)