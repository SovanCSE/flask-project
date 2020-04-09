import multiprocessing

#as under of new process calling this fucntion
def calc_sqaue(numbers, q):
    for num in  numbers:
        q.put(num * num)

if __name__ == "__main__":
    numbers = [2.2, 4, 10]

    #Multiprocessing queue to shared between two processes
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=calc_sqaue, args=(numbers, q))
    #Process is started calling the function & other process is waiting
    # untill current process  get completed
    p.start()
    p.join()

    #If queue is not empty then enter into this condition
    while not q.empty():
        print(q.get())

    print("Main porcess is Done!!")




