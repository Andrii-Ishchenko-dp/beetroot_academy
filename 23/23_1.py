from typing import Optional
def to_power(x, exp):
    if exp>0:
        if exp==1:
            return x
        else:
            y = to_power(x,exp-1)*x
        return y
    return ValueError('Степень должна быть больше 0')

print(to_power(3,2))
