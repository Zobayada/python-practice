# ------------------- Try Exception --------------
def divide(x,y):
    try:
        result = x // y
        print("Ans is: " , result)
    except:
        print("Sorry ")
divide(6,0)  

# ------------------- Example --------------------
def summation(a,b):
    try:
        c = ((a+b)*(a-b))
        print(c)
    except:
        print("Result is Wrong ")

summation(5,2)