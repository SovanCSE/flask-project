
scores = [[1,35,80],[2,30,70],[3,40,75],[4, 32, 60],[5, 40, 85]]
#get list of marks with depend of present(add 2 for greater than equal to 35 else -2)
abv_avg = list(map(lambda x: x[2]+2 if x[1]>= 35 else x[2]-2, scores))
print("max result: ", abv_avg)


