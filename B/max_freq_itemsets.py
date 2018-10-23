import multiprocessing

SUPPORT = 20


def read_input(path, separator=None):
    output = []
    with open(path, 'r') as f:
        for line in f:
            output.append(list(map(int, line.rstrip().split(separator))))
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


def get_comb(combs, buckets):
    res = []
    for comb in combs:
        cnt = 0
        for bucket in buckets:
            for elem in comb:
                if elem not in bucket:
                    break
            else:
                cnt += 1
        if cnt >= SUPPORT:
            res.append(comb)
    return res


def gen_k_itemsets(itemsets_k_1, buckets):
    # elem list without repetition
    elem_list = set([elem for itemset in itemsets_k_1 for elem in itemset])

    # generate all candidate itemsets
    tmp_itemsets = []
    for itemset in itemsets_k_1:
        for elem in elem_list:
            if elem > itemset[-1]:
                tmp_itemsets.append(itemset + [elem])

    cpu_cnt = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_cnt)
    result = []
    gap = int(len(tmp_itemsets) / cpu_cnt)
    if gap == 0:
        gap = 1
    for i in range(0, len(tmp_itemsets), gap):
        result.append(pool.apply_async(get_comb, args=(tmp_itemsets[i:i + gap], buckets,)))
    pool.close()
    pool.join()
    itemsets_k = []
    for res in result:
        itemsets_k.extend(res.get())

    return itemsets_k


def main():
    buckets = read_input(path='./buckets.txt', separator=',')
    candidate_itemsets = get_candi_itemsets(buckets)
    # generate itemsets of size k
    k = 2
    itemsets_k_1 = candidate_itemsets
    while True:
        candidate_itemsets_k = gen_k_itemsets(itemsets_k_1, buckets)
        if len(candidate_itemsets_k) == 0:
            with open('B.txt', 'w') as f:
                # output
                for item in itemsets_k_1:
                    f.write(' '.join(map(str, item)) + '\n')
            break
        itemsets_k_1 = candidate_itemsets_k
        k += 1


if __name__ == '__main__':
    main()
