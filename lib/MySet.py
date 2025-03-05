class MySet:
    def __init__(self, enumerable=[]):
        """
        Initialize the set using a dictionary to store unique values.
        """
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, value):
        """
        Check if the value exists in the set.
        """
        return value in self.dictionary
    
    def add(self, value):
        """
        Add a value to the set.
        """
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        """
        Remove a value from the set if it exists.
        """
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        """
        Return the number of elements in the set.
        """
        return len(self.dictionary)
    
    def clear(self):
        """
        Remove all elements from the set.
        """
        self.dictionary = {}
        return self
    
    def __str__(self):
        """
        Return a formatted string representation of the set.
        """
        return f"MySet: {set(self.dictionary.keys())}"

if __name__ == "__main__":
    my_set = MySet([1, 2, 3, 3])
    print(my_set.has(2))  # True
    print(my_set.has(4))  # False
    my_set.add(4)
    print(my_set.has(4))  # True
    my_set.delete(2)
    print(my_set.has(2))  # False
    print(my_set.size())  # 3
    my_set.clear()
    print(my_set.size())  # 0


