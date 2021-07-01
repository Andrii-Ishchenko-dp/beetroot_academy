def count_lines(filename):
    with open(filename) as file:
        sim = [row.rstrip() for row in file]
        print('Количество строк: {}'.format(len(sim)))

def count_chars(filename):
    with open(filename) as file:
        s = file.read()
        print('Количество символов:' + ' ' + str(len(s)))

def test(filename):
    count_lines(filename)
    count_chars(filename)

test('file1')
