class BookScanner:
    def __init__(self, file):
        self.file = file
        f = open(self.file, "r")
        self.books, self.libraries, self.days = tuple(int(i) for i in f.readline().rstrip().split(" "))

        # library_data = tuple(([], set()) for i in range(libraries))

        self.library_data = {i: [] for i in range(self.libraries)}
        self.library_books = {i: set() for i in range(self.libraries)}
        self.book_scores = tuple(int(i) for i in f.readline().rstrip().split(" "))

        # 扫图书馆
        for i in range(self.libraries):
            for j in f.readline().rstrip().split(" "):
                self.library_data[i].append(int(j))
            for j in f.readline().rstrip().split(" "):
                self.library_books[i].add(int(j))
        f.close()

        self.already_sign_up = set()
        self.library_score_queue = [i for i in range(self.libraries)]
        self.result = [[self.libraries]] + [[] for i in range(self.libraries * 2)]

    def operate(self):
        i = 0
        while i < self.result[0][0]:
            self.library_score_queue = \
                sorted(self.library_score_queue,
                       key=lambda x: -sum([self.book_scores[i] for i in self.library_books[x]
                                           if i not in self.already_sign_up]) * (self.library_data[x][2] /
                                                                                 (self.library_data[x][1] ** 2)))

            tmp = self.library_books[self.library_score_queue[0]] - self.already_sign_up
            if len(tmp) == 0:
                self.result[0][0] = self.result[0][0] - 1
                self.result.pop()
                continue
            self.result[(i + 1) * 2 - 1].append(self.library_score_queue[0])  # 图书馆编号
            # result[(i + 1) * 2 - 1].append(len(library_books[library_score_queue[i]]))  # 书数量
            # result[(i + 1) * 2] = list(library_data[library_score_queue[i]])
            #
            self.result[(i + 1) * 2 - 1].append(len(tmp))
            self.result[(i + 1) * 2] = list(tmp)

            # 去重
            self.already_sign_up = self.already_sign_up | tmp
            # print("already_sign_up: " + str(already_sign_up))

            print(i)
            i += 1
            self.library_score_queue.pop(0)

    def write_file(self):
        print(self.library_data)
        print(self.result)
        output = self.result

        f = open(self.file.replace("txt", "out1"), "w")
        for i in output:
            f.write(" ".join([str(j) for j in i]))
            f.write("\n")

        f.close()

    # @staticmethod
    def __call__(self):
        # f = BookScanner(BookScanner)
        self.operate()
        self.write_file()


if __name__ == '__main__':
    input_list = ["Test/a_example.txt",
                  "Test/b_read_on.txt",
                  "Test/c_incunabula.txt",
                  "Test/d_tough_choices.txt",
                  "Test/e_so_many_books.txt",
                  "Test/f_libraries_of_the_world.txt"]

    for i in input_list:
        i = BookScanner(i)
        i()
