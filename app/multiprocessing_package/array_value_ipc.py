import multiprocessing

# Calling function to get square value of each number in list & storing result into share memory
# as square_results (array) and sum (variable).
def cal_square(numbers, square_results, sum):
    for idx, val in enumerate(numbers):
        sum.value += val
        square_results[idx] = val * val

if __name__ == "__main__":
    numbers = [3, 4, 5]
    #Share Array to communicate between two processes
    square_results = multiprocessing.Array('i', 3)
    #Share variable to communicate between two process
    sum = multiprocessing.Value('d', 1)

    #as process p1 is generated
    p1 = multiprocessing.Process(target=cal_square, args=(numbers, square_results, sum))

    #process p1 getting started to execution
    p1.start()

    #wait other processes untill process p1 is completed
    p1.join()
    print("square result::", square_results[:])
    print("sum result:: ", sum.value)
    print("Main process is done")


