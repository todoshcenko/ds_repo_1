import math
import numpy as np


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_bisection(number):
    """Округление чередуется чтобы не уйти в бесконечный цикл при 2 числах.
    В противном случае пришлось бы начинать перебор при 2-х числах."""
    round_func = [math.floor, math.ceil]
    low, high = 1, 100
    count = 0
    while True:
        count += 1
        predict = round_func[count % 2]((high + low) / 2)
        if number > predict:
            low = predict
        elif number < predict:
            high = predict
        else:
            return count


score_game(game_core_bisection)
