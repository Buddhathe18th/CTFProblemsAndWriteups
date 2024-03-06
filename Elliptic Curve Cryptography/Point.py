#Class of point in field in a mod.
# The only point with mod 0 is the origin.


class Point:
    def __init__(self, x, y, a, b, mod):

        if mod==0:
            self.x = x
            self.y = y
        else:
            self.x = x % mod
            self.y = y % mod

        self.a = a
        self.b = b
        self.mod = mod

    def __str__(self):
        return ("Point ("+str(self.x)+","+str(self.y)+") on y^2=x^3+"+str(self.a)+"x+"+str(self.b)+" on group mod "+str(self.mod))


    @staticmethod
    def origin(a=0,b=0,mod=0):
        return Point(0,0,a,b, mod)

    def equal(self,P):
        return (self.x == P.x and self.y == P.y and self.a == P.a and self.b ==P.b and self.mod == P.mod)

    @staticmethod
    def add(PList):
        sum=PList[0]
        for i in range(1,len(PList)):
            sum=Point.addTwo(sum,PList[i])
        return sum


    @staticmethod
    def negate(P):
        return Point(P.x,-P.y,P.a,P.b,P.mod)

    @staticmethod
    def addTwo(Q,P):
        if (P.mod!=Q.mod):
            raise Exception("Unequal mod, cannot be operated together")
        if (P== Point.origin()):
            return Q
        elif (Q==Point.origin()):
            return P
        if (P.x==Q.x and P.y==-Q.y):
            return Point.origin()

        if (not P.equal(Q)):
            slope=(Q.y-P.y)* pow((Q.x-P.x),-1,P.mod)
        else:
            slope=(3*P.x**2 + P.a)*pow((2*P.y),-1,P.mod)
        xFinal = (slope**2-P.x-Q.x)%P.mod
        yFinal = (slope * (P.x-xFinal) - P.y)%P.mod

        return Point(xFinal,yFinal,P.a,P.b,P.mod)

    def copyOf(self):
        return Point(self.x,self.y,self.a,self.b,self.mod)

    @staticmethod
    def multiply(n,P):
        if type(n) is not int or n<=0:
            raise Exception("n must be an positive integer")

        Q=P.copyOf()
        R=Point.origin(P.a,P.b,P.mod)
        while n>0:
            if n%2==1:
                R=Point.addTwo(R,Q)
            Q=Point.addTwo(Q,Q)
            n=int(n/2)
        return R
