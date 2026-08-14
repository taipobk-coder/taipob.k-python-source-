"""
#เขียน function ที่สามารถแปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB

โดยใช้ชื่อ function convert_currency(100,"USD")

แสดงผลผ่านทางหน้าจอ
100 THB = 3.3 USD

และทดสอการใช้งาน function ที่ตัวเองเขียนด้วย
"""
def convert_currency(amount, currency):
    if currency == "USD":
        return amount / 32
    elif currency == "THB":
        return amount * 32
    else:
        return None

print(f"100 THB = {convert_currency(100, 'USD')} USD")
print(f"100.
       USD = {convert_currency(100, 'THB')} THB")