for x in range(1,100):
    options = [[3,"Fizz"],[5,"Buzz"],[6,"Boop"]]#Array storing what multiples go with each word
    output=""
    for y in options:
        if (x % y[0]) == 0:
            output += y[1]#if the nuber is a multiple of the option add the linked word to the output
    if output == "":
        output += str(x)
    print(output)
