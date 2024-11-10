class Node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right 
        self.huff=''

def printnodes(node,val=''):
    newVal= val + str(node.huff)

    if node.left:
        printnodes(node.left,newVal)
    
    if node.right:
        printnodes(node.right,newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

n = int(input("Enter number of symbols : "))
freq=[]
chars=[]

for i in range(n):
    symbol = input(f"Enter Symbol {i+1} : ")
    fr=int(input("Enter Frequency of {symbol} : "))
    freq.append(fr)
    chars.append(symbol)

nodes=[]

for j in range(len(chars)):
    nodes.append(Node(freq[j],chars[j]))

while len(nodes) > 1:
    nodes = sorted(nodes,key=lambda x:x.freq)

    left = nodes[0]
    right = nodes[1]

    left.huff = '0'
    right.huff = '1'

    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print("\nHuffman Codes:")
printnodes(nodes[0])
