import fileinput
import sys
def input_to_list(x):
	x.append(raw_input(""))
	return x


if __name__=='__main__':
	answer=[]
	word=[]
	i=0
    ## read inputfile and let line be split 
    ## by ' ' and append into word
	for line in fileinput.input():	
		word.append(line.split()) 
        
		##convert element of word into integer
	for line in word: 
		word[i]=map (int,line) 
		i=i+1
		weight=[]
		height=[]
		tmp=[]

	## taxonomy word into weight and height		
	for x in word:
		weight.append(x[0])
		weight.append(x[2])
	for x in range(1,max(weight)+1):
		tmp.append(x)
	print tmp        





