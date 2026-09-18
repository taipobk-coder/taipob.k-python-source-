try:
    n1 = float(input("enter your number1:"))
    n2 = float(input("enter your number2:"))
    ot = (input("enter your operateor(+,-,*,/):"))

    result = 0

        
    if ot == "+":
            result = n1 + n2
    elif ot == "-":
            result = n1 - n2
    elif ot == "*":
            result = n1 * n2
    elif ot == "/":
            result = n1 / n2
    else:
        raise ValueError("only + - * /")
    print(f"{n1} {ot} {n2} = {result}")

except ValueError:
    print("number only!!!")
except ZeroDivisionError:
    print("if 0 you go out!!!")
except Exception:
      print("โห่ไรวะคนไทยเท่านี้ไม่รู้")

finally:
    print("จบครับแยกย้าย")
