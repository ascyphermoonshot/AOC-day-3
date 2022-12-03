import string
def compare(lst1,lst2):
	return ''.join(set(lst1)&set(lst2))
categories=list(string.ascii_letters)
priorities=list(range(1,len(categories)+1))
pdic={categories:priorities for categories,priorities in zip(categories,priorities)}
with open("/storage/emulated/0/Download/input (2).txt") as f:
	f.seek(0)
	sacks=f.readlines()
priors=0
for sack in sacks:
	comp1=list(sack[0:int(len(sack)/2)])
	comp2=list(sack[int(len(sack)/2)::])
	item=compare(comp1,comp2)
	if len(item)==1:
		priors+=pdic[item]
print(priors)