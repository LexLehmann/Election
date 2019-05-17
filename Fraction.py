class Fraction:
    def __init__(self, num, de):
        self.numer = num
        self.denom = de

    def __repr__(self):
        return str(self.numer) + "/" + str(self.denom)

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

    def __float__(self):
        return self.numer/self.denom

    def __int__(self):
        self.simplify()
        return self.numer

    def __floor__(self):
        self.numer = self.number - (self.numer%self.denom)
        return(Fraction(self.numer, self.denom))

    def simplify(self):
        num1 = self.numer
        num2 = self.denom

        num3 = num1%num2
        while(num3 != 0):
            num1 = num2
            num2 = num3
            num3 = num1%num2

        if self.denom < 0:
            self.numer = self.numer*-1
            self.denom = self.denom*-1
        val = Fraction(self.numer//num2, self.denom//num2)
        return val.simplfyToTrillion()

    def simplfyToTrillion(self):
        precision = 10000000000000
        if self.denom > precision:
            numer = (self.numer * precision) // self.denom
            denom = precision
            if (self.numer*precision)%self.denom >= self.denom//2:
                numer += 1

            num1 = numer
            num2 = denom

            num3 = num1 % num2
            while (num3 != 0):
                num1 = num2
                num2 = num3
                num3 = num1 % num2

            self.numer = numer//num2
            self.denom = denom//num2
        return Fraction(self.numer, self.denom)

    def __sub__(self, other):
        numer = self.numer
        denom = self.denom
        if isinstance(other, Fraction):
            otherNumer = other.numer
            otherDenom = other.denom
        elif isinstance(other, int):
            otherNumer = other
            otherDenom = 1
        if (self.denom != otherDenom):
            tempDenom = self.denom
            tempNumer = self.numer
            denom = tempDenom * otherDenom
            numer = tempNumer * otherDenom
            otherNumer = otherNumer * tempDenom
        numer = numer - otherNumer

        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __rsub__(self, other):
        numer = self.numer
        denom = self.denom
        if isinstance(other, int):
            otherNumer = other
            otherDenom = 1
        if (self.denom != otherDenom):
            tempDenom = self.denom
            tempNumer = self.numer
            denom = tempDenom * otherDenom
            numer = tempNumer * otherDenom
            otherNumer = otherNumer * tempDenom
        numer = numer - otherNumer

        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __add__(self, other):
        numer = self.numer
        denom = self.denom
        if isinstance(other, Fraction):
            otherNumer = other.numer
            otherDenom = other.denom
        elif isinstance(other, int):
            otherNumer = other
            otherDenom = 1
        if (self.denom != otherDenom):
            tempDenom = self.denom
            tempNumer = self.numer
            denom = tempDenom*otherDenom
            numer = tempNumer*otherDenom
            otherNumer = otherNumer*tempDenom
        numer = numer + otherNumer

        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __radd__(self, other):
        numer = self.numer
        denom = self.denom
        if isinstance(other, int):
            otherNumer = other
            otherDenom = 1
        if (self.denom != otherDenom):
            tempDenom = self.denom
            tempNumer = self.numer
            denom = tempDenom*otherDenom
            numer = tempNumer*otherDenom
            otherNumer = otherNumer*tempDenom
        numer = numer + otherNumer

        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numer = self.numer*other.numer
            denom = self.denom*other.denom
        elif isinstance(other, int):
            numer = self.numer*other
            denom = self.denom

        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __rmul__(self, other):
        if isinstance(other, int):
            numer = self.numer*other
            denom = self.denom
        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            numer = self.numer * other.denom
            denom = self.denom * other.numer
        elif isinstance(other, int):
            numer = self.numer
            denom = self.denom * other

        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __rtruediv__(self, other):
        if isinstance(other, int):
            numer = self.denom * other
            denom = self.numer
        val = Fraction(numer, denom)
        val = val.simplify()
        return val

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numer*other.denom == other.numer*self.denom
        elif isinstance(other, int):
            copy = self.simplify()
            return copy.numer == other and copy.denom == 1
        else:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numer * other.denom < other.numer * self.denom
        elif isinstance(other, int):
            return float(self) < other
        else:
            return False

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numer * other.denom > other.numer * self.denom
        elif isinstance(other, int):
            return float(self) > other
        else:
            return False

    def __ge__(self, other):
        return self == other or self > other