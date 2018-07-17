from sympy import *


def main():
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    e = ( a*b*b + 2*b*a*b )**c

    print('')
    pprint(e)
    print('')

    a = Symbol('a')
    b = Symbol('b')
    e = (a + 2*b)**5
###############################################################################
    print("\nExpression : ")
    print()
    pprint(e)
    print("\n\nDifferentiating w.r.t. a:")
    print()
    pprint(e.diff(a))
    print("\n\nDifferentiating w.r.t. b:")
    print()
    pprint(e.diff(b))
    print("\n\nSecond derivative of the above result w.r.t. a:")
    print()
    pprint(e.diff(b).diff(a, 2))
    print("\n\nExpanding the above result:")
    print()
    pprint(e.expand().diff(b).diff(a, 2))
    print()
##############################################################################
    a = Symbol('a')
    b = Symbol('b')
    e = (a + b)**5

    print("\nExpression:")
    pprint(e)
    print('\nExpansion of the above expression:')
    pprint(e.expand())
    print()
################################################################################
    a = Symbol('a')
    b = Symbol('b')
    e = log((a + b)**5)
    print()
    pprint(e)
    print('\n')

    e = exp(e)
    pprint(e)
    print('\n')

    e = log(exp((a + b)**5))
    pprint(e)
    print()

if __name__ == "__main__":
    main()