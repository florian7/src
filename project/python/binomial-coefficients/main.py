#!/usr/bin/python3

import sys
from binomial_coefficients import *

def help():
    print("Usage: {} {--draw n | '[(n k), ...]'}".format(sys.argv[0]))
    exit()

def main():

    argv = sys.argv

    if len(argv) < 2:
        help()

    if argv[1] == '--draw':
        try:
            n = int(argv[2])
        except ValueError as e:
            print("ValueError: " '\n'.join(e.args))
            help()

        draw(n)

    else:
        
        for nk in argv[1].split(','):

            try:
                n, k = nk.strip().split(' ')

                if n[0] != '(' or k[-1] != ')':
                    raise SyntaxError("Incorrect parenthesis")

                n, k = int(n[1:]), int(k[:-1])

            except SyntaxError as e:
                print("SyntaxError: " + '\n'.join(e.args))
                help()

            except ValueError as e:
                print("ValueError: " + '\n'.join(e.args))
                help()

            coef = coefficient(n, k)
            print("({}, {}) = {}".format(n, k, coef))

if __name__ == '__main__':
    main()
