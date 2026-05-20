

# def longest_sub(s):
#     if(len(s)==0):
#         return 0
#     if(len(s)==1):
#         return 1
#     count = 1
  

#     for j in range(0,len(s)):
#         new = []
#         print("------>"+"now from "+s[j:])
#         a = s[j:]
#         for i in range(0,len(a)):
#             if(a[i] not in new):
#                 new.append(a[i])
#                 print(new)
#                 if(i == len(a)-1):
#                     if(count<len(new)):
#                         count = len(new)
#                         print(count)
#                         new = [s[i]]
#                     else:
#                         new = [s[i]]

#             else:
#                 if(count<len(new)):
#                     count = len(new)
#                     print(count)
#                     new = [a[i]]
#                 else:
#                     new = [a[i]]
#     return count


def longest_sub(s):
    count = 0
    new = set()
    for i in s:
        new.add(i)
        print(new)
        print(count)
        

print(longest_sub("bbtablud"))


