def process(value):
    p_mapping = {
        "[": "]",
        "{": "}",
        "(": ")"
    }
    for c in value:
        if c in p_mapping.keys():
            closer = p_mapping.get(c)
            if value.find(closer) - value.find(c) == 1:
                value = list(value)
                value.pop(0)
                value.pop(0)
                value = "".join(value)
                if not value:return True
                continue
            elif value.rfind(closer) == len(value) -1:
                value = list(value)
                value.pop(0)
                value.pop(len(value) -1)
                value = "".join(value)
                if not value:return True

    return False
# condition arasindaki islemler func olacak


# ilk parantezin karsiligi varmi varsa yeri dogrumu
    # ( ) # true
    # ( ][ ) # true ama icerisi yanlis
        # ] [
    # ([]) # true
    # ( ] [ ]) true 

if __name__ == '__main__':
    assert process(value='{([[]}') == False
    assert process(value='[[({})]]') == True
    assert process(value='[') == False
    assert process(value='{{]') == False
    assert process(value=')[{}])') == False
    assert process(value='{}()[][]()') == True
    assert process(value='({[{}]})') == True
    assert process(value='{}()[[()]]') == True
    assert process(value='{}(){[()]]}}') == False
    assert process(value='{}()[][]{}') == True
    assert process(value='({([]}))') == False