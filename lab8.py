class CustomSet:
    def __init__(self):
        """Initializes an empty CustomSet"""
        self._min_buckets = 8
        self._n_buckets = 8
        self._len = 0
        self._L = [[] for i in range(self._n_buckets)]

    def __len__(self):
        """Returns the number of items in CustomSet"""
        return self._len

    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        return hash(item) % self._n_buckets

    def __contains__(self, item):
        """Returns True (False) if item is (is not) in the CustomSet"""
        bucket_index = self._find_bucket(item)
        return item in self._L[bucket_index]

    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored - they do not increase the length, but they do not raise an error."""
        if item in self:
            return  # Item is already in the set
        
        bucket_index = self._find_bucket(item)
        self._L[bucket_index].append(item)
        self._len += 1

        # Rehash if necessary
        if self._len >= 2 * self._n_buckets:
            self._rehash(2 * self._n_buckets)

    def remove(self, item):
        """Removes item from CustomSet. Removing an item not in CustomSet should raise a KeyError."""
        if item not in self:
            raise KeyError(f"{item} not found in the CustomSet")
        
        bucket_index = self._find_bucket(item)
        self._L[bucket_index].remove(item)
        self._len -= 1

        # Rehash if necessary
        if self._len <= 0.5 * self._n_buckets and 0.5 * self._n_buckets >= self._min_buckets:
            self._rehash(self._n_buckets // 2)

    def _rehash(self, new_buckets):
        """Rehashes every item from a hash table with n_buckets to one with new_buckets."""
        new_L = [[] for i in range(new_buckets)]

        for bucket in self._L:
            for item in bucket:
                new_bucket_index = hash(item) % new_buckets
                new_L[new_bucket_index].append(item)

        self._L = new_L
        self._n_buckets = new_buckets
