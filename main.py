# name = 'ABHISHEK'
# for i in name:
#     print(i)
#     if(i=="K"):
#         print("Kartikey is present")

# colors = ["Red","Green","Blue","Yellow","Black","White"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
# i= int(input("Enter a number: "))
# while(i<=100):
#     i= int(input("Enter a number: "))
#     print(i)
# print("You have enteres a number less than or eqaul to 100")
   

# for i in range(1,12):
#     if(i==5):
#         continue
#         print("Skip...")
#     print("2 X",i,"=",2*(i+1))
#     if(i==10):
#         break
# print("End...")

# Function:

def calc_gmean(a,b):

    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    else:
        print(b,"is greatern than", a)

a = 5
b=10
calc_gmean(a,b)
isGreater(a,b)

c=5
d=6
calc_gmean(c,d)
isGreater(c,d)
    
   