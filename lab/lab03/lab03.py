"""Lab 3: Recursion and Tree Recursion"""

# Q1
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if b==0:
        return c
    elif b==1:
        return a+c
    else:
        return ab_plus_c(a,b-1,c)+a

# Q2
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a>b:
        if a%b==0:
            return b
        else:
            return gcd(b,a%b)
    else:
        if b%a==0:
            return a
        else:
            return gcd(a,b%a)

# Q3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    steps=1
    print(n)
    if n!=1:
        if n%2==0:
            steps=hailstone(n//2)+1
        else:
            steps=hailstone(n*3+1)+1
    return steps
