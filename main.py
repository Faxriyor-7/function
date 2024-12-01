# Function


# ...
# Exercise 1
# num = int(input("Enter the number :: "))
# a = int(input("Enter the A number :: "))
# b = int(input("Enter the B number :: "))
# c = int(input("Enter the C number :: "))
# d = float(input("Enter the D number :: "))
# e = float(input("Enter the E number :: "))
#
#
# def powerA3(main, numb, numb2, numb3, numb4, numb5):
#     print(main**3, numb ** 3, numb2**3, numb3**3, numb4**3, numb5**3)
#

# powerA3(num, a, b, c, d, e)



# ...
# Exercise 2
# numb = int(input("Enter the number ::: "))
#
# a = int(input("Enter the A nummber ::: "))
# b = int(input("Enter the B nummber ::: "))
# c = int(input("Enter the C nummber ::: "))
#
# def powerA234(main, num, num1, num2):
#     print(main**2, main**3, main **4, num**2, num**3, num**4,num1**2, num1**3, num1**4, num2**2, num2**3, num2**4, sep="\n")
#
# powerA234(numb, a, b, c)



# ...
# Exercise 3
# a = int(input("Enter the A number ::: "))
# b = int(input("Enter the B number ::: "))
# c = int(input("Enter the C number ::: "))
# d = int(input("Enter the D number ::: "))
#
# def mean(a1, b1, c1, d1):
#     print(f"A va B sonlarining o'rta arifmetigi : {(a1 + b1) / 2}")
#     print(f"C va D sonlarining o'rta arifmetigi : {(c1 + d1) / 2}")
#     print(f"A va B sonlarining Geometrik arifmetigi : {(a1 * b1) / 2}")
#     print(f"C va D sonlarining Geometrik arifmetigi : {(c1 * d1) / 2}")
#
# mean(a,b,c,d)


# ...
# Exercise 4
# import math
#
#
# # Teng tomonli uchburchakning perimetri va yuzasini hisoblovchi funksiya
# def teng_tomonli_uchburchak(a):
#     if a <= 0:
#         return "Tomon uzunligi musbat bo'lishi kerak!"
#
#     # Perimetrni hisoblash
#     perimetr = 3 * a
#
#     # Yuzani hisoblash
#     yuza = (math.sqrt(3) / 4) * (a ** 2)
#
#     return perimetr, yuza
#
#
# # Foydalanuvchidan tomon uzunligini kiritish
# a = float(input("Teng tomonli uchburchakning tomon uzunligini kiriting: "))
#
# # Funksiyani chaqirish va natijalarni chiqarish
# natija = teng_tomonli_uchburchak(a)
#
# if isinstance(natija, tuple):
#     print(f"Teng tomonli uchburchakning perimetri: {natija[0]}")
#     print(f"Teng tomonli uchburchakning yuzasi: {natija[1]:.2f}")
# else:
#     print(natija)
