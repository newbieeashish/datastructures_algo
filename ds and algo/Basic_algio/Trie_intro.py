'''Trie
You've learned about Trees and Binary Search Trees. In this notebook, you'll learn about a new type of Tree called Trie. Before we dive into the details, let's talk about the kind of problem Trie can help with.

Let's say you want to build software that provides spell check. This software will only say if the word is valid or not. It doesn't give suggested words. From the knowledge you've already learned, how would you build this?

The simplest solution is to have a hashmap of all known words. It would take O(1) to see if a word exists, but the memory size would be O(n*m), where n is the number of words and m is the length of the word. Let's see how a Trie can help decrease the memory usage while sacrificing a little on performance.'''

#Let's look at a basic Trie with the following words: "a", "add", and "hi"


basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))


'''
You can lookup a word by checking if word_end is True after traversing all the 
 in the word. Let's look at the word "hi". The first letter is "h", so you would 
 call basic_trie['h']. The second letter is "i", so you would call 
 basic_trie['h']['i']. Since there's no more letters left, you would see if this
  is a valid word by getting the value of word_end. Now you have 
  basic_trie['h']['i']['word_end'] with True or False if the word exists.

In basic_trie, words "a" and "add" overlapp. This is where a Trie saves memory. 
Instead of having "a" and "add" in different cells, their characters treated like
es in a tree. Let's see how we would check if a word exists in basic_trie'''


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie
    
    for char in word:
        if char not in current_node:
            return False
        
        current_node = current_node[char]
    
    return current_node['word_end']


# Test words
test_words = ['ap', 'add']
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


'''Trie Using a Class¶
Just like most tree data structures, let's use classes to build the Trie. 
Implement two functions for the Trie class below. Implement add to add a word to 
the Trie. Implement exists to return True if the word exist in the trie and False
 the word doesn't exist in the trie'''


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """

        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char] = TrieNode()
                node = node.children[char]
                node.is_word = True
            else:
                node.children[char] = TrieNode()
                node = node.children[char]

        pass

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                try:
                    node = node.children[char]
                    return node.is_word
                except KeyError:
                    return False
            else:
                try:
                    node = node.children[char]
                except KeyError:
                    return False

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


'''

Trie using Defaultdict (Optional)
This is an optional section. Feel free to skip this and go to the next section of
 the classroom.

A cleaner way to build a trie is with a Python default dictionary. 
The following TrieNod class is using collections.defaultdict instead of a 
normal dictionary.'''


import collections


class TrieNode1:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie1(object):
    def __init__(self):
        self.root = TrieNode1()

    def add(self, word):
        """
        Add `word` to trie
        """
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char].is_word = True
            else:
                node.children[char]
                node = node.children[char]

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                return node.children[char].is_word
            else:
                node = node.children[char]


# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie1()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')


