x = 1
warunek = True
while warunek:
    print(x)
    while x >= 5 and x%5==0:
        print("duża liczba!")
        break
        pass
    x+=1
    if x > 25:
        break
    pass
