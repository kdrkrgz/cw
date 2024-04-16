# 1- \n ile satirlari bul
# 2- satirlarda don
# 3- markerlarda don
# 4- marker varsa satirda split et ve ilk elementi al
# 5- satiri rstrip et
# 6- satirlari birlestir


def strip_comments(strng, markers):
    lines = strng.split('\n')
    for i in range(len(lines)):
        for marker in markers:
            if marker in lines[i]:
                lines[i] = lines[i].split(marker)[0].rstrip()
    return '\n'.join(lines)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
# 'apples, pears\ngrapes\nbananas'
