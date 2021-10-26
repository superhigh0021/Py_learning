def check(str1, str2):
    length1 = len(str1)
    length = min(length1, len(str2))
    k = max(range(0, length+1), key=lambda i: i if str1[length1-i:] == str2[:i]else False)
    return(k,str1+str2[k:]) # k为重复字符的个数（两个字符串首尾交叉的最大子串长度）
str1 = input("str1= ")
str2 = input("str2= ")
print(str1, str2)
print(check(str1, str2))
