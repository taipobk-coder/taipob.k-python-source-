print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
n1=float(input("enter height:"))
n2=float(input("enter weight:"))

#cal

bmi = n2 / (n1 ** 2)

#output

print("total_bmi:",bmi)