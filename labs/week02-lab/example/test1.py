
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

#input
r1 = float(input("enter radius:"))

#cal
p1=3.14159 *  r1 ** 2
c1 = 2 * 3.14159 * r1
#output
print("answer area =",c1)
print("cal of this circle:"+ str(c1))
