for a in range(1, 400):
    for b in range(1, 400):
            c = (1000 - a) - b
            if a < b < c:
                if a ** 2 + b ** 2 == c ** 2:
                    print(f"The value of a,b,c are {a},{b},{c}")
                    num=a*b*c
                    print(f"The product of a * b * c is {num}")
