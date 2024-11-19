class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  

class HashTableWithLinkedLists:
    def __init__(self, size):
        self.size = size
        self.table = {i: None for i in range(size)}  

    def _hash_function(self, key):
        return hash(key) % self.size  
    def insert(self, key, value):
        index = self._hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node  
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value  
                    return
                current = current.next
            if current.key == key:
                current.value = value  
            else:
                current.next = new_node  

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value  
            current = current.next
        return None  

    def delete(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next  
                else:
                    prev.next = current.next  
                return True
            prev = current
            current = current.next
        return False  

# Exemplo
htable = HashTableWithLinkedLists(10)
htable.insert("name", "Alice")
htable.insert("age", 30)
print(htable.search("name"))  
htable.delete("age")
print(htable.search("age"))   
