def get_choco_max(jarray):
    if len(jarray) <= 2:
        return max(jarray)
    an, an1 = jarray[0], jarray[1]
    for num in jarray[2:]:
        an2 = max(num + an, an1)
        an, an1 = an1, an2
    return an2
