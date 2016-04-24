def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

start = 1
end = 100000
finalSum = []
for i in range(start, end+1):
    a = factors(i)
    s = 0 
    for j in a:
        if j % 2 != 0 :
            s += j
    finalSum.append(s)

for t in range(input()):
    l, r = map(int , raw_input().split())
    print sum(finalSum[l-1 : r])
