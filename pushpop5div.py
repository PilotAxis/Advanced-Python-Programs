def PUSH(Arr):
    s = []
    for i in range(0, len(Arr)):
        if Arr[i]%5==0:
            s.append(Arr[i])
    if len(s) == 0:
        print("Empty Stack")
    else:
        print(s)

PUSH([1,10,15,20])