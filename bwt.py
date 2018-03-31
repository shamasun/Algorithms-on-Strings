import sys

def bwt(text):
    k = len(text)
    bwm = [[None] * k] * k
    myText = list(text)
    bwm[k - 1] = myText
    for i in range(0, len(text) - 1):
        myText = list(myText)
        last = myText.pop(k - 1)
        myText.insert(0, last)
        bwm[i] = myText
    bwm.sort()
    return ''.join([row[k-1] for row in bwm])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(bwt(text))