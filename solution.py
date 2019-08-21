class Line():
	def __init__(self,p1,p2):
		self.p1_x = p1[0]
		self.p1_y = p1[1]
		self.p2_x = p2[0]
		self.p2_y = p2[1]

class det():
	def __init__(self,l1,l2):
		self.l1 = l1
		self.l2 = l2
		
	def crossP(self):
		# y = kx + b
		k1 = float((self.l1.p1_y - self.l1.p2_y)/(self.l1.p1_x - self.l1.p2_x))
		k2 = float((self.l2.p1_y - self.l2.p2_y)/(self.l2.p1_x - self.l2.p2_x))
		b1 = float(self.l1.p1_y - k1*self.l1.p1_x)
		b2 = float(self.l2.p1_y - k2*self.l2.p1_x)
		print("k1,b1;k2,b2",k1,b1,k2,b2)
		
		# y = kx + b
		# 0 = (k1-k2)x +(b1-b2)
		# x = (b2 - b1)/(k1 - k2)
		# y = k1*x + b1
		try:
			x = (b2 - b1)/(k1 - k2)
			print(x)
		except:
			if b2 == b1:
				print("paralleled - same line")
				return False
			else:
				print("paralleled - not same line")
				return False
		y = k1*x + b1
		if x >= self.l1.p1_x and x <= self.l1.p2_x:
			print(x,y)
			return True
		else:
			return False

if __name__ == "__main__":
	p1 = [0,0]
	p2 = [1,1]
	p3 = [0,1]
	p4 = [1,0]

	'''
	p1 = [0,1]
	p2 = [1,1]
	p3 = [0,0]
	p4 = [1,0]
	'''

	'''
	p1 = [0,0]
	p2 = [1,100]
	p3 = [0,1]
	p4 = [1,0]
	'''

	l1 = Line(p1,p2)
	l2 = Line(p3,p4)
	detector = det(l1,l2)
	jud = detector.crossP()
	print(jud)