import app
b = app.a
app.dummy_func(10, 243, "-")
from error.app import varaibles



# from app import a, dummy_func
# b = a
# dummy_func(10, 243, "-")


print(b)

def calc():
    var1 = int(input("Enter number 1:"))
    var2 = int(input("Enter number 2:"))
    # k = 5//0
    var3 = addition(var1, var2)
    result = addition(100, 220)
    # print("again", result)
    print("varaible 3 chcek",var3)
    if var3[0][0] > 100:
        return "Success"
    else:
        return "Fail"

try:
 calc()
# except NameError:
#     print("")
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError as err:
    print("error --->>>>>",err)
    def addition(var1, var2):
        result = var1 + var2
        print("result from addition:",result)
        return [result], "succcess"
    calc()




print("func")

print(varaibles)
