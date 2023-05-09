# exercise_12
def find_numbers(s, p):
    for x in range(1, s+1):
        y = s - x
        if x * y == p:
            return (x, y)
    return None
