def normalize_integer(integer: int | float) -> float:
    minimum = 0
    maximum = 100

    return (integer - min(integer, minimum)) / (max(integer, maximum) - min(integer, minimum))



NUMBER = 74
NUMBER2 = 150
NUMBER3 = -45
NUMBER4 = 50


print(
    normalize_integer(NUMBER),
    normalize_integer(NUMBER2),
    normalize_integer(NUMBER3),
    normalize_integer(NUMBER4)
)