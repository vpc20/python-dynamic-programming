import sys


def draw_column_nums(colwidth_arr, left_width):
    print(' ' * left_width + '  ', end='')  # '*' is dummy value because of problem in copy/paste
    for i, width in enumerate(colwidth_arr):
        print(f'{i:^{width + 1}}', end='')  # width + 1 vertical line on the right
    print('')


def draw_top(colwidth_arr, left_width):
    print(' ' * left_width + ' ', end='')
    print('┌', end='')
    for i, width in enumerate(colwidth_arr):
        if i == len(colwidth_arr) - 1:
            print(('─' * width), end='')
        else:
            print(('─' * width + '┬'), end='')
    print('┐')


def draw_mid(colwidth_arr, left_width):
    print(' ' * left_width + ' ', end='')
    print('├', end='')
    for i, width in enumerate(colwidth_arr):
        if i == len(colwidth_arr) - 1:
            print(('─' * width), end='')
        else:
            print(('─' * width + '┼'), end='')
    print('┤')


def draw_bottom(colwidth_arr, left_width):
    print(' ' * left_width + ' ', end='')
    print('└', end='')
    for i, width in enumerate(colwidth_arr):
        if i == len(colwidth_arr) - 1:
            print(('─' * width), end='')
        else:
            print(('─' * width + '┴'), end='')
    print('┘')


def draw_data(arr, colwidth_arr, row, left_width):
    print(f'{row:>{left_width}} │', end='')
    for i, e in enumerate(arr):
        if isinstance(e, list) or isinstance(e, bool):  # convert list or boolean to strings
            e = str(e)
        if isinstance(e, str):
            print(f' {e:{colwidth_arr[i] - 1}}│', end='')
        else:
            print(f'{e:>{colwidth_arr[i] - 1}} │', end='')  # right-justify numbers
    print('')


def ascii_box1(arr):
    colwidth_arr = []
    for col in range(len(arr[0])):
        maxlencol = -sys.maxsize
        for row in range(len(arr)):
            maxlencol = max(maxlencol, len(str(arr[row][col])) + 2)  # add 2 spaces, 1 space on each side
        colwidth_arr.append(maxlencol)

    left_width = len(str(len(arr)))

    draw_column_nums(colwidth_arr, left_width)
    draw_top(colwidth_arr, left_width)
    for i in range(len(arr)):
        draw_data(arr[i], colwidth_arr, i, left_width)
        if i != len(arr) - 1:
            draw_mid(colwidth_arr, left_width)
    draw_bottom(colwidth_arr, left_width)
    print('Paste the ascii box in the first column of target window.')


if __name__ == '__main__':
    # ascii_box1([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    #             [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],
    #             [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44], [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    #             [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66], [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77],
    #             [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88], [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],
    #             [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110], [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]])
    # ascii_box1([['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al'],
    #             ['ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl'],
    #             ['ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl'],
    #             ['da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl'],
    #             ['ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el'],
    #             ['fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl'],
    #             ['ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl'],
    #             ['ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh', 'hi', 'hj', 'hk', 'hl'],
    #             ['ia', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'ih', 'ii', 'ij', 'ik', 'il'],
    #             ['ja', 'jb', 'jc', 'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl'],
    #             ['ka', 'kb', 'kc', 'kd', 'ke', 'kf', 'kg', 'kh', 'ki', 'kj', 'kk', 'kl'],
    #             ['la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll']])
    # ascii_box1([[[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #             [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #             [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #             [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #             [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]]])

    ascii_box1([[[], ['r'], ['rr'], ['rrr']], [['d'], ['rr', 'dd'], ['rrr', 'rrd', 'ddd'], ['rrrr', 'rrrd', 'rrdd', 'dddd']], [['dd'], ['rrr', 'ddr', 'ddd'], ['rrrr', 'rrdr', 'dddr', 'rrrd', 'ddrd', 'dddd'], ['rrrrr', 'rrrdr', 'rrddr', 'ddddr', 'rrrrd', 'rrdrd', 'dddrd', 'rrrdd', 'ddrdd', 'ddddd']], [['ddd'], ['rrrr', 'ddrr', 'dddr', 'dddd'], ['rrrrr', 'rrdrr', 'dddrr', 'rrrdr', 'ddrdr', 'ddddr', 'rrrrd', 'ddrrd', 'dddrd', 'ddddd'], ['rrrrrr', 'rrrdrr', 'rrddrr', 'ddddrr', 'rrrrdr', 'rrdrdr', 'dddrdr', 'rrrddr', 'ddrddr', 'dddddr', 'rrrrrd', 'rrdrrd', 'dddrrd', 'rrrdrd', 'ddrdrd', 'ddddrd', 'rrrrdd', 'ddrrdd', 'dddrdd', 'dddddd']]])
    ascii_box1([[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 1, 5, 6, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10], [0, 1, 5, 8, 10]])