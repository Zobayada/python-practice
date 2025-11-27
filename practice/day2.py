# Day 2: 
"""
. input()
. Numeric operations
. Strings (slicing, methods)
. Boolean & comparison
. if–else
. Practice Tasks
"""

# input() function diye user theke data neya hoyeche

name = input ("Enter Your Name: ")
print("Welcome, " + name)

age = 20
print(str(age))  

age = int(input("Enter Your Age: ")) # int dewa hoyeche karon input function always string return kore
print("You are", age ,"years old.") # comma use korar karon holo print er moddhe space auto dewa hoye
print ("You are " + str(age) + " years old.") # plus (+) sign use korar karon holo string gula ke jog kra hoyeche

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
print("Hello", name, ",", "you are" , age , "years old.")
print("Hello " + name + ", you are " + str(age) + " years old.")
print(f"Hello {name}, you are {age} years old.") # f string use korar karon holo eta aro shohoje string er moddhe variable gula ke boshate pare
print("Hello {} , you are {} years old.".format(name, age)) # format method use korar karon holo eta o aro shohoje string er moddhe variable gula ke boshate pare
print("Hello {name} , you are {age} years old.".format(name=name, age=age)) # format method er aro ekta way jekhane variable gula ke explicitly bole dewa hoye


# Numeric Operations
7 % 3 = 1 # modulus operator, vagshesh ber kore
10 // 3 = 3 # floor division, vagfol er integer part ber kore
2 ** 5 = 32 # exponentiation, power ber kore
15 / 2 = 7.5 # normal division, float result dey
15 // 2 = 7 

# Strings – (Indexing + Slicing + Methods)
name = "Zobayada Afnan"

#indexing
print(name[0]) # output: Z
print(name[9]) # output: A
print(name[-1]) # output: n
print(name[-4]) # output: f 

#slicing
prnit(name[0:7]) # output: Zobayad