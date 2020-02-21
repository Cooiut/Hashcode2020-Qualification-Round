class BookScanner:
    def __init__(self, file):
        self.file = file
        f = open(self.file, "r")
        self.books, self.libraries, self.days = tuple(int(i) for i in f.readline().rstrip().split(" "))

        # library_data = tuple(([], set()) for i in range(libraries))

        self.library_data = {i: [] for i in range(self.libraries)}
        self.library_books = {i: set() for i in range(self.libraries)}
        self.book_scores = [int(i) for i in f.readline().rstrip().split(" ")]
        self.reamining_days = self.days + 10

        # 扫图书馆
        for i in range(self.libraries):
            for j in f.readline().rstrip().split(" "):
                self.library_data[i].append(int(j))
            for j in f.readline().rstrip().split(" "):
                self.library_books[i].add(int(j))
        f.close()

        self.already_sign_up = set()
        self.library_score_queue = [i for i in range(self.libraries)]
        self.result = [[self.libraries]]  # + [[] for i in range(self.libraries * 2)]

    def operate(self):
        i = 0
        while i < self.result[0][0]:

            self.library_score_queue = sorted(self.library_score_queue,
                                              key=lambda x: -sum([self.book_scores[i] for i in self.library_books[x]]) *
                                                            (self.library_data[x][2] / (self.library_data[x][1] ** 2)))


            # self.library_score_queue = sorted(self.library_score_queue,
            #                                   key=lambda x: -sum([self.book_scores[k] for k in self.library_books[x]]) /
            #                                                 ((self.reamining_days - self.library_data[x][1] if self.reamining_days - self.library_data[x][1] != 0 else -1) /
            #                                                  self.library_data[x][2]))
            print(self.library_score_queue)

            tmp = self.library_books[self.library_score_queue[0]] - self.already_sign_up
            if len(tmp) == 0:
                self.result[0][0] = self.result[0][0] - 1
                continue
            self.result.append([])
            self.result.append([])
            self.result[(i + 1) * 2 - 1].append(self.library_score_queue[0])  # 图书馆编号
            self.result[(i + 1) * 2 - 1].append(len(tmp))
            self.result[(i + 1) * 2] = sorted(tmp, key=lambda x: -self.book_scores[x])

            # 去重
            self.already_sign_up = self.already_sign_up | tmp
            for j in self.already_sign_up:
                self.book_scores[j] = 0

            print(self.file, i)

            # 判断超时
            self.reamining_days -= self.library_data[self.library_score_queue[0]][1]
            if self.reamining_days < 0:
                self.result[0][0] = int((len(self.result) - 1) / 2)
                break

            i += 1
            self.library_score_queue.pop(0)

    def write_file(self):
        print(self.library_data)
        print(self.result)
        output = self.result

        f = open(self.file.replace("Test", "Out"), "w")
        for i in output:
            f.write(" ".join([str(j) for j in i]))
            f.write("\n")

        f.close()

    # @staticmethod
    def __call__(self):
        # f = BookScanner(BookScanner)
        self.operate()
        self.write_file()


def run_it(f):
    x = BookScanner(f)
    x()


if __name__ == '__main__':
    input_list = ["Test/a_example.txt",
                  "Test/b_read_on.txt",
                  "Test/c_incunabula.txt",
                  "Test/e_so_many_books.txt",
                  "Test/f_libraries_of_the_world.txt",
                  "Test/d_tough_choices.txt"]
    mult = True
    # mult = False
    if mult:
        from multiprocessing import Pool

        pool = Pool(4)
        for file in input_list:
            pool.apply_async(run_it, (file,))
        pool.close()
        pool.join()
    else:
        run_it(input_list[1])
