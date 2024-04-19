def accum(st):
    return '-'.join([str(st[i]*(i+1)).title() for i in range(len(st))])


accum("abcd") # -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") # -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt")) # -> "C-Ww-Aaa-Tttt"