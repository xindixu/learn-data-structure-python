def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, num, den):
        if not isinstance(num, int):
            raise TypeError("Numerator needs to be an integer")
        if not isinstance(den, int):
            raise TypeError("Denominator needs to be an integer")

        common = gcd(num, den)
        self.num = num // common
        self.den = den // common

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction(num={self.num}, den={self.den})"

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return self.get_first_num(other) == self.get_second_num(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.get_first_num(other) > self.get_second_num(other)

    def __ge__(self, other):
        return self.get_first_num(other) >= self.get_second_num(other)

    def __lt__(self, other):
        return self.get_first_num(other) < self.get_second_num(other)

    def __le__(self, other):
        return self.get_first_num(other) <= self.get_second_num(other)

    def get_first_num(self, other):
        return self.num * other.den

    def get_second_num(self, other):
        return other.num * self.den


def main():
    f1 = Fraction(6, 8)
    f2 = Fraction(3, 4)
    f3 = f1 * f2
    print(f3)
    print(f1 < f2)
    print(f1 != f2)
    print(f1 == f2)
    print(f1.__repr__())


if __name__ == '__main__':
    main()
