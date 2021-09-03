

class HashNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:
    """
    This is a simplified hash map
    that doesn't use a good randomized
    hashing function, which brings
    down it's time complexity a bit
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.number_of_hash_nodes = 1000
        self.hash_nodes = [None] * self.number_of_hash_nodes

    def put(self, key: int, value: int):
        """
        value will always be non-negative.
        """
        index: int = key % self.number_of_hash_nodes
        if self.hash_nodes[index] is None:
            self.hash_nodes[index] = HashNode(key, value)
        else:
            current = self.hash_nodes[index]
            while True:
                if current.pair[0] == key:
                    current.pair = (key, value)  # update
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = HashNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.number_of_hash_nodes
        current = self.hash_nodes[index]
        while current is not None:
            if current.pair[0] == key:
                return current.pair[1]
            else:
                current = current.next
        return -1

    def remove(self, key: int):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.number_of_hash_nodes
        current: HashNode = self.hash_nodes[index]
        previous = current
        if current is None:
            return
        if current.pair[0] == key:
            self.hash_nodes[index] = current.next
        else:
            current = current.next
            while current:
                if current.pair[0] == key:
                    previous.next = current.next
                    break
                else:
                    current, previous = current.next, previous.next


if __name__ == '__main__':
    hash_map = MyHashMap()
    method_calls = ["remove", "put", "remove", "remove", "get", "remove", "put", "get", "remove", "put", "put", "put", "put", "put", "put", "put", "put",
                               "put", "put", "put", "remove", "put", "put", "get", "put", "get", "put", "put", "get", "put", "remove", "remove", "put", "put", "get", "remove",
                               "put", "put", "put", "get", "put", "put", "remove", "put", "remove", "remove", "remove", "put", "remove", "get", "put", "put", "put", "put",
                               "remove", "put", "get", "put", "put", "get", "put", "remove", "get", "get", "remove", "put", "put", "put", "put", "put", "put", "get", "get",
                               "remove", "put", "put", "put", "put", "get", "remove", "put", "put", "put", "put", "put", "put", "put", "put", "put", "put", "remove", "remove",
                               "get", "remove", "put", "put", "remove", "get", "put", "put"]
    key_value_pairs = [[27], [65, 65], [19], [0], [18], [3], [42, 0], [19], [42], [17, 90], [31, 76], [48, 71], [5, 50], [7, 68], [73, 74], [85, 18], [74, 95],
                                        [84, 82], [59, 29], [71, 71], [42], [51, 40], [33, 76], [17], [89, 95], [95], [30, 31], [37, 99], [51], [95, 35], [65], [81], [61, 46],
                                        [50, 33], [59], [5], [75, 89], [80, 17], [35, 94], [80], [19, 68], [13, 17], [70], [28, 35], [99], [37], [13], [90, 83], [41], [50],
                                        [29, 98], [54, 72], [6, 8], [51, 88], [13], [8, 22], [85], [31, 22], [60, 9], [96], [6, 35], [54], [15], [28], [51], [80, 69], [58, 92],
                                        [13, 12], [91, 56], [83, 52], [8, 48], [62], [54], [25], [36, 4], [67, 68], [83, 36], [47, 58], [82], [36], [30, 85], [33, 87], [42, 18],
                                        [68, 83], [50, 53], [32, 78], [48, 90], [97, 95], [13, 8], [15, 7], [5], [42], [20], [65], [57, 9], [2, 41], [6], [33], [16, 44], [95, 30]]

    for index, method_call in enumerate(method_calls):
        if method_call == "remove":
            key = key_value_pairs[index][0]
            print(hash_map.remove(key))
        elif method_call == "put":
            key, value = key_value_pairs[index]
            print(hash_map.put(key, value))
        elif method_call == "get":
            key = key_value_pairs[index][0]
            print(hash_map.get(key))
