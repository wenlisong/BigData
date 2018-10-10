import sys
from operator import itemgetter
from itertools import groupby


def read_mapper_output(file):
    for line in file:
        yield line.rstrip().split('\t', 1)


def main():
    user_movie = {}  # {'user':[[like], [unlike]]}
    pre_user_id = None
    top_score = [0 for _ in range(100)]
    min_score = 0

    def print_jaccard_distance(last_user_id):
        nonlocal top_score
        nonlocal min_score
        nonlocal user_movie
        for uid, val in user_movie.items():
            if uid != last_user_id:
                numerator = len(user_movie[uid][0].intersection(user_movie[last_user_id][0]).union(
                    user_movie[uid][1].intersection(user_movie[last_user_id][1])
                ))
                denominator = len(user_movie[uid][0].union(user_movie[last_user_id][0]).union(
                    user_movie[uid][1].union(user_movie[last_user_id][1])
                ))
                result = numerator / denominator
                if result > min_score:
                    top_score[top_score.index(min_score)] = result
                    min_score = min(top_score)
                    print("\"{0}\" \"{1}\"\t{2}".format(uid, last_user_id, result))

    data = read_mapper_output(sys.stdin)
    for user_id, group in groupby(data, itemgetter(0)):
        if pre_user_id:
            print_jaccard_distance(pre_user_id)

        user_movie[user_id] = [set([]), set([])]
        for values in group:
            movie_id, is_like = values[1].split('\t')
            if is_like == 'T':
                user_movie[user_id][0].add(movie_id)
            else:
                user_movie[user_id][1].add(movie_id)

        pre_user_id = user_id
    print_jaccard_distance(pre_user_id)


if __name__ == '__main__':
    main()
