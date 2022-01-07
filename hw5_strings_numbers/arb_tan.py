import decimal as d

pi = None


def sin_taylor(x):
    sin = x
    last_summand = x
    fact_num = 1
    last_sin = None

    while sin != last_sin:
        fact_num += 2

        last_summand *= -x * x
        last_summand /= fact_num * (fact_num - 1)

        last_sin = sin
        sin += last_summand

    return sin


def cos_taylor(x):
    cos = 1
    last_summand = 1
    fact_num = 0
    last_cos = None

    while cos != last_cos:
        fact_num += 2

        last_summand *= -x * x
        last_summand /= fact_num * (fact_num - 1)

        last_cos = cos
        cos += last_summand

    return cos


def compute_pi():
    k = 1
    ak = d.Decimal(1)
    a = ak
    b = d.Decimal(0)
    last_a = None
    last_b = None
    coeff = d.Decimal(640320) ** 3 / 24

    while last_a != a or last_b != b:
        last_a = a
        last_b = b

        ak *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        ak /= k ** 3 * coeff
        a += ak
        b += ak * k
        k += 1

    pi = (426880 * d.Decimal(10005).sqrt()) / (13591409 * a + 545140134 * b)

    return pi


def grad_to_rad(x):
    global pi

    if pi is None:
        pi = compute_pi()
    return x * pi / 200


def arb_tan(A, E):
    with d.localcontext() as l:
        l.prec = 1500
        A = d.Decimal(A)
        x = grad_to_rad(A)
        sin = sin_taylor(x)
        cos = cos_taylor(x)

    with d.localcontext() as l:
        l.prec = E
        res = sin / cos

    return res


if __name__ == "__main__":
    A = input()
    E = int(input())

    print(arb_tan(A, E))
