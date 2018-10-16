#Виводить перші n рядків з фалу
def WriteLines(n):
    f = open("a.txt", 'r')
    for index, line in enumerate(f):
        if index >= n:
            break
        print (line)
    f.close()

# зчитує з файлу a та записує парні рядки у Верхньому регістрі в файл b1, а непарні в нижньому регістрі в файл b2
def separ():
    f = open("a.txt", 'r')
    wparni = open('b1.txt', 'w')
    wneparni = open('b2.txt', 'w')
    for index, line in enumerate(f):
        if index % 2 == 0:
            #print(index)
            #print(line)
            wparni.write(line.upper())
        else:
            #print(line)
            wneparni.write(line.lower())
    wparni.close()
    wneparni.close()
    f.close()


a = int(input("Enter number: "))
WriteLines(a)

separ()

