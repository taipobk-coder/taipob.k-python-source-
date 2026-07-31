#รับชื่อจริง (หรือข้อความ) จากผู้ใช้
#นับจำนวนสระทั้งหมดในข้อความว่ามีกี่ตัว
#ตัวอย่างหน้าจอ
#What is your name? : 
#your text have 4 vowels.
"""text = input("Enter your name or text: ")
vowel_count = 0
for char in text:
	if char.lower() in "aeiou":
		vowel_count += 1
print(f"Your text has {vowel_count} vowels.")
"""

name = input("what is your name ?:")
vowel = list(name)
count = 0
for vowel in name:
	if vowel == 'a' or vowel == 'A':
		count = count + 1
    elif vowel == 'e' or vowel == 'E':
        count = count + 1
	elif vowel == 'i' or vowel == 'I':
            count = count + 1
	elif vowel == 'o' or vowel == 'O':
            count = count + 1
	elif vowel == 'u' or vowel == 'U':
            count = count + 1	
print(f"your vowel is:{count}")