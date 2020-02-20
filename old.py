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
# library_score_queue = sorted(library_score_queue, key=lambda x: -sum([book_scores[i] for i in library_books[x]]) -
#                                                                 (library_data[x][2] / library_data[x][1]))

for i in library_score_queue:
    print(sum([book_scores[i] for i in library_books[i]]), (library_data[i][2] / library_data[i][1]))

