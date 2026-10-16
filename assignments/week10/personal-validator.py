"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(),isspaces(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
name = input("enter your name: ")
age = int(input("enter your age: "))
phon = input("enter your phon: ")

check_n = False
for char in name:
    if char.isalpha() or char.isspace():
        check_n = True
    else:
        check_n = False 

check_a = False
if 18<= age <= 65:
    check_a = True

check_ph = False
if phon.isdigit() and len(phon) == 10:
    check_ph = True

print("Validation Results:")
if check_n:
    print("name: valid(contains only letters and spaces)")

if check_a:
    print("age: valid({age}year old)")
else:
    print("age invalid")

if check_ph:
    print("phon:valid(10-digit number)")
else:
    print("phon invalid")

print("Formatted Information:")
print(f"name:{name.upper()}")
if 18 <= age <= 30:
    print("Young Adult(18-30)")
elif 31 <= age <= 60:
    print("age group:adult(31-60)")
else:
    print("age group:senior")

print(f"phon:+91-{phon}")