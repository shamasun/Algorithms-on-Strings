#Uses python3
import sys

def match_extend(text, trie, marker):
    k = 0
    currentNode = 0
    for i in range(len(text)):
        symbol = list(text)[k]
        edges = list(trie[currentNode].keys())
        if(symbol in edges):
            k += 1
            currentNode = trie[currentNode][symbol]
            if (marker[currentNode]):
                return True
        else:
            return False
    return False

def trie_pattern_match_extend(text, trie, marker):
    myAnswer = []
    for i in range(0, len(text)):
        myText = text[i: (i + 100)]
        if match_extend(myText, trie, marker):
            myAnswer.append(i)
    for j in myAnswer:
        print(j, end=' ')

def trie_extend_contruct(patterns):
    trie = {0:{}}
    marker = {}
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
                marker.update({currentNode:False})
                part[char] = currentNode
        marker.update({currentNode:True})
    return trie, marker

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
myTrie, myMarker = trie_extend_contruct(patterns)
trie_pattern_match_extend(text, myTrie, myMarker)