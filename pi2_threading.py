import decimal, threading, sys
fact_out = [0, 0, 0]
n=int(input("n: "))

sys.setrecursionlimit(2147483647)

def fact(l):
    n=l[0]
    i=l[1]
    factorial = 1
    while n>0:
          factorial*=n
          n-=1
    fact_out[i] = factorial

def func1(precision):
    p = decimal.getcontext().prec
    decimal.getcontext().prec = precision
    d = decimal.Decimal(10005).sqrt()
    decimal.getcontext().prec = p
    return 426880 * d

def func2(k):
    _a = threading.Thread(target=fact, args=[[6*k, 0]])
    _b = threading.Thread(target=fact, args=[[3*k, 1]])
    _c = threading.Thread(target=fact, args=[[k, 2]])
    _a.start()
    _b.start()
    _c.start()
    print("_a:%s\n_b:%s\n_c:%s"%(_a.name, _b.name, _c.name))
    _c.join()
    _b.join()
    _a.join()
    a = decimal.Decimal(fact_out[0]*(545140134*k+13591409))
    b = decimal.Decimal(fact_out[1]*(fact_out[2]**3)*((-262537412640768000)**k))
    res = a / b
    if k > 0:
        return res + func2(k - 1)
    else:
        return res

def pi_chudnovsky(k, precision):
      return func1(precision)/func2(k)

p = 10*n+1
decimal.getcontext().prec = p
pi = pi_chudnovsky(n*2, p)

print(str(pi)[n+1])