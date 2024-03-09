from collections import Counter


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


def max_cha(dic):
    max_val = 0
    key_res = ""
    for key, val in dic.items():
        if val > max_val:
            max_val = val
            key_res = key
    return key_res


def reorganize_string(s: str) -> str:
    temp = list(s)
    dic = Counter(temp)
    res = [""] * len(s)
    max_key = max_cha(dic)
    if dic[max_key] > (len(s) + 1) // 2:
        return ""
    max_val = dic[max_key]
    idx = 0
    while max_val:
        res[idx] = max_key
        idx += 2
        max_val -= 1
    dic[max_key] = 0
    for key, val in dic.items():
        if val:
            while val:
                if idx >= len(s):
                    idx = 1
                res[idx] = key
                idx += 2
                val -= 1
    return "".join(res)


print(reorganizeString("vvvlo"))
print(reorganize_string("vvvlo"))
