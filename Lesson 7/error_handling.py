try:
    result=10/0
except ZeroDivisionError:
    print("Error,you tried to divide by 0")

text = "this is not a number"
try:
    text_to_int=int(text)
except Exception as e:
    print("This is a error" , e)

    try:
        result = 10/2
    except ZeroDivisionError:
        print("Error,you tried to divide by 0")
    else:
        print("Divison succesfull.Result", result)