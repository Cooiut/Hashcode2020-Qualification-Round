# 读文件
# file = "Test/a_example.txt"
# file = "Test/b_read_on.txt"
# file = "Test/c_incunabula.txt"
# file = "Test/d_tough_choices.txt"
# file = "Test/e_so_many_books.txt"
file = "Test/f_libraries_of_the_world.txt"

f = open(file, "r")

books, libraries, days = tuple(int(i) for i in f.readline().rstrip().split(" "))

library_data = tuple(([], []) for i in range(libraries))

book_scores = tuple(int(i) for i in f.readline().rstrip().split(" "))

# 扫图书馆
for i in range(libraries):
    for j in f.readline().rstrip().split(" "):
        library_data[i][0].append(int(j))
    for j in f.readline().rstrip().split(" "):
        library_data[i][1].append(int(j))
f.close()

# 操作

already_sign_up = set()

library_score_queue = [i for i in range(libraries)]

library_score_queue = sorted(library_score_queue, key=lambda x: sum([book_scores[i] for i in library_data[x][1]]))
# 可以除天数
# print(library_score_queue)

result = [[libraries]] + [[] for i in range(libraries * 2)]

for i in range(len(library_score_queue)):
    result[(i + 1) * 2 - 1].append(library_score_queue[i])
    result[(i + 1) * 2 - 1].append(len(library_data[library_score_queue[i]][1]))

    result[(i + 1) * 2] = library_data[library_score_queue[i]][1]

print(result)

# 写文件
if __name__ == '__main__':
    # print(library_data)

    output = result

    f = open(file.replace("txt", "out"), "w")
    for i in output:
        f.write(" ".join([str(j) for j in i]))
        f.write("\n")

    f.close()
