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