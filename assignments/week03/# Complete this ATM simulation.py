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
        if choice =="1":
            print("(balance)",balance)
        elif choice =="2":
            withdraw = float(input("how much: "))
            balance = balance - withdraw
            print("(balance)",balance)
        elif choice =="3":
             deposit = float(input("how much: "))
             balance = balance + deposit
             print("(balance)",balance)
        elif choice =="4":
            break
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")