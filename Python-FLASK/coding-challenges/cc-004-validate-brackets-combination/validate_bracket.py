
def isValid(bracket):
    while "()" in bracket or "[]" in bracket or  "{}" in bracket:
        bracket=bracket.replace("()","").replace("[]","").replace("{}","")

    return bracket==""


while(True):

    bracket=input("Enter just the characters (, ), {, }, [, ] : ")
    
    if isValid(bracket):
        print(isValid(bracket))
        break
    else:
        print(isValid(bracket))
        



   
