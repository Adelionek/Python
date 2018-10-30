def multiplier_of_(x):
    def multiplier(number):
        return number*x
    return  multiplier


print(multiplier_of_(5)(9))