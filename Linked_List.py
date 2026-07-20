class Node:
    """A node in a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list implementation."""
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """Add a new node to the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """Add a new node to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Delete the first occurrence of value in the list."""
        if not self.head:
            return False

        # If head contains the value
        if self.head.value == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        
        return False  # Value not found

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev

    def has_cycle(self):
        """Detect if the linked list contains a cycle (Floyd's Cycle-Finding Algorithm)."""
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def __iter__(self):
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        """String representation of the list."""
        nodes = []
        current = self.head
        
        # Handle potential cycle in string representation to prevent infinite loops
        visited = set()
        while current:
            if id(current) in visited:
                nodes.append("... (Cycle detected)")
                break
            visited.add(id(current))
            nodes.append(str(current.value))
            current = current.next

        return " -> ".join(nodes) if nodes else "Empty LinkedList"


# ---------------------------------------------------------
# Test Cases
# ---------------------------------------------------------

def run_tests():
    print("Testing LinkedList Implementation...\n")

    # Test 1: Empty list representation
    ll = LinkedList()
    assert repr(ll) == "Empty LinkedList", "Test 1 Failed"
    print("✓ Test 1 Passed: Empty list representation")

    # Test 2: Prepend elements
    ll.prepend(10)
    ll.prepend(20)
    assert list(ll) == [20, 10], "Test 2 Failed"
    print("✓ Test 2 Passed: Prepend elements")

    # Test 3: Append elements
    ll.append(30)
    ll.append(40)
    assert list(ll) == [20, 10, 30, 40], "Test 3 Failed"
    print("✓ Test 3 Passed: Append elements")

    # Test 4: Iteration (using __iter__)
    elements = [item for item in ll]
    assert elements == [20, 10, 30, 40], "Test 4 Failed"
    print("✓ Test 4 Passed: Iteration (__iter__)")

    # Test 5: Delete existing element
    deleted = ll.delete(10)
    assert deleted is True, "Test 5 Failed"
    assert list(ll) == [20, 30, 40], "Test 5 Failed"
    print("✓ Test 5 Passed: Delete middle element")

    # Test 6: Delete head element & non-existing element
    ll.delete(20)
    assert list(ll) == [30, 40], "Test 6 Failed"
    assert ll.delete(999) is False, "Test 6 Failed (Non-existing value)"
    print("✓ Test 6 Passed: Delete head & non-existing value")

    # Test 7: Reverse list
    ll.reverse()
    assert list(ll) == [40, 30], "Test 7 Failed"
    print("✓ Test 7 Passed: Reverse list")

    # Test 8: Has cycle (No cycle test)
    assert ll.has_cycle() is False, "Test 8 Failed"
    print("✓ Test 8 Passed: Has cycle (False)")

    # Test 9 (Bonus): Has cycle (With cycle test)
    # Manually creating a cycle for testing
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    cycle_ll = LinkedList()
    cycle_ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Points back to head, creating a cycle

    assert cycle_ll.has_cycle() is True, "Test 9 Failed"
    print("✓ Test 9 Passed: Has cycle (True)")

    print("\n🎉 All tests passed successfully!")


if __name__ == "__main__":
    run_tests()