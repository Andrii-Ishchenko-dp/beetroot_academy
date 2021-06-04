import math

def make_operation(a,*args):
    end=args[0]
    arg=1
    if a == '+':
        return sum(args)
    elif a == '-':
        while arg < len(args):
            end-=args[arg]
            arg+=1
        return end
    elif a == '*':
        for arg in range(args[-1]):
            end*=args[arg]
        return end

print(make_operation('-',5,5,-10,-20))

