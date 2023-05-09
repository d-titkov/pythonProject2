# exercise_14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def powers_of_two(n):
    power = 1
    while power <= n:
        print(power)
        power *= 2