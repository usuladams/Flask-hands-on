
phone_book={}
def add(name,phone_number):
    if name in phone_book:
        print("Exists phone number of ", name)
    else:
        phone_book.update({name:phone_number})
        print("Phone number of ", name, " is inserted into the phonebook")
        
        
   
def find(name):
    if name in phone_book:
        print("Phone number of ", name, " is ",phone_book[name])
    else:
        print("Couldn't find phone number of ", name)

def delete(name):
    if name in phone_book:
        del phone_book[name]
        print(name, " is deleted from the phonebook")
    else:
        print("Couldn't find phone number of ", name)
    
while True:
    info = """
    Welcome to the phonebook application
    1. Find phone number
    2. Insert a phone number
    3. Delete a person from the phonebook
    4. Terminate
    Select operation on Phonebook App (1/2/3) : """

    number=input(info)
    if number=="1":
        name=input("Find the phone number of : ")
        find(name)
    
    
    elif number=="2":
        name=input("Insert name of the person : ")
        phone_number=input("Insert phone number of the person : ")
        if not phone_number.isdigit():
            print('Invalid Input Format,cancelling operation...')
        else:
            add(name,phone_number)
   
    elif number=="3":
        name=input("Whom to delete from phonebook : ")
        delete(name)

    elif number=="4":
         print("Exiting Phonebook... Good Bye")
         break
    elif number=="5":
         print(phone_book)
