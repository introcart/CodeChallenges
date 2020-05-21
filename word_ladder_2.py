"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from typing import List
from collections import deque
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return_list = []
        wordList = set(wordList)
        queue = deque(beginWord)

        visited = set()
        temp_list = []

        while queue:
            word = queue.popleft()

            if word == endWord:
                return_list.append(temp_list)
                temp_list.clear()

            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    new_word = word[:i] + char + word[i + 1:]


if __name__ == "__main__":
    obj = Solution()
    begin, end = "hit", "cog"
    expected = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]

    actual = obj.findLadders()

    assert expected == actual, "Actual returned values - {0}".format(actual)
