# 读文件
# file = "Test/a_example.in"
file = "Test/b_small.in"
# file = "Test/c_medium.in"
# file = "Test/d_quite_big.in"
# file = "Test/e_also_big.in"

f = open(file, "r")

amount = int(f.readline().split(" ")[0])
denominations = tuple(int(i) for i in f.readline().rstrip().split(" "))

f.close()

# 操作

# min(myList, key=lambda x:abs(x-myNumber))


# Method 1
result = list(denominations)
current_sum = sum(result)
while current_sum > amount:
    # print(result)
    diff = current_sum - amount
    closest = min(result, key=lambda x: abs(x - diff))
    result.remove(closest)
    current_sum = sum(result)


# 写文件
if __name__ == '__main__':

    output = [str(denominations.index(i)) for i in sorted(result)]

    f = open(file.replace("in", "out"), "w")
    f.write(str(len(output)) + "\n")
    f.write(" ".join(output))

    f.close()
