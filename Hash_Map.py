def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Hash Map Strategy:
    We iterate through the list while maintaining a hash map storing {number: index}.
    For each number x, we calculate its required complement = target - x.
    If the complement exists in the hash map, we found the pair and return their indices.
    Otherwise, we add the current number x and its index to the map.
    """
    seen = {}  # Map value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # Return empty list if no pair is found


def is_anagram(s: str, t: str) -> bool:
    """
    Hash Map Strategy:
    First check if both strings have the same length; if not, return False.
    We build a frequency map of characters in string 's'.
    Then, we iterate through string 't' and decrement the character counts.
    If a character in 't' is not in the map or its count drops below 0, return False.
    If the loop finishes, all frequencies matched and we return True.
    """
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
    """
    Hash Map Strategy:
    Pass 1: Count frequency of each character in string 's' using a hash map.
    Pass 2: Iterate through string 's' with indices and check character frequencies.
    The first character with a frequency of 1 is our answer, so return its index.
    If no unique character is found, return -1.
    """
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
