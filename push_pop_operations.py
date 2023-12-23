def PushS(sk):
    s = int(input())
    sk.append(s)
    return sk

def PopS(sk):
    if len(sk) == 0:
        print("Empty")
    else:
        sk.pop()

sk = print(PushS([1]))