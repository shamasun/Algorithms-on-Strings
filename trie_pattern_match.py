def match(text, trie):
    k = 0
    currentNode = 0
    for i in range(len(text)):
        symbol = list(text)[k]
        edges = list(trie[currentNode].keys())
        if(symbol in edges):
            k += 1
            currentNode = trie[currentNode][symbol]
            if (list(trie[currentNode].keys()) == []):
                return True
        else:
            return False
    return False

def trie_pattern_match(text, trie):
    myAnswer = []
    for i in range(0, len(text)):
        myText = text[i: (i + 100)]
        if match(myText, trie):
            myAnswer.append(i)
    for j in myAnswer:
        print(j, end=' ')