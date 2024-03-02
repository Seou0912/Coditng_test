import random


def generate_random_code():
    code = " "
    for _ in range(6):
        code += str(random.randint(0, 45))
        print(generate_random_code())

    return code
