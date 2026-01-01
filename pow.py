def power(base, exp):
    if exp < 0:
        print("Power should not be negative.")
    elif exp == 0:
        print(base, "^", exp, "= 1")
    else:
        result = 1
        for _ in range(exp):
            result *= base
        print(base, "^", exp, "=", result)

a = int(input("Enter base: "))
b = int(input("Enter power value: "))
power(a, b)