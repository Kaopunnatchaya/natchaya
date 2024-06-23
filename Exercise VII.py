#รายการของเลข 1-20
numbers = list(range(1, 21))
odd_numbers = []
even_numbers = []
for number in numbers:
    if number % 2 == 0:  # ตรวจสอบว่าเป็นเลขคู่หรือไม่
        even_numbers.append(number)  
    else:
        odd_numbers.append(number)  

print("เลขคี่:", odd_numbers)
print("เลขคู่:", even_numbers)
#นางสาวณัฐชยา บุนนาค 6749010008