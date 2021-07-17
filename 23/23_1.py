from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    if exp<0:
        return TypeError
    while exp>0:
        x*=x
        exp-=1
    return to_power(x,exp)
try:
    y = to_power(3,2)
    print(y)
except TypeError as msgg:
    print('Степерь должна быть больше 0')
