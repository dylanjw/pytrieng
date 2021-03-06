#!/usr/bin/env python3
import pickle

class EndNode:
    parent = None
    def __init__(self, parent):
        self.parent = parent


class Node:
    parent: None
    children: None
    val: None
    def __init__(self, val=None, children=None, parent=None):
        self.val = val
        self.children = children or {}
        self.parent = parent


class PopString:
    string = None
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def popleft(self):
       char = self.string[0]
       self.string = self.string[1:]
       return char


def parse_words(words, root):
    for word in words:
        node = root
        word = PopString(word)
        while True:
            try:
                char = word.popleft()
            except IndexError:
                node.children["*"] = EndNode(node)
                break

            if node.children.get(char) is None:
                node.children[char] = Node(char, parent=node)

            node = node.children[char]
    return root


def word_from_end_node(node):
    word = ""
    if not isinstance(node, EndNode):
        raise ValueError("Not an EndNode")
    parent = node.parent
    while parent.val is not None:
        word = parent.val + word
        parent = parent.parent
    return word


def get_words_from_node(node):
    words = []
    prefix = word_from_end_node(node)[:-1]

    def inner(node, prefix):
        nonlocal words

        if not isinstance(node, EndNode):
            prefix = prefix + node.val
        else:
            words.append(prefix)
            return

        if node.children is None:
            return

        for child in node.children.values():
            inner(child, prefix)

    inner(node.parent, prefix)

    return words


def retrieve(trie, val):
    node = trie
    for char in val:
        try:
            node = node.children[char]
        except IndexError:
            raise ValueError(f"{val} is not an English word")
    else:
        try:
            return node.children['*']
        except IndexError:
            raise ValueError(f"{val} is not an English word")


def english():
     with open("words.txt", "r") as w:
         for word in w.readlines():
             yield word.strip()


trie = parse_words(english(), Node())


def prefixed_with(val):
    node = retrieve(trie, val)
    return list(get_words_from_node(node))

def old_prefixed_with(val):
    node = retrieve(trie, val)
    return list(old_get_words_from_node(node))
