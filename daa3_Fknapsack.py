class Item:
    def __init__(self,p,w):
        self.p=p
        self.w=w

def kns(limit,arr):
    arr_copy = arr[:]
    arr_copy.sort(key=lambda x: (x.p/x.w),reverse=True)
    total=0.0
    for i in arr_copy:
        if i.w<=limit:
            limit -= i.w
            total += i.p
        else:
            total +=(i.p*limit)/i.w
            break
    return total

def kns_p(limit,arr):
    arr_copy = arr[:]
    arr_copy.sort(key=lambda x: (x.p),reverse=True)
    total=0.0
    for i in arr_copy:
        if i.w<=limit:
            limit -= i.w
            total += i.p
        else:
            total +=(i.p*limit)/i.w
            break
    return total

def kns_w(limit,arr):
    arr_copy = arr[:]
    arr_copy.sort(key=lambda x: (x.w))
    total=0.0
    for i in arr_copy:
        if i.w<=limit:
            limit -= i.w
            total += i.p
        else:
            total +=(i.p*limit)/i.w
            break
    return total

def main():
    limit = int(input("\nEnter limit of Knapsack : "))

    n = int(input("\nEnter total number of items : "))

    arr=[]
    for i in range(n):
        p = float(input(f"\nEnter Item {i+1} profit = "))
        w = float(input(f"Enter Item {i+1} Weight = "))
        arr.append(Item(p,w))

    print("\n\nMax Profit as per Profit/Weight ratio ---> ",kns(limit,arr))
    print("\n\nMax Profit as per Maximum Profit      ---> ",kns_p(limit,arr))
    print("\n\nMax Profit as per Minimum Wweight     ---> ",kns_w(limit,arr))

main()
