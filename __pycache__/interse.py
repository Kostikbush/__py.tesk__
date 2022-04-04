def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res
s1,s2,s3 = "SPAM","SLAM","SCAM"
lis = [1,2,3,4]
lis1= [3,4,5,6,7]
