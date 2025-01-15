def factorial(num):
    if num < 0:
        print("Cant calculate factorial")
        return
    if num <=1:
        print("Factoial is", 1)
        return
    fact = 1
    for i in range(2, num+1):
        fact = fact * i
    print("The factorial is", fact)
    return

factorial(5)
        

