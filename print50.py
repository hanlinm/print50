# print 1-50 where numbers multiple of 2 and 3 will print hello and hi, respectively
num = 1
while num < 51:
	if(num%2 == 0):
		print("hello")
	elif(num%3 == 0):
		print("hi")
	else:
		print(num)

	num += 1	
