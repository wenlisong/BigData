from itertools import combinations
import pdb

SUPPORT = 100


def read_input(path, separator=None):
    output = []
    with open(path, 'r') as f:
        for line in f:
            output.append(map(int, line.rstrip().split(separator)))
    return output


def get_candi_itemsets(data):
    cnt_list = [0 for _ in range(100001)]
    candidate_itemsets = []
    for line in data:
        for key in line:
            cnt_list[key] += 1

    for key, val in enumerate(cnt_list):
        if val >= SUPPORT:
            candidate_itemsets.append(key)
    return candidate_itemsets


def gen_k_itemsets(itemsets_k_1, k, buckets):
    itemsets_k = []
    for comb in combinations(itemsets_k_1, k):
        cnt = 0
        for bucket in buckets:
            for elem in comb:
                if elem not in bucket:
                    break
            cnt += 1
        if cnt >= SUPPORT:
            itemsets_k.append(comb)
    return itemsets_k


def main():
    buckets = read_input(path='./buckets.txt', separator=',')
    candidate_itemsets = get_candi_itemsets(buckets)
    # generate itemsets of size k
    k = 2
    itemsets_k_1 = candidate_itemsets.copy()
    while True:
        candidate_itemsets_k = gen_k_itemsets(itemsets_k_1, k, buckets)
        if len(candidate_itemsets_k) == 0:
            break
        candidate_itemsets.extend(candidate_itemsets_k)
        pdb.set_trace()
        itemsets_k_1 = candidate_itemsets_k
        k += 1

    with open('top_100_freq_items', 'w') as f:
        for item in candidate_itemsets:
            try:
                f.write(' '.join(map(str, item)) + '\n')
            except TypeError:
                f.write('{0}\n'.format(item))


if __name__ == '__main__':
    main()
