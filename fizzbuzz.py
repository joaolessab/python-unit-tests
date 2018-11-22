def is_fizzbuzz(value):
    if (value % 3 == 0):
        resp = "fizz"
    elif (value % 5 == 0):
        resp = "buzz"
    elif (value % 5 == 0 and value % 3 == 0):
        resp = "fizzbuzz"
