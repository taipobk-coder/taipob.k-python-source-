#ภาษีขั้นบันได#

def calculate_tax(income):
    net = income
    total_tax = 0.0
    tax_details = []

    # 1. ขั้น 0 - 150,000 (0%)
    tax_details.append("ขั้น 0 - 150,000 ฿ (0%): 0.00 ฿")

    # 2. ขั้น 150,001 - 300,000 (5%)
    if net > 150000:
        taxable = min(net - 150000, 150000)
        step_tax = taxable * 0.05
        total_tax += step_tax
        tax_details.append(f"ขั้น 150,001 - 300,000 ฿ (5%): {step_tax:,.2f} ฿")

    # 3. ขั้น 300,001 - 500,000 (10%)
    if net > 300000:
        taxable = min(net - 300000, 200000)
        step_tax = taxable * 0.10
        total_tax += step_tax
        tax_details.append(f"ขั้น 300,001 - 500,000 ฿ (10%): {step_tax:,.2f} ฿")

    # 4. ขั้น 500,001 - 750,000 (15%)
    if net > 500000:
        taxable = min(net - 500000, 250000)
        step_tax = taxable * 0.15
        total_tax += step_tax
        tax_details.append(f"ขั้น 500,001 - 750,000 ฿ (15%): {step_tax:,.2f} ฿")

    # 5. ขั้น 750,001 - 1,000,000 (20%)
    if net > 750000:
        taxable = min(net - 750000, 250000)
        step_tax = taxable * 0.20
        total_tax += step_tax
        tax_details.append(f"ขั้น 750,001 - 1,000,000 ฿ (20%): {step_tax:,.2f} ฿")

    # 6. ขั้น 1,000,001 - 2,000,000 (25%)
    if net > 1000000:
        taxable = min(net - 1000000, 1000000)
        step_tax = taxable * 0.25
        total_tax += step_tax
        tax_details.append(f"ขั้น 1,000,001 - 2,000,000 ฿ (25%): {step_tax:,.2f} ฿")

    # 7. ขั้น 2,000,001 - 5,000,000 (30%)
    if net > 2000000:
        taxable = min(net - 2000000, 3000000)
        step_tax = taxable * 0.30
        total_tax += step_tax
        tax_details.append(f"ขั้น 2,000,001 - 5,000,000 ฿ (30%): {step_tax:,.2f} ฿")

    # 8. ขั้นมากกว่า 5,000,000 (35%)
    if net > 5000000:
        taxable = net - 5000000
        step_tax = taxable * 0.35
        total_tax += step_tax
        tax_details.append(f"ขั้นมากกว่า 5,000,000 ฿ (35%): {step_tax:,.2f} ฿")

    # คำนวณค่าสรุป
    remaining = income - total_tax
    effective = (total_tax / income * 100) if income > 0 else 0.0

    return {
        "details": tax_details,
        "total_tax": total_tax,
        "remaining": remaining,
        "effective": effective
    }


# --- ส่วน Main ---
input_user = float(input("กรอกเงินได้สุทธิ : "))

result = calculate_tax(input_user)

print("\nรายละเอียดภาษี")
for info in result['details']:
    print(f"{info}")

print("\n")
print(f"ภาษีรวม {result['total_tax']:,.2f} ฿")
print(f"รายได้หลังหักภาษี {result['remaining']:,.2f} ฿")
print(f"Effective Tax Rate {result['effective']:.2f} %")