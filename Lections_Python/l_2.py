colors = ["red", "green", "blue"] #данные
data = open("file.txt", "a") #функция опен - передали аргументы
data.writelines(colors) #произвели запись
data.close() #надо закрыть


exit() #закрыли подключение, т.е. ф-ция не будет работать
path = "file.txt"
data.open(path, "r")
for line in data:
    print(line)
data.close()