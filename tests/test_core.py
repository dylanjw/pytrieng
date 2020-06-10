#!/usr/bin/env python3
from trieng import *


def test_pop_string():
    string = PopString("baseball")
    char = string.popleft()
    assert char == 'b'
    char = string.popleft()
    assert char == 'a'
    char = string.popleft()
    assert char == 's'


def test_parse_dict():
    test_words = ["cat", "cathedral", "ball", "balloon", "pumpkin"]
    root = Node(val="")
    parse_words(test_words, root)
    assert '*' in root.children['c'].children['a'].children['t'].children


def test_english_words():
    words = english()
    next(words)
    next(words)
    next(words)
    next(words)
    next(words)
    next(words)
    assert next(words) == "aardwolf"


def test_retrieve_a_random_word():
    assert retrieve(ENGLISH_TRIE, "bombastic")


def test_word_from_end_node():
    node = retrieve(ENGLISH_TRIE, "bombastic")
    word_from_end_node(node) == "bombastic"


def test_words_from_prefix():
    prefix = retrieve(ENGLISH_TRIE, "bomb")
    words = list_from_node(prefix)
    assert next(words) == "bomb"
    assert next(words) == "bombacaceae"
