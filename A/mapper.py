import sys


def read_input(file):
    for line in file:
        line = line.rstrip().split(',')[:3]
        if line[0] == 'userId':
            continue

        if 0.5 <= float(line[2]) <= 2.5:
            line[2] = 'F'
        else:
            line[2] = 'T'  # like
        yield line


def main():
    data = read_input(sys.stdin)

    for line in data:
        print('{0}\t{1}\t{2}'.format(line[0], line[1], line[2]))


if __name__ == '__main__':
    main()
