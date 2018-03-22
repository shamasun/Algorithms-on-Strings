#Uses python3
import sys

def prefix_trie_match(text, trie):
    k = 0
    symbol = list(text)[k]
    currentNode = 0
    while True:
        edges = list(trie[currentNode].keys())
        if(edges == []):
            return True
        try:
            symbol = list(text)[k]
        except IndexError:
            return False
        else:
            if(symbol in edges):
                currentNode = trie[currentNode][symbol]
                k += 1
            else:
                return False

def trie_pattern_match(text, trie):
    myAnswer = []
    for i in range(0, len(text)):
        myText = text[i:len(text)]
        if prefix_trie_match(myText, trie):
            myAnswer.append(i)
    for j in myAnswer:
        print(j, end=' ')

def trie_contruct(patterns):
    trie = {0:{}}
    root = 0
    for pattern in patterns:
        currentNode = root
        for char in list(pattern):
            part = trie[currentNode]
            if(char in part.keys()):
                currentNode = part[char]
            else:
                currentNode = len(trie)
                trie[currentNode] = {}
                part[char] = currentNode
    return(trie)

text = sys.stdin.readline().strip ()
n = int(sys.stdin.readline().strip ())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
trie = trie_contruct(patterns)
trie_pattern_match(text, trie)