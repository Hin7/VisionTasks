# Вывод мимнимального значения идущих подряд кадров, для которых сумма расстояний
# между последовательно идущими кадрами превышает порог равный 1000.
# Решение задачи.

# Автор: Хоружий И.Н.
# Дата:  18.01.2022


#порог активного движения
THRESHOLD = 1000


# читаем входные данные из файла input.txt
inFile = open("input.txt", mode = "r")
nKadr = int(inFile.readline())
print(nKadr)
shiftInKadr = [ int(item) for item in inFile.readline().split(" ")]
print(shiftInKadr)
inFile.close()

#создаем копию для работы
summShifts = shiftInKadr[:]
minK=0
searchSize = nKadr
success = False
#запускаем поиск превышения суммы над порогом увеличивая
#на каждом шаге увеличивая количество суммируемых кадров
#и уменьшая область поиска в массиве
#сумму копим в списке summShifts, на каждом шаге добавляя
#кадр номер i+minK
while searchSize and not success:
    #ищем превышение суммы над порогом
    for i in range(0, searchSize):
        #для одного кадра не добавляем ничего 
        if minK : 
            summShifts[i] += shiftInKadr[i + minK]
        #проверяем превышение суммы над порогом
        if summShifts[i] >= THRESHOLD:
            print(minK+1)
            outFile = open("output.txt", mode = "w")        
            outFile.write(str(minK+1))
            outFile.close()
            success = True
            break
    searchSize -= 1
    minK += 1 
            
    
