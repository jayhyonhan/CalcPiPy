import decimal, threading, sys
from multiprocessing import Pool

fact_out = [0, 0, 0]
def factorial_function(l):
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
    #threading
    #_a = threading.Thread(target=factorial_function, args=[[6*k, 0]])
    #_b = threading.Thread(target=factorial_function, args=[[3*k, 1]])
    #_c = threading.Thread(target=factorial_function, args=[[k, 2]])
    #_a.start()
    #_b.start()
    #_c.start()
    #print("_a:%s\n_b:%s\n_c:%s"%(_a.name, _b.name, _c.name))
    #_c.join()
    #_b.join()
    #_a.join()
    #parallel proccesing
    
    # only for multiproccesing
    _pool = Pool()
    _a = _pool.apply_async(func=factorial_function, args=([6*k, 0]))
    _b = _pool.apply_async(func=factorial_function, args=([3*k, 1]))
    _c = _pool.apply_async(func=factorial_function, args=([k, 2]))
    _c.wait()
    _b.wait()
    _a.wait()
    a = decimal.Decimal(fact_out[0]*(545140134*k+13591409))
    b = decimal.Decimal(fact_out[1]*(fact_out[2]**3)*((-262537412640768000)**k))
    print(a,b)
    res = a / b
    if k > 0:
        return res + func2(k - 1)
    else:
        return res

def pi_chudnovsky(k, precision):
      return func1(precision)/func2(k)
if __name__ == '__main__':
    n=int(input("n: "))
    print("start")
    sys.setrecursionlimit(2147483647)
    p = 10*n+1
    decimal.getcontext().prec = p
    pi = pi_chudnovsky(n*2, p)
    print(str(pi)[n+1])