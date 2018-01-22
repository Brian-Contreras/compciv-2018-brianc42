def fob(max):
    for num in range(1, max + 1):
        print(str(num), end='')
        if num % 15 is 0:
            print(" FizzBuzz")
        elif num % 3 is 0:
            print(" Fizz")
        elif num % 5 is 0:
            print(" Buzz")
        else:
            print("")