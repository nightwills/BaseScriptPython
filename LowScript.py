Method = input("Что будем делать? Варианты: +,- ")
if Method != "+" and Method != "-":
    print('Такая операция отсутствует')
    exit()
Value1 = float(input("Введите первое число: "))
Value2 = float(input("Введите второе число: "))

if Method == "+":
    summ = Value1 + Value2
elif Method == "-":
    summ = Value1 - Value2
print('Результат: '+str(summ))    
    