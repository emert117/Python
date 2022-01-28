def count_substring(string, sub_string):
    count = 0
    offset = string.find(sub_string)
    while (offset >= 0):
        count += 1
        offset = string.find(sub_string, offset+1, len(string))
        
    return count

print(count_substring("ABCDCDC", "CDC"))