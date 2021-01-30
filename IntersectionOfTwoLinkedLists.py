def getIntersectionNode(a, b):
    seen = set()
    while a or b:
        if a:
            if a in seen:
                return a
            else:
                seen.add(a)
            a = a.next
        if b:
            if b in seen:
                return b
            else:
                seen.add(b)
            b = b.next
    print(seen)
    return None
