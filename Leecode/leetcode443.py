input1 = ["a","a","a","b","b","a","a"]

def compress(chars):
    chars.append('0')
    i = 1
    counter = 1

    while i < len(chars):
        if chars[i-1] == chars[i]:
            chars.remove(chars[i])
            counter += 1
        elif chars[i - 1] != chars[i] and counter == 1:
            i += 1
            continue
        elif chars[i-1] != chars[i]:
            for p in str(counter)[::-1]:
                chars.insert(i,p)
            counter = 1
            i += 2

    chars.remove('0')
    return chars

print(compress(input1))