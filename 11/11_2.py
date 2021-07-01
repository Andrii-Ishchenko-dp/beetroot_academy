#Implement a class Mathematician which is a helper class for doing math operations on lists

#The class doesn't take any attributes and only has methods:

#square_nums (takes a list of integers and returns the list of squares)
#remove_positives (takes a list of integers and returns it without positive numbers
#filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician():
    def __init__(self):
        pass
    def square_nums(self,x):
        y=[]
        for t in x:
            y.append(t*t)
        return y
    def remove_positives(self, x):
        y=[]
        for t in x:
            if t%2!=0:
                y.append(t)
        return y
    def filter_leaps(self,x):
        y = []
        for t in x:
            if t % 4 != 0 or (t % 100 == 0 and t % 400 != 0):
                continue
            else:
                y.append(t)
        return y


x=Mathematician()
print(x.filter_leaps([2001, 1884, 1995, 2003, 2020]))
