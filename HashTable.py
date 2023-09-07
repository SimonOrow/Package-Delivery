class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [[]] * capacity

    def get_bucket(self, key):
        key = int(key)
        return self.buckets[key % self.capacity]

    def find_index_with_key(self, bucket, key):
        key = int(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return -1

    def add(self, key, value):
        key = int(key)
        bucket = self.get_bucket(key)
        index = self.find_index_with_key(bucket, key)
        if index != -1:
            bucket[index][1] = value
        else:
            bucket.append([key, value])

    def retrieve(self, key):
        key = int(key)
        bucket = self.get_bucket(key)
        index = self.find_index_with_key(bucket, key)
        if index != -1:
            return bucket[index][1]
        else:
            return -1

    def remove(self, key):
        key = int(key)
        bucket = self.get_bucket(key)
        index = self.find_index_with_key(bucket, key)
        if index != -1:
            del bucket[index]