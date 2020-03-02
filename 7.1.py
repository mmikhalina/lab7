# Дан текст з цифр і малих латинських літер, за яким слідує крапка. Визначити яких
# букв - голосних або приголосних більше в цьому тексті. Результат вивести на екран.
# Міхаліна Мирослав Олексанлрович 122-Д
# 5 варіант


while True:
    a = 'zxcvbnmsdfghjklqwrtp'
    b = 'aeiuoy'
    text = input("Введіть текст: ")
    if text[-1] != ".":
        print("Ви забули крапку")
        continue
    turn = False
    count_a = 0
    count_b = 0
    for i in text:
        if i in a:
            count_a += 1
        if i in b:
            count_b += 1
        if i not in s:
            turn = True
    if turn:
        print("Error")
    if count_a > count_b:
        print("приголосних більше")
    elif count_a < count_b:
        print("голосних більше")
    else:
        print("Однакова кількість")
    if input('Enter') == '':
        continue
    break
