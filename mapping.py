class HashNode:
    """Class to represent a node in the linked list (for chaining)."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size=10):
        """Initialize the hash map with a given size (number of buckets)."""
        self.size = size
        self.buckets = [None] * self.size  # List of buckets (each bucket will hold a linked list)
    
    def _hash(self, key):
        """Private method to hash the key to an index."""
        return hash(key) % self.size  # Use Python's built-in hash function and take modulo to get the index
    
    def put(self, key, value):
        """Insert or update the key-value pair in the hash map."""
        index = self._hash(key)  # Hash the key to get the bucket index
        head = self.buckets[index]
        
        # Check if the key already exists in the linked list
        current = head
        while current is not None:
            if current.key == key:
                current.value = value  # Update the value if key exists
                return
            current = current.next
        
        # If the key doesn't exist, insert it at the beginning of the linked list
        new_node = HashNode(key, value)
        new_node.next = head
        self.buckets[index] = new_node  # Set the new node as the head of the list

    def get(self, key):
        """Retrieve the value associated with the given key."""
        index = self._hash(key)
        head = self.buckets[index]
        
        # Traverse the linked list to find the key
        current = head
        while current is not None:
            if current.key == key:
                return current.value  # Return the value if key is found
            current = current.next
        
        return None  # Return None if the key is not found

    def remove(self, key):
        """Remove the key-value pair from the hash map."""
        index = self._hash(key)
        head = self.buckets[index]
        prev = None
        current = head
        
        # Traverse the linked list to find the key
        while current is not None:
            if current.key == key:
                if prev is None:  # The node to remove is the head node
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next  # Bypass the current node
                return True  # Return True if the key was found and removed
            prev = current
            current = current.next
        
        return False  # Return False if the key was not found

    def __str__(self):
        """Return a string representation of the hash map."""
        output = []
        for i, bucket in enumerate(self.buckets):
            if bucket is not None:
                chain = []
                current = bucket
                while current:
                    chain.append(f"{current.key}: {current.value}")
                    current = current.next
                output.append(f"Bucket {i}: " + " -> ".join(chain))
            else:
                output.append(f"Bucket {i}: Empty")
        return "\n".join(output)

# Example usage
if __name__ == "__main__":
    hash_map = HashMap()

    # Insert key-value pairs
    hash_map.put("apple", 10)
    hash_map.put("banana", 20)
    hash_map.put("grape", 30)
    
    # Retrieve values
    print(f"Value for 'apple': {hash_map.get('apple')}")
    print(f"Value for 'banana': {hash_map.get('banana')}")
    print(f"Value for 'orange' (non-existent): {hash_map.get('orange')}")

    # Update a value
    hash_map.put("apple", 15)
    print(f"Updated value for 'apple': {hash_map.get('apple')}")
    
    # Remove a key
    hash_map.remove("banana")
    print(f"Value for 'banana' after removal: {hash_map.get('banana')}")
    
    # Print the hash map structure
    print("\nHashMap Structure:")
    print(hash_map)
