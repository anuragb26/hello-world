def deep_reverse(L):
    l=len(L)
    i=0
    while(i<(l/2)):
        L[i],L[l-1-i]=L[l-1-i],L[i]
        if(isinstance(L[i],list)):
        	deep_reverse(L[i])
        if(isinstance(L[l-1-i],list)):
        	deep_reverse(L[l-1-i])
        i+=1

L=[[1,2],[2,3,4],[5,6,7],[1,2,3,4]]
deep_reverse(L)
print(L)