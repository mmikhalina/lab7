# Міхаліна Мирослав Олексанлрович 122-Д
# Вивести відомості про товари з ціною, що вище середньої. Поля структури:
# Найменування, Кількість, Ціна, Виробник, Дата надходження на склад.
# 5 варіант


while True:

    data = [{'Найменування': 'Шкарпетки', 'Кількість': 50, 'Ціна': 500, 'Виробник': 'Житомир',
             'Дата надхождення на склад': '30/01/20'},
            {'Найменування': 'Шапка', 'Кількість': 100, 'Ціна': 300, 'Виробник': 'Злагода',
             'Дата надхождення на склад': '09/02/20'},
            ]
    output = []
    for i in data:
        average = (i.get('Ціна'))
        if average > 400:
            output.append(i)
    for info in output:
        print(f'{info}')

    if input('Enter') == '':
        continue
    break
