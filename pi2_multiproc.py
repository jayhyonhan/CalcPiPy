import decimal, sys
from multiprocessing import Process, Manager


def main():
    global fact_out
    manager = Manager()
    fact_out = manager.list([0, 0, 0])
    n=int(input("n: "))
    sys.setrecursionlimit(2147483647)
    sys.set_int_max_str_digits(2147483647)
    p = 10*n+1
    decimal.getcontext().prec = p
    pi = pi_chudnovsky(n*2, p)
    print(str(pi)[n+1])

def fact(l):
    n=l[0]
    _i=l[1]
    fact_out = l[2]
    factorial = 1
    while n>0:
          factorial*=n
          n-=1
    fact_out[_i] = factorial

def func1(precision):
    p = decimal.getcontext().prec
    decimal.getcontext().prec = precision
    d = decimal.Decimal(10005).sqrt()
    decimal.getcontext().prec = p
    return 426880 * d

def func2(k):
    arguments = [[6*k, 0, fact_out], [3*k, 1, fact_out], [k, 2, fact_out]]
    procs = []
    for argument in arguments:
        proc = Process(target=fact, args=(argument,))
        procs.append(proc)
        proc.start()
        print(proc.name)

    for proc in procs:
        proc.join()
    a = decimal.Decimal(fact_out[0]*(545140134*k+13591409))
    b = decimal.Decimal(fact_out[1]*(fact_out[2]**3)*((-262537412640768000)**k))
    res = a / b
    if k > 0:
        return res + func2(k - 1)
    else:
        return res

def pi_chudnovsky(k, precision):
      return func1(precision)/func2(k)

if __name__ == '__main__':
    main()