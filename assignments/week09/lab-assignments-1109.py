def cul_units(units):
    if units > 200:
        cost = (2.5 * 50) + (3.0 * 50) + (100 * 3.5) + ((units-200) * 4.0) + 25
        print("1-50 u: 120.00 b")
        print("51-100 u: 150.00 b")
        print("101-200 u: 350.00 b")
        print(f"201-{units}u:{(units - 200)}b")
        print("sv_free:25 b")
        print("totol:",cost)

    elif units > 100:
        cost = (2.5 * 50) + (3.0 * 50) + (100 * 3.5) + ((units-200) * 3.5) + 25
        print("1-50 u: 120.00 b")
        print("51-100 u: 150.00 b")
        print(f"101-{units}u:{(units - 100)}b")
        print("sv_free:25 b")
        print("totol:",cost)

    elif units > 50:
        cost = (2.5 * 50) + (3.0 * 50) + (100 * 3.5) + ((units-200) * 3.0) + 25
        print("1-50 u: 120.00 b")
        print(f"51-{units}u:{(units - 50)}b")
        print("sv_free:25 b")
        print("totol:",cost)

    elif units >=0:
        cost = (2.5 * units) + 25
        print(f"1-{units}u:{2.5*units}b")
        print("sv_free:25 b")
        print("totol:",cost)

    else :
        print("not pass!!!")



print("====โปรแกรมคำนวณไฟฟ้า====")
while(True):
    print("1.คำนวณค่าไฟฟ้า")
    print("2.exit")
    choice = input("เลือกครับ :")

    if choice == "1":
        units = float(input("entrt your units:"))
        cul_units(units)
    elif choice == "2":
        break
    else:
        print("ทำใหม่อย่ามาบ้าตุ๋ยดุ้ยวะ")