secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

def recoverSecret(triplets):
    word = []
    letters = set(t for t in triplets for t in t)
    for _ in range(len(letters)):
        not_first = []
        for letter in letters:
            for triplet in triplets:
                exc_triplet = [i for i in triplet if i not in word]
                if letter in exc_triplet and exc_triplet.index(letter) != 0: 
                    not_first.append(letter)
            first = set(letters) - set(not_first) # first letter
            if len(first) == 1:
                letters = set(not_first)
                word.append(first.pop())
    return ''.join(word)


assert recoverSecret(triplets) == secret