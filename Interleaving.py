
def AllInter(a,b):
    lengthA = len(a)
    lengthB = len(b)
    if lengthA==0:
        return [b]
    if lengthB==0:
        return [a]
    positionA, *subListA = a
    positionB, *subListB = b
    return [[positionA] + subL for subL in AllInter(subListA, b)] + [[positionB] + subL for subL in AllInter(subListB, a)]

def ParallelInter(a, b):
    interleaving = []
    for i in range(len(a) + len(b)):
        if len(a) > i:
            interleaving.append(a[i])
        if len(b) > i:
            interleaving.append(b[i])
    print (interleaving)

print("Parallel-Inter: ")
ParallelInter([1,2],[3,4])
print("All-Inter: ")
print(AllInter([1,2],[3,4]))