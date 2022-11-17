# y = lambda a: a ** 2
# x = [
#     y(i) for i in range(10)
# ]
# print( x )

# x = [i for i in range(20) if i % 2 == 0 ]
# print( x )

# x = ['Hi' if i % 2 == 0 else 'bye' for i in range(20)]
# print( x )

a, b = map(int, input('input two numbers').split())
spisak_1 = [i ** 3 for i in range(a, b + 1)]
spisak_2 = [j ** 2 for j in range(a, b + 1)]

print(spisak_1, ' | ', spisak_2)
