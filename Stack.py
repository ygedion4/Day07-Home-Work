class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


def is_balanced(s: str) -> bool:
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():  # Opening bracket
            stack.push(char)
        elif char in mapping:  # Closing bracket
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False

    return stack.is_empty()


def max_sliding_window_sum(arr: list, k: int) -> int:
    if not arr or k <= 0 or k > len(arr):
        return 0

    q = Queue()
    current_sum = 0

    # Fill initial window of size k
    for i in range(k):
        q.enqueue(arr[i])
        current_sum += arr[i]

    max_sum = current_sum

    # Slide the window across the rest of the array
    for i in range(k, len(arr)):
        # Remove the element going out of the window
        removed = q.dequeue()
        current_sum -= removed

        # Add the new element coming into the window
        q.enqueue(arr[i])
        current_sum += arr[i]

        # Update max_sum
        max_sum = max(max_sum, current_sum)

    return max_sum


def run_tests():
    print("Running Tests...\n")

    # --- Stack Tests ---
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    assert s.size() == 1
    print("✓ Stack basic operations passed.")

    # --- Queue Tests ---
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    assert q.dequeue() == "A"
    assert q.peek() == "B"
    assert q.size() == 1
    print("✓ Queue basic operations passed.")

    # --- Balanced Brackets Tests ---
    assert is_balanced("{[()]}") is True
    assert is_balanced("{[(])}") is False
    assert is_balanced("((()") is False
    assert is_balanced("") is True
    print("✓ Balanced Brackets tests passed.")

    # --- Sliding Window Sum Tests ---
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    # Subarrays of size 3: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6 -> Max = 9
    assert max_sliding_window_sum(arr1, k1) == 9

    arr2 = [1, 2, 3, 4, 5, 6]
    k2 = 2
    # Subarrays: [1,2]=3, [2,3]=5, [3,4]=7, [4,5]=9, [5,6]=11 -> Max = 11
    assert max_sliding_window_sum(arr2, k2) == 11

    print("✓ Maximum Sliding Window Sum tests passed.")
    print("\n🎉 All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
