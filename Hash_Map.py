def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # Map value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # Return empty list if no pair is found


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_counts = {}

    # Count character frequencies in s
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Subtract frequencies using characters in t
    for char in t:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True


def first_uniq_char(s: str) -> int:
    char_counts = {}

    # Pass 1: Build frequency map
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Pass 2: Find the first character with a count of 1
    for index, char in enumerate(s):
        if char_counts[char] == 1:
            return index

    return -1


def run_tests():
    print("Running Tests...\n")

    # --- Two Sum Tests ---
    print("Testing Two Sum...")
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("✓ Two Sum passed all test cases!")

    # --- Is Anagram Tests ---
    print("\nTesting Is Anagram...")
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("listen", "silent") is True
    assert is_anagram("a", "ab") is False
    print("✓ Is Anagram passed all test cases!")

    # --- First Unique Character Tests ---
    print("\nTesting First Unique Character...")
    assert first_uniq_char("leetcode") == 0
    assert first_uniq_char("loveleetcode") == 2
    assert first_uniq_char("aabb") == -1
    print("✓ First Unique Character passed all test cases!")

    print("\n🎉 All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
