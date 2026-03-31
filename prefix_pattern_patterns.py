arr=[1,1,1]
k=2 
d={0:1}
count=0 
prefix_sum=0
for i in arr:
    prefix_sum+=i 
    
    if prefix_sum-k in d:
        count+=d[prefix_sum-k]
        
    d[prefix_sum]=d.get(prefix_sum,0)+1
print(count)