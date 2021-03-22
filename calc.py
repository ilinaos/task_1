try:
    num1=float(input('Введите число: '))
    while True:
        op_num=input('Введите операцию и число через пробел или = для вывода результата: ').split()
        if op_num[0]=='+':
            num1+=float(op_num[1])
        elif op_num[0]=='-':
            num1-=float(op_num[1])
        elif op_num[0]=='*':
            num1*=float(op_num[1])
        elif op_num[0]=='**':
            num1**=float(op_num[1])
        elif op_num[0]=='=':
            print (f'Результат: {num1}')
            break
        elif (op_num[0]=='/' or op_num[0]=='//' or op_num[0]=='%') and op_num[1]=='0':
            print ('На ноль делить нельзя! Попробуйте снова')
        elif op_num[0]=='/':
            num1/=float(op_num[1])
        elif op_num[0]=='//':
            num1//=float(op_num[1])
        elif op_num[0]=='%':
            num1%=float(op_num[1])
        else:
            print ('Что-то пошло не так.\nМожет, вы забыли пробел или неправильно указали операцию?\nМожно использовать операции +, -, *, /, **, //, %')
except ValueError:
    print ('Нужно вводить числа и математические операции')