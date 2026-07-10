"""
print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()
"""

#input

s1 = int(input("enter Seconds:"))

#cal

h1 = s1 // 3600
se1_remain =  s1 % 3600

m1 = se1_remain // 60
se1_remain = m1 * 60

#output

print("min=",m1)
print("sec=",s1)
print("hour=",h1)