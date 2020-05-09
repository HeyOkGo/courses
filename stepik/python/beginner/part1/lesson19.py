list = list(range(1, 401))
for n in list:
    if n % 10 == 1 and n != 11 and n != 111 and n != 211 and n != 311 and n != 411 and n != 511 and n != 611 and n != 711 and n != 811 and n != 911:
        print(n, "программист")
    elif n == 0 or n % 10 == 0 or 19 >= n >= 5 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or (n % 10 == 1 and n >= 111) or n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
        print(n, "программистов")
    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print(n, "программиста")