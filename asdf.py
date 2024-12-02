def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

gen_1 = my_generator(5)
print(
    next(gen_1) + next(gen_1) + next(gen_1) + list(gen_1)[0] + list(gen_1)[1]
)