# 读文件
# file = "Test/a_example.txt"
# file = "Test/b_read_on.txt"
# file = "Test/c_incunabula.txt"
# file = "Test/d_tough_choices.txt"
# file = "Test/e_so_many_books.txt"
file = "Test/f_libraries_of_the_world.txt"

f = open(file, "r")

books, libraries, days = tuple(int(i) for i in f.readline().rstrip().split(" "))

# library_data = tuple(([], set()) for i in range(libraries))

library_data = {i: [] for i in range(libraries)}

library_books = {i: set() for i in range(libraries)}

book_scores = tuple(int(i) for i in f.readline().rstrip().split(" "))

# 扫图书馆
for i in range(libraries):
    for j in f.readline().rstrip().split(" "):
        library_data[i].append(int(j))
    for j in f.readline().rstrip().split(" "):
        library_books[i].add(int(j))
f.close()

# 操作

already_sign_up = set()

library_score_queue = [i for i in range(libraries)]

# library_score_queue = sorted(library_score_queue, key=lambda x: -sum([book_scores[i] for i in library_books[x]]))
library_score_queue = sorted(library_score_queue, key=lambda x: -sum([book_scores[i] for i in library_books[x]]) *
                                                                (library_data[x][2] / (library_data[x][1] ** 1)))

library_score_queue = sorted(library_score_queue,
                             key=lambda x: -(
                                     (sum([book_scores[i] for i in library_books[x]]) / (
                                             len(library_books[x]) * library_data[x][1])) *
                                     library_data[x][2]) / library_data[x][1])
# 可以除天数
# print(library_score_queue)

result = [[libraries]] + [[] for i in range(libraries * 2)]

# for i in range(libraries):
i = 0
while i < result[0][0]:
    tmp = library_books[library_score_queue[i]] - already_sign_up
    if len(tmp) == 0:
        result[0][0] = result[0][0] - 1
        result.pop()
        continue
    result[(i + 1) * 2 - 1].append(library_score_queue[i])  # 图书馆编号
    # result[(i + 1) * 2 - 1].append(len(library_books[library_score_queue[i]]))  # 书数量
    # result[(i + 1) * 2] = list(library_data[library_score_queue[i]])
    #
    result[(i + 1) * 2 - 1].append(len(tmp))
    result[(i + 1) * 2] = list(tmp)

    # 去重
    already_sign_up = already_sign_up | tmp
    # print("already_sign_up: " + str(already_sign_up))
    print(i)
    i += 1
'''    for j in range(libraries):
        if j != library_score_queue[i]:
            # for item in already_sign_up:
                # print(item)
                # library_data[j][1].discard(item)
            library_books[j] -= already_sign_up
'''
# 写文件
if __name__ == '__main__':
    print(library_data)
    print(result)
    output = result

    f = open(file.replace("txt", "out"), "w")
    for i in output:
        f.write(" ".join([str(j) for j in i]))
        f.write("\n")

    f.close()
