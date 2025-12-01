def roman(s):
    valeurroman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    i = 0     

    while i < len(s):
        if i + 1 < len(s) and valeurroman[s[i]] < valeurroman[s[i + 1]]:
            total += valeurroman[s[i + 1]] - valeurroman[s[i]]
            i += 2
        else:
            total += valeurroman[s[i]]
            i += 1 
        return total
