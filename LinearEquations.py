#  File: LinearEquations.py
#  Description: This program will create a class called LinearEquation that will be able to create an object that describes a  linear equation and use different methods to give different functions to that object
#  Student's Name: Arturo Salinas
#  Student's UT EID: ams8964
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 04/05/2020
#  Date Last Modified: 04/07/2020


###########################################################


class LinearEquation():
    

    def __init__(self, m, b):
        self.m = m
        self.b = b
        self.LinearEquation = str(self.m) + 'x +'  + str(self.b)
        
        
        # create LinearEquation object
    def showEq(self):
        self.LinearEquation
        # if y-interecept is negative, have the b term print a negative sign
        if self.m > 0 and self.b < 0:
            return str(self.m) + 'x - ' + str(self.b * -1) 
        # if y-interecept is zero, leave the term outj
        elif self.b == 0 and self.m > 0:
            return str(self.m) + 'x'

        elif self.b == 0 and self.m < 0:
            return '- ' + str(self.m * -1) + 'x'

        elif self.m == 0 and self.b > 0:
            return '+ ' + str(self.b)

        elif self.m == 0 and self.b < 0:
            return '- ' + str(self.b * -1)    

        elif self.m < 0 and self.b > 0:
            return '- ' + str(self.m * -1) + 'x + ' + str(self.b)

        elif self.m < 0 and self.b < 0:
            return '- ' + str(self.m * -1) + 'x - ' + str(self.b * -1)
        else:
            return str(self.m) + 'x + '  + str(self.b)


        
    # method called add that adds together two LinearEquation objects. It should return a new LinearEquation object whose slope is equal to the sum of the two slopes, and whose y-intercept is equal to the sum of the two y-intercepts.  
    def add(self, self1):
        m = self.m + self1.m
        b = self.b + self1.b
        return LinearEquation(m,b)

        
    # method called sub that subtracts two LinearEquation objects. Similar to 'add' above.
    def sub(self, self2):
        m = self.m - self2.m
        b = self.b - self2.b
        return LinearEquation(m,b)
    
    # method called compose that returns a new LinearEquation object that represents the composition of the two equations given as arguments. 
    def compose(self, self3):
        m = self.m * self3.m
        b = self.m * self3.b + self.b
        return LinearEquation(m,b)
    
    def evaluate(self, self4):
        eval = (self.m * self4) + self.b
        return eval
    
    
def main():

        f = LinearEquation(5,3)
        print("f(x) =",f.showEq())
        print("f(3) =",f.evaluate(3),"\n")
                 
        g = LinearEquation(-2,-6)
        print("g(x) =",g.showEq())
        print("g(-2) =",g.evaluate(-2),"\n")

        h = f.add(g)
        print("h(x) = f(x) + g(x) =",h.showEq())
        print("h(-4) =",h.evaluate(-4),"\n")

        j = f.sub(g)
        print("j(x) = f(x) - g(x) =",j.showEq())
        print("j(-4) =",j.evaluate(-4),"\n")

        k = f.compose(g)
        print("f(g(x)) =",k.showEq(),"\n")
           
        m = g.compose(f)
        print("g(f(x)) =",m.showEq(),"\n")

        g = LinearEquation(5,-3)
        print("g(x) =",g.showEq())
        print("g(-2) =",g.evaluate(-2),"\n")
           
        h = f.add(g)
        print("h(x) = f(x) + g(x) =",h.showEq())
        print("h(-4) =",h.evaluate(-4),"\n")

        j = f.sub(g)
        print("j(x) = f(x) - g(x) =",j.showEq())
        print("j(-4) =",j.evaluate(-4),"\n")
           
main()
