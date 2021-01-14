def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, num, den):
        common = gcd(num, den)
        self.num = num // common
        self.den = den // common

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num


def main():
    f1 = Fraction(6, 8)
    f2 = Fraction(3, 4)
    f3 = f1 + f2


if __name__ == '__main__':
    main()
