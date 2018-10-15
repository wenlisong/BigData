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
            candidate_itemsets.append([key])
    return candidate_itemsets


def gen_k_itemsets(itemsets_k_1, buckets):
    itemsets_k = []
    # elem list without repetition
    elem_list = set([elem for itemset in itemsets_k_1 for elem in itemset])

    # generate all candidate itemsets
    tmp_itemsets = []
    for itemset in itemsets_k_1:
        for elem in elem_list:
            if elem > itemset[-1]:
                tmp_itemsets.append(itemset + [elem])

    for comb in tmp_itemsets:
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
    itemsets_k_1 = candidate_itemsets
    with open('A.txt', 'w') as f:
        # output k = 1
        for item in itemsets_k_1:
            f.write(' '.join(map(str, item)) + '\n')
        while True:
            candidate_itemsets_k = gen_k_itemsets(itemsets_k_1, buckets)
            if len(candidate_itemsets_k) == 0:
                break
            # output k >= 2
            for item in candidate_itemsets_k:
                f.write(' '.join(map(str, item)) + '\n')
            itemsets_k_1 = candidate_itemsets_k

            k += 1


if __name__ == '__main__':
    main()
