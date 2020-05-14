# Implement Trie (Prefix Tree)
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

import testlib
from typing import Dict, Optional


class Trie:
    def __init__(self):
        self.value: Optional[str] = None
        self.children: Dict[Optional[str], Optional[Trie]] = {}

    def insert(self, word: str) -> None:
        if not word:
            if None not in self.children:
                self.children[None] = None
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
            self.children[word[0]].value = word[0]
        self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return None in self.children
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        return False


if __name__ == "__main__":

    def example_test(t: testlib.unittest.TestCase):
        trie = Trie()
        trie.insert("apple")
        t.assertEqual(trie.search("apple"), True)
        t.assertEqual(trie.search("app"), False)
        t.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        t.assertEqual(trie.search("app"), True)

    testlib.run(lambda t, tc: tc(t), [example_test])
