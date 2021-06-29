def fizz_buzz(max_val, opt):
    for x in range(1, max_val):
        output = ""
        for y in opt:
            if (x % y[0]) == 0:
                output += y[1]#add to output if multiple of the option 
        if output == "":
            output += str(x)#if no match add number to the output
        print(output)

options = [[3,"Fizz"],[5,"Buzz"],[6,"Boop"]]#Array storing what multiples go with each word
fizz_buzz(100, options)
