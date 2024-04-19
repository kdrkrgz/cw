def expanded_form(num):
    return " + ".join([str(int(v)*10**k) for k, v in enumerate(str(num)[::-1]) if v != "0"][::-1])



# print(expanded_form(12))  # '10 + 2'
# print(expanded_form(42))  # '40 + 2'
print(expanded_form(70304))  # '70000 + 300 + 4'
