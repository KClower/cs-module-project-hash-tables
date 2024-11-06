class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY if MIN_CAPACITY > capacity else capacity
        self.storage = [None] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.

        Load factor = number of items in the table / number of slots in array
        load factor = 8/8 = 1.0
        load factor = 16/8 = 2.0

        if load factor is greater than 0.7:
            rehash, doubling the size of the table
        """
        # Your code here
        return self.size / self.capacity
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for character in key:
            # ord(character) simply returns the unicode rep of the
            # character 
            hash = (( hash << 5) + hash) + ord(character)
        # Note to clamp the value so that the hash is 
        # related to the power of 2
        return hash & 0xFFFFFFFF
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
    

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.

        Get the index for the key.
        Search the linked list at that index for the key.
        If the key is found, overwrite the value stored there.
        Else insert the key and value at the head of the list at that index.
        Make a counter to keep track of values stored for load factor.
        """
        # Your code here
        index = self.hash_index(key)
        # create node
        new_node = HashTableEntry(key, value)
        # if index None insert node else travrse linked list to the end append new node
        if self.storage[index] is None:
            self.storage[index] = new_node
            self.size += 1
        else:
            existing_node = self.storage[index]
            while existing_node is not None:
                if existing_node.key == key:
                    existing_node.value = value
                    return
                if existing_node.next is None:
                    break
                existing_node = existing_node.next

            existing_node.next = new_node
            self.size += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
            
      

        



    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.

        Get the index for the key.
        Search the linked list at the index for the key.
        If found, delete it, and return it.
        Else return None.
        Update counter.
        """
        # Your code here
        index = self.hash_index(key)
        head = self.storage[index]

        if head is None:
            print(f"Key of {key} not found.") 
            return None 
        
        if head.key == key:
            self.storage[index] = head.next
            self.size -= 1
        else:
            prev_pointer = head
            current_pointer = head.next
            while current_pointer is not None:
                if current_pointer.key == key:
                    prev_pointer.next = current_pointer.next
                    self.size -= 1
                    break
                prev_pointer = prev_pointer.next
                current_pointer = current_pointer.next
            else:
                print(f"Key {key} not found.")
                return None
        if self.get_load_factor() < 0.2 and self.capacity > MIN_CAPACITY:
            self.resize(max(MIN_CAPACITY, self.capacity // 2))
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.

        Get the index for the key.
        Search the linked list at that index for the key.
        If found, return the value.
        Else return none.
        """
        # Your code here
        index = self.hash_index(key)
        current_entry = self.storage[index]

        while current_entry is not None:
            if current_entry.key == key:
                return current_entry.value
            current_entry = current_entry.next
        return None

    

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        self.size = 0

        for entry in old_storage:
            current_entry = entry
            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
