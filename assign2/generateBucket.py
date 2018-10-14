ITEM_BUCKET_COUNT = 10000

bucket = [[] for _ in range(ITEM_BUCKET_COUNT)]


with open('buckets.txt', 'w') as f:
    for b in range(1, ITEM_BUCKET_COUNT+1):
        bucket = ''
        for i in range(1, b + 1):
            if b % i == 0:
                bucket += '{0},'.format(i)
        f.writelines(bucket.rstrip(',')+'\n')

