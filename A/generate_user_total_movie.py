import sys


# read data by generator
def read_input(file):
    with open('./ml-20m/ratings.csv', 'r') as f:
        for line in f:
            line = line.rstrip().split(',')[:3]
            if line[0] == 'userId':
                continue

            yield line[0]  # 0:userid, 1:movieid, 2:rating

def main():
    data = read_input(sys.stdin)
    user_total_movie = {}
    for user_id in data:
        # count how many movies user watched
        try:
            user_total_movie[user_id] += 1
        except:
            user_total_movie[user_id] = 1
    with open('user_total_movie.txt', 'w') as f:
        for key, val in user_total_movie.items():
            f.write("%s %s\n" %(key, val))




if __name__ == '__main__':
    main()
