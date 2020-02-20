# 读文件
file = "Test/a_example.txt"
# file = "Test/b_read_on.txt"
# file = "Test/c_incunabula.txt"
# file = "Test/d_tough_choices.txt"
# file = "Test/e_so_many_books.txt"
# file = "Test/f_libraries_of_the_world.txt"

f = open(file, "r")

books, libraries, days = tuple(int(i) for i in f.readline().rstrip().split(" "))

library_data = tuple(([], []) for i in range(libraries))

book_scores = tuple(int(i) for i in f.readline().rstrip().split(" "))

# 扫图书馆
for i in range(libraries):
    for j in f.readline().rstrip().split(" "):
        library_data[i][0].append(j)
    for j in f.readline().rstrip().split(" "):
        library_data[i][1].append(j)
f.close()

print(library_data)
# 操作

# min(myList, key=lambda x:abs(x-myNumber))


# Method 1
result = []

# 写文件
if __name__ == '__main__':
    output = []

    f = open(file.replace("txt", "out"), "w")
    f.write(str(len(output)) + "\n")
    f.write(" ".join(output))

    f.close()
