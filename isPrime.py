# while (True):
#     num=(input('Введите целое число: '))
#     if num.isdigit():
#         delit=0
#         num=int(num)
#         for i in range(2,int(num/2+1)):
#             if num%i==0:
#                 delit+=1
#         if delit==0:
#             print ('Вы ввели простое число')
#         else:
#             print ('Ваше число не является простым')
#         break
#     else:
#         print ('Это не целое число! Попробуйте снова\n')

num=(input('Введите целое число: '))
try:
    delit=0
    num=int(num)
    for i in range(2,int(num/2+1)):
        if num%i==0:
            delit+=1
    if delit==0:
        print ('Вы ввели простое число')
    else:
        print ('Ваше число не является простым')
except ValueError:
    print ('Это не целое число! Попробуйте снова\n')