def fizzbuzz():
    for i in range(1,101):
        print_number = True

        if i%3 == 0:
            print("Fizz")
            print_number = False
        if i%5 == 0:
            print("Buzz")
            print_number = False
        if print_number:
            print(i)
        print()