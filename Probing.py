

def hashkeyFun(age):
	return age % x

def hashing(HASH,age):
	hashkey=hashkeyFun(age)
	HASH[hashkey].append(age)



def display_hash():
    for i in range(len(HASH)):
        print(i, end = " ")
          
        for j in HASH[i]:
            print("-->", end = " ")
            print(j, end = " ")   
        print()



x=3
HASH =[[] for _ in range(x)]
hashing(HASH,12)
hashing(HASH,13)
hashing(HASH,23)
hashing(HASH,11)
hashing(HASH,16)
hashing(HASH,22)
hashing(HASH,15)
hashing(HASH,13)
hashing(HASH,43)
hashing(HASH,37)
hashing(HASH,94)
hashing(HASH,245)


display_hash()
  


