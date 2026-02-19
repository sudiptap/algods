# Trie (Prefix Tree)

## When to Use
- **Prefix matching** and autocomplete
- Word search and dictionary problems
- Storing and querying strings efficiently
- Keywords: "prefix", "dictionary", "word search", "autocomplete", "starts with"

## Core Idea
A tree where each node represents a character. Paths from root to nodes spell out prefixes. Mark end-of-word nodes.

## Template
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

## Complexity
- Insert/Search: O(m) where m = word length
- Space: O(total characters across all words)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 208 | Implement Trie | Medium | Core implementation | |
| 211 | Design Add and Search Words | Medium | Trie + DFS | |
| 212 | Word Search II | Hard | Trie + Backtracking | |
| 336 | Palindrome Pairs | Hard | Trie | |
| 421 | Maximum XOR of Two Numbers | Medium | Bit Trie | |
| 648 | Replace Words | Medium | Prefix matching | |
| 720 | Longest Word in Dictionary | Medium | Trie + BFS | |

## Tips
- Use a dictionary for children (flexible) or a fixed-size array of 26 for lowercase letters (faster)
- For "word search on a board" problems, combine Trie with backtracking
- Can store additional data at nodes (counts, word references)
