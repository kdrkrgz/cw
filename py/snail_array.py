array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

arr2 = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
]                       

# i=0 saga dogru tum arrayi yaz ve popla
# i=1 array varsa, arrayin sonuncu itemini al popla
# i=2 array varsa, arrayin sonuncu itemini al popla
# i=3 array varsa, arrayin sonuncu itemini al popla
# i=4 array varsa, (len-i) arrayi ters cevir yaz



def snail(snail_map):
    res = []
    while snail_map:
        #add first arrays and pop
        res += snail_map[0]
        snail_map.pop(0)

        if snail_map:
            # betwen last and first arrays add last element and pop
            for i in snail_map:
                res += [i[-1]]
                i.pop(-1)
                
            # last array add reversed and pop
            if snail_map[-1]:
                res += snail_map[-1][::-1]
                snail_map.pop(-1)


            # betwen last and first arrays add first element and pop
            for i in reversed(snail_map):
                res +=[i[0]]
                i.pop(0)

    return res


print(snail(arr2))



# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]