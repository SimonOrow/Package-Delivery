class HashTable:
    def __init__(self, capacity):
        # Create instance with specified capacity.
        self.capacity = capacity
        self.buckets = [[]] * capacity

    def get_bucket(self, key):
        # Returns bucket from key index.
        key = int(key)
        return self.buckets[key % self.capacity]

    def find_index_with_key(self, bucket, key):
        # Enumerates all buckets finding one with the specified key.
        key = int(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return -1  # Return -1 if not found

    def add(self, key, value):
        # Add to hash table with key and value.
        key = int(key)
        bucket = self.get_bucket(key)
        index = self.find_index_with_key(bucket, key)
        if index != -1:
            # If bucket already exists, and we're simply trying to update the value.
            bucket[index][1] = value
        else:
            # Bucket does not exist, and we want to add a new key/value
            bucket.append([key, value])

    def retrieve(self, key):
        key = int(key)
        bucket = self.get_bucket(key)
        index = self.find_index_with_key(bucket, key)
        if index != -1:
            # Return the bucket
            return bucket[index][1]
        else:
            # Could not find bucket
            return -1

    def remove(self, key):
        key = int(key)
        bucket = self.get_bucket(key)
        index = self.find_index_with_key(bucket, key)
        if index != -1:
            # If index exists, remove the bucket.
            del bucket[index]