#Uses python3
import sys

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

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = trie_contruct(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))