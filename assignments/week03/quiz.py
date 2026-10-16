# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("enter age:"))
if 0 <= age <= 12 :
    print("child") 
elif 13<= age <=19:
    print("teen")
elif 20 <= age <= 59:
    print("adult")
elif age >=60:
    print("senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if choice ==1:
            print("(balance)")
        elif choice ==2:
            
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
