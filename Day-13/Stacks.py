class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the size of the stack"""
        return len(self.items)

# ✅ Run this to test
if __name__ == "__main__":
    stack = Stack()
    stack.push("Python")
    stack.push("Java")
    stack.push("C++")
    print("Top:", stack.peek())     # C++
    print("Pop:", stack.pop())      # C++
    print("Top after pop:", stack.peek())  # Java
