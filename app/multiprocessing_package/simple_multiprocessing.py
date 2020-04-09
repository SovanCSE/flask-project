import multiprocessing

square_results = []
def cal_square(numbers):
    global square_results
    for num in numbers:
        square_results.append(num * num)
    print("square_results is inside another process::", square_results)

if __name__ == "__main__":
    numbers = [2,3,4]
    square_results = []
    p1 = multiprocessing.Process(target=cal_square, args=(numbers,))
    p1.start()
    p1.join()

    print("square_results in main process:", square_results)
    print("Done!!")

