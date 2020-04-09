import multiprocessing

"""
 Why is lock useful in multiprocessing technique?
  Answer: While multiple processes or threads are using common shared 
   resources(memory, file or database etc) that time some conflict situation 
   can happen between calculations so get rid of this embarrassing movement 
   multiprocessing introduced one of the concepts called lock to utilize shared 
   resources between processes or threads. 
"""

def deposit(balance, lock):
    for val in range(10000):
        lock.acquire()
        balance.value += val
        lock.release()

def withdraw(balance, lock):
    for val in range(10000):
        lock.acquire()
        balance.value -= val
        lock.release()

if __name__ == "__main__":
    #shared variable
    bank_balance = multiprocessing.Value('i', 200)

    #lock in mutiprocessing
    lock = multiprocessing.Lock()

    deposit_process = multiprocessing.Process(target=deposit, args=(bank_balance, lock))
    withdraw_process = multiprocessing.Process(target=withdraw, args=(bank_balance, lock))

    deposit_process.start()
    withdraw_process.start()

    deposit_process.join()
    withdraw_process.join()

    print("Latest bank balance:", bank_balance.value)
