if __name__ == '__main__':
    N = int(input())
    lst =[]
for i in range(N):
    l= input().split()
    if 'insert' in l :
        lst.insert(int(l[1]),int(l[2]))
    elif 'print' in l:
        print(lst)
    elif 'remove' in l:
        lst.remove(int(l[1]))
    elif 'append' in l :
        lst.append(int(l[1]))
    elif 'sort' in l:
        lst.sort()
            #print(lst)
    elif 'pop' in l :
        lst.pop()
    elif 'reverse' in l :
        lst.reverse()