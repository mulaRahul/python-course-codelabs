is_negative = lambda num: num < 0
is_even = lambda num: num%2 == 0

def is_prime(num):
    if is_even(num) and num == 2:
        return False
        
    for x in range(3, num, 2):
        if num%x == 0:
            return False

    return True
    

# tests
print(f"{is_negative(-3) = }")
print(f"{is_even(9) = }")
print(f"{is_prime(17) = }")
