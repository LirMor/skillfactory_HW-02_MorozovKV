# игровое поле
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# количество столбцов игрового поля
field_size = 3

def printing_field():
    ''' Функционал печати поля '''
    print(f"-------")
    for i in range(field_size):
        print(f"|{field[i * 3]}|{field[1 + i * 3]}|{field[2 + i * 3]}|")
        print(f"-------")

def end_game(field):
    ''' Функция проверки завершенности игры '''
    end = False
    # массив победных комбинаций
    combination_end_game = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
        (0, 4, 8), (2, 4, 6)              # диагональные линии
    )
    # перебор победных комбинаций, для выявления победителя
    for position in combination_end_game:
        # если три ячейки совпадает, то сообщает кто 'X' или 'O'
        if (field[position[0]] == field[position[1]] and field[position[1]] == field[position[2]] and field[position[2]] in ('X', 'O')):
            end = field[position[0]]

    return end

def start_game():
    ''' Функция начала игры'''
    # текущим игроком зажается 'X'
    current_player = 'X'
    # номер итерации
    step = 0
    # вызов функции печати игрового поля
    printing_field()

    # игра продолжается до тех пор, пока кто-то не выиграет, не выйдет из игры или пока не закончатся свободные ячейки для 'X' и 'O'
    while (step < 9) and (end_game(field) == False):
        index = input(f'Ходит {current_player}. Введите номер поля (0 - что бы закончить игру):')

        # если введен 0, значит игра окончена
        if index == '0':
            print('До свидания. Ждем вас снова!')
            break

        # если итерации возможна
        if index in field_list:
            index = int(index)

            # если введенная ячейка незанята, туда будет помещен 'X' или 'O', в зависимости от того какой игрок выбирал ячейку
            if not field[index - 1] in ('X', 'O'):
                field[index - 1] = current_player
                # если сейчас ходил игрок 'X', то он заменился игроком 'O', и наоборот
                if (current_player == 'X'):
                    current_player = 'O'
                else:
                    current_player = 'X'

                step += 1
                printing_field()
            else:
                print('Ячейка уже занята. Повторите!')
        else:
            print('Некорректный ввод. Повторите!')

    # если все ячейки заполнены и нет победителя, то игра окончена в ничью, иначе объявляется победитель
    if (step > 8):
        print('Игра окончена. Ничья!')
    elif end_game(field):
        print(f"Выиграл {end_game(field)}")
        # начать новую игру?
        new_game = input("Начать новую игру (Y - Да, любой другой символ - Нет):")
        # если введено Y начинается новая игра, иначе игра закрывается
        if new_game in ('Y', 'y'):
            start_game()
        else:
            print('До свидания. Ждем вас снова!')

print('Добро пожаловать в игру Крестики & Нолики!')

# начало игры
start_game()