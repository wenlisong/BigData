import sys
from operator import itemgetter
from itertools import groupby


# read data from mapper by generator
def read_mapper_output(file):
    for line in file:
        yield line.rstrip().split('\t', 1)

def read_total_movie():
    with open('user_total_movie.txt', 'r') as f:
        data = {}
        for line in f:
            line = line.rstrip().split(' ')
            data[line[0]] = int(line[1])
        return data

def main():
    def print_jaccard_distance():
        nonlocal top_score
        nonlocal min_score
        nonlocal new_data
        nonlocal user_total_movie
        for user_pair, cnt in new_data.items():
            numerator = cnt
            user1, user2 = user_pair.split(' ')
            denominator = user_total_movie[user1] + user_total_movie[user2] - cnt
            result = numerator / denominator
            if result > min_score:
                top_score[top_score.index(min_score)] = result
                min_score = min(top_score)
                print("\"{0}\" \"{1}\"\t{2}".format(user1, user2, result))

    top_score = [0 for _ in range(100)]
    min_score = 0
    user_total_movie = read_total_movie()
    data = read_mapper_output(sys.stdin)
    new_data = {}
    for user_pair, group in groupby(data, itemgetter(0)):
        try:
            new_data[user_pair] += 1
        except:
            new_data[user_pair] = 1

    print_jaccard_distance()


if __name__ == '__main__':
    main()
