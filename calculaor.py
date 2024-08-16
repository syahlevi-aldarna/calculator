# calculator sederhana

print(20*"=" + "\n")
print("kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukan angka 1 = "))
operator = input("operator(+,-,*,/) = ")
angka_2 =  float(input("masukan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasil nya = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasil nya = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasil nya = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasil nya = {hasil}")
else:
    print("masukin yang bener bro!!!, pening nih")


print("horee!!!")