def generate_hashtag(s):
    if not s or len(s)>140:
        return False
    ht = '#' + ''.join([i.strip().capitalize() for i in s.strip().split(' ')])
    return ht if not len(ht) >= 140 else False

print(generate_hashtag("ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq" ))