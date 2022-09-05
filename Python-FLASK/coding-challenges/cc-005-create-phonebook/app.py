from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

phone_book={}
def add(name,phone_number):
    if name in phone_book:
        return "Exists phone number of "+name
    else:
        phone_book.update({name:phone_number})
        return "Phone number of "+name+" is inserted into the phonebook"
          
def find(name):
    if name in phone_book:
        return phone_book[name]
    else:
        return "Couldn't find phone number of "+name

def delete(name):
    if name in phone_book:
        del phone_book[name]
        return name+" is deleted from the phonebook"
    else:
        return "Couldn't find phone number of "+name

def show():
    phone_book_item=list(phone_book.items())
    return phone_book_item

def show_num():
   
    phone_book_key=list(phone_book.keys())
    return phone_book_key


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listpage",methods=["GET","POST"])
def list_html():
    if request.method=="POST":
        name=request.form.get("name").strip()
        number=request.form.get("number")

        
        if request.form['submit_button'] == 'add-button':
            if name=="" or number=="":
                return render_template("index.html",info_alert="Please Enter name and phone number...")
            else:
                return render_template("index.html",info_add=add(name,number))
        elif request.form['submit_button'] == 'show-button':
            return render_template("index.html",phone_book_item=show(),phone_book_key=show_num())
        elif request.form['submit_button'] == 'delete-button':
            if name=="":    
                return render_template("index.html",info_alert="Please Enter the name you want to delete...")
            else:
                return render_template("index.html",info_delete=delete(name),name=name)
        elif request.form['submit_button'] == 'find-button':
            if name=="":    
                return render_template("index.html",info_alert="Please Enter the name you want to find...")
            else:    
                return render_template("index.html",info_find=find(name),name=name)
   
   



if __name__=="__main__":
    app.run(debug=True)