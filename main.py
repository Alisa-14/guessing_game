import datetime
import random


def check_num(text):
    while True:
        try:
            return int(input(f"{text}"))
        except:
            print("Нужно вводить числа.")


def num_log_add(num2, text, num_log_record, a):
    now = datetime.datetime.now()
    num_log_record.append(f'[{now}] [User] [Попытка "{str(a + 1)}"] : Введено число - {num2}')
    num_log_record.append(f'[{now}] [System] [INFO] : {text}')


def num_log_write():
    with open("game_log.txt", "a", encoding='utf-8') as out:
        for i in range(len(num_log_record)):
            out.write(str(num_log_record[i]))
            out.write('\n')


if __name__ == '__main__':
    print("Начинаем игру в угадайку.\n"
          "Вам нужно угадать загаданное число в рамках от 1 до 1000.\n"
          "У вас будет 10 попыток и после каждой неудачи подсказка. \n")
    while True:
        num = random.randint(1, 1000)
        now = datetime.datetime.now()
        num_log_record = [f"[{now}] [System] [INFO]: Загадано число - {num}"]
        while True:
            for a in range(10):
                if a != 9:
                    num2 = check_num("Попробуйте угадать число от 1 до 1000: ")
                    if num != num2:
                        if num2 < num:
                            print(f"Загаданное число больше. Попробуй еще раз.\n"
                                  f"Осталось попыток: {str(9 - a)}\n")
                            num_log_add(num2, "Число не угадано.", num_log_record, a)
                        if num2 > num:
                            print(f"Загаданное число меньше. Попробуй еще раз.\n"
                                  f"Осталось попыток: {str(9 - a)}\n")
                            num_log_add(num2, "Число не угадано.", num_log_record, a)
                    else:
                        print(f"!!!!!!!!!!!Вы угадали с {(a + 1)} попытки!!!!!!!!!!!\n")
                        num_log_add(num2, "Число угадано.", num_log_record, a)
                        num_log_record.append(f'_______________________________')
                        num_log_write()
                        break
                if a == 9:
                    num2 = check_num("Попробуйте угадать число от 1 до 1000: ")
                    if num != num2:
                        if num2 < num:
                            print(f"Загаданное число больше. Вы не угадали.\n"
                                  "Ваши попытки закончились\n")
                        if num2 > num:
                            print(f"Загаданное число меньше. Вы не угадали.\n"
                                  "Ваши попытки закончились.\n")
                        num_log_add(num2, "Число не угадано.", num_log_record, a)
                        now = datetime.datetime.now()
                        num_log_record.append(f'[{now}] [System] [INFO]: Попытки закончились. Игрок проиграл.')
                        num_log_record.append(f'_______________________________')
                        num_log_write()
                    else:
                        print(f"!!!!!!!!!!!Вы угадали с {(a + 1)} попытки!!!!!!!!!!!\n")
                        num_log_add(num2, "Число угадано.", num_log_record, a)
                        num_log_record.append(f'_______________________________')
                        num_log_write()
                        break
            while True:
                choice = str(input(f"Начать заново? (Y/N): "))
                if choice in ("Y", "y"):
                    break
                if choice in ("N", "n"):
                    exit()
                else:
                    print("Не верно введена команда!")
