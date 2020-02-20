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


all_books = set(i - 1 for i in book_scores)
already_sign_up = set()

library_score_queue1 = [i for i in range(libraries)]
# print(library_score_queue1)

library_score_queue = sorted(library_score_queue1, key=lambda x: sum([book_scores[i] for i in library_data[x][1]]))
# 可以除天数
# print(library_score_queue)
# print(library_data, 1111111111)
# print(book_scores)
# print(all_books)
library_days_queue = sorted(library_score_queue1, key=lambda x: library_data[x][0][2] / library_data[x][0][1],
                            reverse=True)
# print(library_days_queue, 11111111)

result = []
result.append([len(library_days_queue)])
for x in library_days_queue:
    current = set(library_data[x][1])
    result.append([x, current])
    # print(result)
    already_sign_up = already_sign_up.union(current)

# print(result)

# 写文件
if __name__ == '__main__':
    # print(library_data)

    output = []

    f = open(file.replace("txt", "out"), "w")
    f.write(str(result[0][0]) + "\n")
    for x in result[1:]:
        f.write(str(x[0]) + " ")
        f.write(str(len(x[1])))
        f.write("\n")
        f.write(str(x[1]).replace(",", "").replace("{", "")[:-1])
        f.write("\n")

f.close()
