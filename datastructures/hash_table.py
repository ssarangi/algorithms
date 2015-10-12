"""
The MIT License (MIT)

Copyright (c) <2015> <sarangis>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

"""
Implement a hash table datastructure along with the different collision
resolution techniques.
"""

from random import randint

class KeyDoesntExistError(Exception):
    pass

class HashTable:
    def __init__(self):
        self._table_size = 11
        self._num_occupied = 0
        self._storage = [None] * self._table_size
        self._collision_resolve = [self._linear_probe_get, self._linear_probe_set]

    def _hash_function(self, item):
        return item % self._table_size

    def load_factor(self):
        return self._num_occupied / self._table_size

    def _get_from_storage(self, hash_value):
        return self._storage[hash_value]

    def _set_into_storage(self, hash_value, value):
        self._storage[hash_value] = value

    def _rehash(self, hash):
        return (hash + 3) % self._table_size

    def _linear_probe_set(self, hash, item, value):
        """
        Linear probing is a technique for open addressing collision resolution.
        The hash value is computed and then checked if it is empty or not. If
        it is not empty then a linear scan at the particular hash index starts
        incrementing to the end and circularly beginning back at 0th index to
        find the next empty spot. Once found, the item is set at that location.
        :param hash: Hash value for the probe
        :param item: Key
        :param value: Value
        :return: None
        """
        inserted = False
        while inserted is not True:
            if self._get_from_storage(hash) is None:
                self._storage[hash] = (item, value)
                inserted = True

            if hash >= self._table_size - 1:
                hash = 0
            else:
                hash = self._rehash(hash)

    def _linear_probe_get(self, hash, item):
        found = False
        while found is not True:
            v = self._get_from_storage(hash)
            if v is None or v[0] != item:
                hash = self._rehash(hash)
            else:
                return v

            if hash >= self._table_size - 1:
                hash = 0


    def __getitem__(self, item):
        hash_value = self._hash_function(item)
        v = self._get_from_storage(hash_value)
        if v[0] != item:
            return self._collision_resolve[0](hash_value, item)

        if v == None:
            raise KeyDoesntExistError("Key %s doesn't exist in hash table" % item)

    def __setitem__(self, key, value):
        hash_value = self._hash_function(key)
        if self._get_from_storage(hash_value) is not None:
            self._collision_resolve[1](hash_value, key, value)
        else:
            self._storage[hash_value] = (key,value)

        self._num_occupied += 1

    def get_or_none(self, key):
        hash_value = self._hash_function(key)
        v = self._get_from_storage(hash_value)
        return v

def main():
    h = HashTable()
    # random_numbers = [randint(0, 100) for i in range(0, 100)]
    numbers = [54,26,93,17,77,31,44,55,20]
    for rn in numbers:
        h[rn] = True

    print(h.load_factor())
    print(h[20])

if __name__ == "__main__":
    main()