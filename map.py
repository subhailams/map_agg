# your code goes here

t = int(input())
map_dict = {}
keys_hit = []
for i in range(t):
    n = list(map(int,input().split()))
    n1, n2 = n
    for j in range(n1):
        arr = input().split()
        key = arr[0]
        value = sum(list(map(int,arr[1:])))
        if key not in map_dict.keys():
            map_dict[key] = value
        else:
            map_dict[key] += value
            keys_hit.append(key)
            
for key,val in map_dict.items():
	if key in keys_hit:
		print(key, val)
	
	
