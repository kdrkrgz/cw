def is_anagram(test, original):
    if len(test) != len(original):
        return False

    test_counts = {char: test.count(char) for char in test}
    original_counts = {char: original.count(char) for char in original}

    return all(test_counts.get(char, 0) == original_counts.get(char, 0) for char in set(test))


assert is_anagram('', '') == True
assert is_anagram('aaz', 'zza') == False
assert is_anagram('qweryt', 'qeywrt') == True