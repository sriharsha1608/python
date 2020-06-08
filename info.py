#def isert(val,key):
           

a=[10,6,2,3,7,1,2]
d=[ ]
f=[]
rem=0
ins=0
for i in a:
	if len(d)==0:
		d.append(i)
		ins=ins+1
		print(d)
	elif len(d)==1:
		if d[0]>i:
			d.append(0)
			d[0],d[1]=i,d[0]
			ins=ins+1
			print(d)
		else:
			d.append(i)
			ins=ins+1
			print(d)
			#print(len(d))
		#print(d)	
	else:
	    c=len(d)
	    count=0
	    for j in d:
	        count=count+1
	        #print(j)
	        #print(c)
	        if i==j:
	            rem=rem+count
	            ins=ins+count+1
	            d.append(i)
	            d.sort()
	            print(d)
	            break
	        elif j>i:
	            s=c-count
	            if d[0]>i:
	                rem=rem
	                ins=ins+1
	                d.append(i)
	                d.sort()
	                print(d)
	                break
	            elif s<count:
	                d.append(i)
	                rem=rem+s
	                ins=ins+s+1
	                
	                d.sort()
	                print(d)
	                break
	                
	            else:
	                d.append(i)
	                rem=rem+count
	                ins=ins+1+count
	                
	                d.sort()
	                print(d)
	                break
	        elif i>j:
	            s=c-count
	            if s<count:
	                d.append(i)
	                rem=rem+s
	                ins=ins+s+1
	                
	                d.sort()
	                print(d)
	                break
	                
	            else:
	                d.append(i)
	                rem=rem+count
	                ins=ins+1+count
	                
	                d.sort()
	                print(d)
	                break
	                
	            
	       
	             
	             
	                
	                
tot=rem+ins
print(tot)