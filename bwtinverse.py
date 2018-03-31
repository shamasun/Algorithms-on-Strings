# python3
import sys

def stringCounter(myList):
    l = len(myList)
    stringCounter = [0] * l
    fullCounter = {'A':0,'C':0,'G':0,'T':0,'$':0}
    for i in range(l):
        char = myList[i]
        value = fullCounter[char] + 1
        stringCounter[i] = value
        fullCounter[char] = value
    return stringCounter

def reverseBWT(bwtext):
    last = list(bwtext)
    first = last[:]
    first.sort()
    lastCounter = stringCounter(last)
    firstCounter = stringCounter(first)
    myDict = dict(zip(tuple(zip(first, firstCounter)), tuple(zip(last, lastCounter))))
    answer = ['$']
    myKey = ('$', 1)
    for i in range(0, len(last)-1):
        V = myDict[myKey]
        char = V[0]
        answer.append(char)
        myKey = V
    answer.reverse()
    return ''.join(answer)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(reverseBWT(text))