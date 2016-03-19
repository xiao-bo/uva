import fileinput
import sys
def input_to_list(x):
	x.append(raw_input(""))
	return x


if __name__=='__main__':
    ## read inputfile and let line be split 
    ## by ' ' and append into word
	word=[]
	for line in fileinput.input():	
		word.append(line.split()) 
        
	##convert element of word into integer
	i=0
	for line in word: 
		word[i]=map (int,line) 
		i=i+1
	weight=[]
	tmp=[]

	## taxonomy word into weight and 		
	for x in word:
		weight.append(x[0])
		weight.append(x[2])
	
	## insert 1~max(weight) into tmp
	"""
	for x in range(1,max(weight)+2):
		tmp.append([x])   
	"""
	##  for loop above equal below code 
	tmp=[[x] for x in range(1,max(weight)+2)]
	
	## inset 0 into tmp
	i=0
	for x in tmp:
		tmp[i].extend([0])
		i=i+1

	###find highest point at x axis 
	for j in range(0,len(word)):## do number of build
		for i in range(word[j][0],word[j][2]+1):## weight of build has same height
			if tmp[i-1][1]<word[j][1]:## find highest point in a build 
				tmp[i-1][1]=word[j][1]
	#print tmp
	#print "=======\n\n"	

	answer=[]
	prev=0
	for x in range(0,len(tmp)):
		if prev!=tmp[x][1]:
			if tmp[x][1]==0:
				answer.append(tmp[x-1][0])
				answer.append(tmp[x][1])
			else:
				answer.append(tmp[x][0])
				answer.append(tmp[x][1])
			prev=tmp[x][1]

	print " ".join(str(x) for x in answer)




