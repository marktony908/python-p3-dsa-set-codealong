class MySet:
    def __init__(self, enumerable=None):
        """Initialize the MySet with an optional list of elements."""
        self.dictionary = {}
        if enumerable is not None:
            for value in enumerable:
                self.dictionary[value] = True

    def has(self, value):
        """Check if the value is in the set."""
        return value in self.dictionary

    def __str__(self):
        """Return a string representation of the set."""
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{{", ".join(set_list)}}}'

    def add(self, value):
        """Add a value to the set if it's not already present."""
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """Remove a value from the set if it exists."""
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """Return the number of elements in the set."""
        return len(self.dictionary)

    def clear(self):
        """Remove all elements from the set."""
        self.dictionary.clear()
        return self
