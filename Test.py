def main():
    input_list = ["Test/a_example.txt",
                  "Test/b_read_on.txt",
                  "Test/c_incunabula.txt",
                  "Test/d_tough_choices.txt",
                  "Test/f_libraries_of_the_world.txt",
                  "Test/e_so_many_books.txt",
                  "Test/a_example.txt",
                  "Test/b_read_on.txt",
                  "Test/c_incunabula.txt",
                  # "Test/d_tough_choices.txt",
                  "Test/f_libraries_of_the_world.txt",
                  "Test/e_so_many_books.txt"]
    output_list = ["Highest/a_example.txt",
                   "Highest/b_read_on.txt",
                   "Highest/c_incunabula.txt",
                   "Highest/d_tough_choices.txt",
                   "Highest/f_libraries_of_the_world.txt",
                   "Highest/e_so_many_books.txt",
                   "Out/a_example.txt",
                   "Out/b_read_on.txt",
                   "Out/c_incunabula.txt",
                   # "Out/d_tough_choices.txt",
                   "Out/f_libraries_of_the_world.txt",
                   "Out/e_so_many_books.txt"]

    for i in range(len(input_list)):
        file = input_list[i]
        f = open(file, "r")
        f.readline()
        book_scores = tuple(int(i) for i in f.readline().rstrip().split(" "))
        f.close()

        file = output_list[i]
        f = open(file, 'r')
        lines = f.readlines()
        score = 0
        for j in range(len(lines)):
            if (j == 0) or (j % 2 == 1):
                continue
            for book in lines[j].rstrip().split(" "):
                score += book_scores[int(book)]
        print("File " + file + ": " + str(score))


if __name__ == '__main__':
    main()
