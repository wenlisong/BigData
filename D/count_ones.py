def read_file(file):
    with open(file, 'r') as f:
        for text in f:
            return text.rstrip()


# make addition using binary string
def binary_add(str_a, str_b):
    return bin(int(str_a, 2) + int(str_b, 2))[2:]

# make subtraction using binary string


def binary_sub(str_a, str_b):
    return bin(int(str_a, 2) - int(str_b, 2))[2:]


class Bucket():
    def __init__(self, count_1s=bin(0)[2:], end_time=None):
        # count_1s is the index number of 2^count_1s, size is loglog(N)=4bits
        self.count_1s = count_1s
        # use binary number denote time, size is log(N)=10 bits
        self.end_time = end_time

    @classmethod
    def merge_buckets(cls, bucket1, bucket2):
        total_1s = bin(int(bucket1.count_1s,2)+1)[2:]
        end_time = bin(min(int(bucket1.end_time, 2), int(bucket2.end_time, 2)))[2:]
        return Bucket(count_1s=total_1s, end_time=end_time)


class BucketList():
    def __init__(self):
        self.N = 1000
        self.list = []

    def get_new_bit(self, char, cur_time):
        if char == '0':
            pass
        elif char == '1':
            bucket = Bucket(end_time=cur_time)
            self.list.append(bucket)
            # update bucket list
            self.update()

    def update(self):
        # delete oldest bucket
        if int(binary_sub(self.list[-1].end_time, self.list[0].end_time), 2) > self.N:
            del self.list[0]
        # check whether the number of bucket with same size greater than 2
        state = False
        while not state:
            state = self.check()

    def check(self):
        count = 0
        for i in range(1, len(self.list)):
            if self.list[i].count_1s == self.list[i-1].count_1s:
                count += 1
                # merge bucket with same size when number of them > 2
                if count >= 2:
                    self.list[i-2] = Bucket.merge_buckets(self.list[i-2], self.list[i-1])
                    del self.list[i-1]
                    break
            else:
                count = 0
        else:
            return True
        return False

    def count_recent_N_1s(self):
        total = 0
        bl = []
        dl = []
        total += int(2**(int(self.list[0].count_1s, 2)) / 2)
        bl.append(self.list[0].count_1s)
        dl.append(2**(int(self.list[0].count_1s, 2)))
        for i in range(1, len(self.list)-1):
            total += 2**(int(self.list[i].count_1s, 2))
            bl.append(self.list[i].count_1s)
            dl.append(2**(int(self.list[i].count_1s, 2)))
        print("Binary number(2^x): {0}".format(bl))
        print("Decimal number: {0}".format(dl))
        return bin(total)[2:]


def main():
    text = read_file('./engg5108_stream_data.txt')
    cur_time = bin(1)[2:]
    bucket_list = BucketList()
    i = 0
    for char in text:
        bucket_list.get_new_bit(char, cur_time)
        cur_time = binary_add(cur_time, '1')
        i+=1
        if i==2000:
            break
    # count number of 1s in the last N bits
    result = bucket_list.count_recent_N_1s()
    print("There are {0} 1s in last 1000 bits.".format(int(result, 2)))


if __name__ == '__main__':
    main()