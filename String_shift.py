# Problem Statement :Given two strings A and B,
# write a function can_shift to return whether or not
# A can be shifted some number of places to get B.

# Example:

# Input:

# A = 'abcde'
# B = 'cdeab'
# can_shift(A, B) == True

# A = 'abc'
# B = 'acb'
# can_shift(A, B) == False


def can_shift(A, B):
    char_list = list(A)
    for i in range(len(char_list)-1):
        rotated_list = char_list[-i:]+char_list[:-i]
        rotated_string = "".join(rotated_list)
        if rotated_string == B:
            return True
            break
    return False


print(can_shift("abcde", "cdeab"))
print(can_shift("abc", "acb"))
