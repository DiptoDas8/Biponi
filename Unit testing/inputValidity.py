def isValid(max_price, min_price):
	if (isinstance(max_price,(int, long)) and isinstance(min_price,(int, long))):
		if(max_price<0 or min_price<0):
			print "Negative price is not valid"
			return False
		elif(max_price<min_price):
			print "Maximum price cannot be less than Minimum price"
			return False
		elif(max_price>1000000000 or min_price>1000000000):
			print "We do not have this much costly product"
			return False
		else:
			#print "Input vailidity checked"
			return True
	else:
		print "Please enter number as input"
		return False
	return True
