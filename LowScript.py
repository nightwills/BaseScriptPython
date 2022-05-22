Method = input("Что будем делать? Варианты: +,- ")
Value1 = float(input("Введите первое число: "))
Value2 = float(input("Введите второе число: "))

if Method == "+":
    summ = Value1 + Value2
elif Method == "-":
    summ = Value1 - Value2
else:
    print('Такая операция отсутствует')
    exit()
print('Результат: '+str(summ))    
    