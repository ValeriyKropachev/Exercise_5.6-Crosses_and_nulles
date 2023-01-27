# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


end_game = 0  # Переменная-условие конца игры
temp1 = int    # Вспомогательная переменная
temp2 = 0     # Вспомогательная переменная
score1 = 0    # Переменная для учета количества ходов участников в процессе игры.
name1 = 'Игрок1'
name2 = 'Игрок2'
game_matrix = ['1', '2', '3',  #Задаем игровое поле
                   '4', '5', '6',
                   '7', '8', '9' ]

def game_field(game_matrix): #Вспомогательная функция для вывода игрового поля
    print(game_matrix[0], '|', game_matrix[1], '|', game_matrix[2])
    print('_', '_', '_', '_', '_')
    print(game_matrix[3], '|', game_matrix[4], '|', game_matrix[5])
    print('_', '_', '_', '_', '_')
    print(game_matrix[6], '|', game_matrix[7], '|', game_matrix[8])

def game_end_checking(game_matrix):
    global end_game
    global name1
    global name2
    if (game_matrix[0] == 'X' and game_matrix[1] == 'X' and game_matrix[2] == 'X') or (game_matrix[3] == 'X' and game_matrix[4] == 'X' and game_matrix[5] == 'X') or (game_matrix[6] == 'X' and game_matrix[7] == 'X' and game_matrix[8] == 'X') or (game_matrix[0] == 'X' and game_matrix[3] == 'X' and game_matrix[6] == 'X') or (game_matrix[1] == 'X' and game_matrix[4] == 'X' and game_matrix[7] == 'X') or (game_matrix[3] == 'X' and game_matrix[5] == 'X' and game_matrix[8] == 'X') or (game_matrix[0] == 'X' and game_matrix[4] == 'X' and game_matrix[8] == 'X') or (game_matrix[2] == 'X' and game_matrix[4] == 'X' and game_matrix[6] == 'X'):
        print("Выиграл игрок ", name1, "!")
        end_game = 1
    elif (game_matrix[0] == '0' and game_matrix[1] == '0' and game_matrix[2] == '0') or (game_matrix[3] == '0' and game_matrix[4] == '0' and game_matrix[5] == '0') or (game_matrix[6] == '0' and game_matrix[7] == '0' and game_matrix[8] == '0') or (game_matrix[0] == '0' and game_matrix[3] == '0' and game_matrix[6] == '0') or (game_matrix[1] == '0' and game_matrix[4] == '0' and game_matrix[7] == '0') or (game_matrix[3] == '0' and game_matrix[5] == '0' and game_matrix[8] == '0') or (game_matrix[0] == '0' and game_matrix[4] == '0' and game_matrix[8] == '0') or (game_matrix[2] == '0' and game_matrix[4] == '0' and game_matrix[6] == '0'):
        print("Выиграл игрок ", name2, "!")
        end_game = 1

def game():
    global end_game
    global temp1
    global temp2
    global score1
    global name1
    global name2
    global game_matrix
    name1 = input("Игрок 1, введите свое имя: ")
    name2 = input("Игрок 2, введите свое имя: ")
    print(name1, "играет X,", name2, "- 0.")
    game_field(game_matrix) #Выводим поле в консоль
    while ((end_game < 1) and (score1 < 9)):
        while temp2 < 1:
            temp1 = input("Введите номер поля, куда вы хотите поставить крестик: ")
            if temp1.isdigit() and int(temp1) > 0 and int(temp1) < 10:
                if game_matrix[int(temp1)-1] != 'X' and game_matrix[int(temp1)-1] != '0':
                    game_matrix[int(temp1)-1] = 'X'
                    temp2 = temp2 + 1
                else:
                    print("Поле уже занято, выберите другое поле.")
            else:
                print("Указан неверный номер поля или символ")
        temp2 = 0
        game_field(game_matrix)
        score1 = score1 + 1
        game_end_checking(game_matrix)
        if (end_game == 0) and (score1 < 9):
            while temp2 < 1:
                temp1 = input("Введите номер поля, куда вы хотите поставить ноль: ")
                if temp1.isdigit() and int(temp1) > 0 and int(temp1) < 10:
                    if game_matrix[int(temp1) - 1] != 'X' and game_matrix[int(temp1) - 1] != '0':
                        game_matrix[int(temp1) - 1] = '0'
                        temp2 = temp2 + 1
                    else:
                        print("Поле уже занято, выберите другое поле.")
                else:
                    print("Указан неверный номер поля или символ")
        elif score1 > 8:
            print("Ничья!")
        temp2 = 0
        game_field(game_matrix)
        score1 = score1 + 1
        game_end_checking(game_matrix)
game()