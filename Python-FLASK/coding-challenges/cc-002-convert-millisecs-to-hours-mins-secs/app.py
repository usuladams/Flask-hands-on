from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

def convert(millisecond):
    hour=millisecond//(60*60*1000)
    millisecond_kalan=millisecond%(60*60*1000)
    minute=millisecond_kalan//(60*1000)
    millisecond_kalan=millisecond_kalan%(60*1000)
    second=millisecond_kalan//1000

    h=f'{hour} hour/s' if hour>0 else ''
    m=f'{minute} minute/s' if minute>0 else ''
    s=f'{second} second/s' if second>0 else f'just {millisecond} millisecond/s' if millisecond<1000 else ''
    return h +' '+ m +' '+ s


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert",methods=["GET","POST"])
def convert_html():
    if request.method=="POST":
        number1=request.form.get("number1")
        if number1=='0' or not number1.isdigit():
            return render_template("convert.html")
        else:
            return render_template("convert.html",convert=convert(int(number1)),number=number1)
    else:
        return redirect(url_for("index"))

if __name__=="__main__":
    app.run(debug=True)