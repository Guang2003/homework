def increte(a):
    if a == 1:
        return 5
    return 2*increte(a/2)+3
i = int(input())
print(increte(i))