my_list = [7, 5, 3, 3, 2]
for t in range(10):
    enter_number = int(input('Введите новый элемент рейтинга: '))
    abs = False
    for i in range(len(my_list)):
        if my_list[i] < enter_number:
            my_list.insert(i, enter_number)
            abs = True
            break
    if not abs:
        my_list.append(enter_number)
    print(my_list)
