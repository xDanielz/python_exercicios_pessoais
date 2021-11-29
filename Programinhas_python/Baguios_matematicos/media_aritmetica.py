def media_aritmetica(list_num: "[1, 2, 3] or [(1,2, af), (2, 3, af)]") -> float:
    result = taf = 0
    if isinstance(list_num[0], tuple):
        for mn, mx, af in list_num:
            result += (mn+mx)/2*af
            taf += af
        return result/taf
    return sum(list_num)/len(list_num)


print(media_aritmetica([(350, 450, 380), (450, 550, 260), (550, 650, 200), (650, 750, 180), (750, 850, 120), (850, 950, 60)]))
