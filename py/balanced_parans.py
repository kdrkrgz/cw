def balanced_parens(n):
    plist = []

    def backtrack(left, right, path):
        print(path)
        if right == left == n:  # print when done
            plist.append(path)

        if left < n:
            backtrack(left + 1, right, path + "(")

        if right < left:
            backtrack(left, right + 1, path + ")")

    backtrack(0, 0, "")
    return plist


# 0 -> ""
# 1 -> ()
# 2 -> ()() (())
# 3 -> ()()() ()(()) (())() (()()) ((()))
