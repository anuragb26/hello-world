s="anurag bajaj"

print s[3:0:-1]
print s[3:11:1]
s=s.replace(s[0:6:1],s[5::-1],1)
print s
# s[0:6]=str(reversed(s[0:6]))
# print s