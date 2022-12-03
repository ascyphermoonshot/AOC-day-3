import string
from textwrap import wrap
def compare(lst1,lst2,lst3):
	return ''.join(set(lst1)&set(lst2)&set(lst3))
def get_groups(lst):
    for i in range(0,len(lst),3):
        yield lst[i:i+3]
categories=list(string.ascii_letters)
priorities=list(range(1,len(categories)+1))
pdic={categories:priorities for categories,priorities in zip(categories,priorities)}
with open("/storage/emulated/0/Download/input (2).txt") as f:
	f.seek(0)
	sacks=f.readlines()
priors=0
gelves=get_groups(sacks)
for gelf in gelves:
	elf1,elf2,elf3=gelf
	item=compare(elf1,elf2,elf3)
	item=item.replace('\n','')
	if len(item)==1:
		priors+=pdic[item]
print(priors)