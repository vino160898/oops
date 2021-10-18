class School:
	'''State Board School - Govt. of Tamil Nadu''' #documandation string
	
	
#Constructor - Initializing object specific values
#Automatic calling when objects are created
#Instance Creation - Instantiation 
	def __init__(self, name, age, qual, exp=0):  #exp(var_len_arg)
		self.t_name = name    #self is object specific values
		self.t_age = age
		self.t_qual = qual
		self.t_exp = exp
		
	def inspect(self):
		print(self.t_name)
		print(self.salary)
		
	def pay(self, salary): #local variable
		#print(salary) 
		self.salary = salary
		
teacher1 = School("Raghu", 35, "M.Sc., M.Phil",10)
teacher2 = School("Ram", 45, "M.Sc., M.Phil, Ph.D.,",15)
teacher3 = School("Ram", 25, "M.Sc., M.Phil")


teacher1.pay(10000)  #must be first calling in arg passing
teacher2.pay(20000)
teacher1.inspect() #function / method calling statement
teacher2.inspect()
teacher3.pay(20000)
teacher3.inspect() #function / method calling statement
teacher3.position = "head master"
print(teacher3.__dict__)
print(teacher1.__dict__) 
del teacher3.position
print(teacher3.__dict__)
