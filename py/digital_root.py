def digital_root(n):
    if n <= 9:
        return n
    
    n = sum([int(i) for i in str(n)])
    return digital_root(n)


# digital_root(942) # 6
print(digital_root(493193))