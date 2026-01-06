# =========================
# HW3 - Watch List
# =========================

# 1) Tabs vs Spaces
# This video shows that small technical preferences can turn into big debates,
# but what really matters is teamwork and consistency in coding standards.

# 2) Python: The Documentary
# Python was created to be simple and readable, which helped it become one of
# the most popular programming languages in the world.

# 3) Andrej Karpathy - Software Is Changing
# Software development is shifting towards AI-driven systems where programmers
# will focus more on ideas and less on low-level implementation details.
def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()
    return len(words[-1])
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)
def reverseWords(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))
def firstUniqChar(s: str) -> int:
    from collections import Counter
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1
def wordFrequency(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    return not (Counter(ransomNote) - Counter(magazine))
def isPalindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]
def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]
values = [10, 15, 40, 50, 67, 70, 83, 90]
search_key = 83

def linear_search(values, key):
    for i in range(len(values)):
        if values[i] == key:
            return i
    return -1


def binary_search(values, key):
    left, right = 0, len(values) - 1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == key:
            return mid
        elif values[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test
print("Linear Search Index:", linear_search(values, search_key))
print("Binary Search Index:", binary_search(values, search_key))

# Time Complexity:
# Linear Search  -> O(n)
# Binary Search  -> O(log n)
