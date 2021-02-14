class Employee:
	def ___init___(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.pay = pay
		self.email = first + '-' + last + '@company.com'
	def fullname(self):
		return '{} {}'.format(emp_1.first, emp_1.last)

emp_1 = Employee('Peter', 'Green', 5000)
emp_2 = Employee('Alice', 'Green', 6000)

print(emp_1)
print(emp_2)

emp_1.first = 'peter'
emp_1.last = 'Green'
em_1.email = 'peter.green@gmail.com'
emp_1.pay = 5000

emp_2.first = 'Jim'
emp_2.last = 'steven'
emp_2.email = 'jim.steven@gmail.com'
emp_2.pay = 2000

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())

#Todo List (Physics Mod "Due: Wens", Python Lab "Due: Thursday", Read Tech Comm "Due Thursday",| Study Physics "Due: Friday",| Analytical Report "Due: Monday", Calc Quiz "Due: Sunday")
#Study for Calc(next Week), Study for Python exam (next Week)