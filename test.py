def reorganizeString(s: str) -> str:
    temp = list(s)
    ans = "" + temp[0]
    temp.remove(temp[0])
    while temp:
        for i in temp:
            curr = ans[-1]
            if i != curr:
                ans = ans + i
                temp.remove(i)
    if len(ans) == len(s):
        return ans
    return ""


print(reorganizeString("vvvlo"))
