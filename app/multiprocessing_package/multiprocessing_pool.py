import multiprocessing
import time

def f(n):
    sum = 0
    for num in range(1000):
        sum += num
    return sum

if  __name__ == "__main__":

    #Pool processing technique to get sum of 0 to 1000 numbers  for 100000 times by
    #sharing multiple cores(5)
    t1 = time.time()
    p = multiprocessing.Pool(processes=5)
    result1 = p.map(f, range(100000))
    p.close()
    p.join()
    print("Pool took: {}".format(time.time() - t1))

    #Serial processing technique to get sum of 0 to 1000 numbers for 100000 times
    # by single core only
    t2 = time.time()
    result2 = []
    for i in range(100000):
        result2.append(f(i))
    print("serial Processing took: {}".format(time.time() - t2))

