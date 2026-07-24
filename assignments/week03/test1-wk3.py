age = int(input("enter age:"))
if 0 <= age <= 12 :
    print("child") 
elif 13<= age <=19:
    print("teen")
elif 20 <= age <= 59:
    print("adult")
elif age >=60:
    print("senior")