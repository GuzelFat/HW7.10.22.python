# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
print ("Введите номер четверти от 1 до 4: ")
h=int(input())
if h==1:
    print ("Диапазон 1 четверти x>0 и у>0")
if h==4:
    print ("Диапазон точек 4 четверти х>0 и у<0")
if h==2:
    print("Диапазон  точек 2 четверти x<0 и у>0")
if h==3:
    print("Диапазон точек 3 четверти x<0 и у<0") 
if h<1 or h>4:
    print("Такой четверти не существует")    
         


