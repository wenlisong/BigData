import sys
from operator import itemgetter
from itertools import groupby


# read data by generator
def read_input(file):
    for line in file:
        line = line.rstrip().split(',')[:3]
        if line[0] == 'userId':
            continue

        if 0.5 <= float(line[2]) <= 2.5:
            line[2] = 'F'
        else:
            line[2] = 'T'  # like
        yield line  # 0:userid, 1:movieid, 2:rating

# user: movie-rating --> movie: user-rating --> user1-user2: rating-movie
# Jaccard Dis = (A intersection B)/(A union B)
def main():
    data = read_input(sys.stdin)
    data = sorted(data, key=lambda x: x[1])
    movie_user_rating = {}
    for movie_id, group in groupby(data, itemgetter(1)):
        movie_user_rating[movie_id] = [[],[]]
        for values in group:
            movie_user_rating[movie_id][0].append(values[0])
            movie_user_rating[movie_id][1].append(values[2])

    for movie_id, vals in movie_user_rating.items():
        # print(movie_id, vals)
        if len(vals[0])>1:
            for i in range(1,len(vals[0])):
                for j in range(i):
                    if vals[1][i] == vals[1][j]:
                        print("{0} {1}\t1".format(vals[0][i],vals[0][j]))



if __name__ == '__main__':
    main()
