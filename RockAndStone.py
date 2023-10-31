import random
import sys

win = 0      # Победы
loser = 0    # Поражения
path = 0     # Ничьи

for i in range(1,4):              # 3 попытки
    
    bot = random.randint(1,3)     # Вариант бота
       
    if bot == 1:
        bot = "к"
    elif bot == 2:
        bot = "н"
    elif bot == 3:
        bot = "б"
        
    player = input("Камень(к), ножницы(н), бумага(б): ")         # Вариант игрока
    if player != "к" and player != "н" and player != "б":        # Выход при неверном значении
        sys.exit()
        
    if player == bot:                                            # Сама игра
        print("Ничья!")
        path += 1
    elif player == "к" and bot == "б" or player == "б" and bot == "н" or player == "н" and bot == "к":
        print("Ты проиграл!")
        loser += 1
    elif player == "б" and bot == "к" or player == "н" and bot == "б" or player == "к" and bot == "н":
        print("Ты победил!")
        win += 1

print("Побед: " + str(win) + "\n" +                              # Вывоб результатов
      "Проигрешей: " + str(loser) + "\n" +
      "Ничьи:" + str(path) + "\n")