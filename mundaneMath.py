def sum_even(a, b):
    count = 0
    for i in range(a, b, 1):
        if(i % 2 == 0):
            count += i
    return count
