# import os
# import random
# import shutil
# from barcode import EAN13
# from barcode.writer import ImageWriter

# contador = 2

# codBar ='780'
# for i in range (0,7):
#     print(random.randint(0,7))
#     codBar += str(random.randint(0,9))

# print(codBar)


# def eanCheck(codBar):
#     checksum = 0
#     for i, digit in enumerate(reversed(codBar)):
#         checksum += int(digit) * 3 if (i % 2 == 0) else int(digit)
#     temp2 = (10 - (checksum % 10)) % 10
#     return temp2

# codBar += str(eanCheck(codBar))

# print(int(codBar))


# codBar += str(eanCheck(codBar))

# CodBarra = EAN13(codBar, writer=ImageWriter())
# CodBarra.save("code3")


# src_path = "C:\REWORK\\" + "code"+ str(contador) + ".png"
# dst_path = "C:\REWORK\crud\static\img\\"


# if os.path.isfile(src_path):
#     shutil.move(src_path, dst_path)


import math


rut = '11442458'

serie = 2
suma = 0

for i in reversed(rut):
    suma += int(i)*serie
    if serie == 7:
        serie = 1
    serie += 1
dvchk = 11 - (suma - math.trunc(suma/11)*11)

if dvchk == 11:
    dvchk = 0
elif dvchk == 10:
    dvchk = 'k'

print(dvchk)