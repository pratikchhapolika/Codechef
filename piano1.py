t =input () 
for i in range(t):
    s = raw_input() 
    length = 0 
    for counter in s:
	if counter == 'T' :
	    length += 2 
	else :
	    length += 1 
    n = input()
   # print "length is",length
    iter = 12*n 
    ans = 0 
    p = length
    while p<iter:
	ans += iter - p 
	p+= length
    print ans 