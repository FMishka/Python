class Animal:
	def __init__(self, name):
		self.name = name

	def Eating(self):
		print(self.name + " ест")

class Cat(Animal):
	sleep = False
	def __init__(self, name):
		super().__init__(name)

	def Sleep(self):
		print("Кот спит")
		self.sleep = True
	
	def Awake(self):
		if self.sleep == True:
			self.sleep = False
			print("Кот не доволен...")
		else:
			print("Кот и так не спит!")

	def Play(self):
		if self.sleep == True:
			print("Кот спит! Играть не может!")
		else:
			print("Мрррр...")

cat = Cat("Том")
print("Проверка: будет ли кот есть")
cat.Eating()
print("Проверка: будет ли кот спать")
cat.Sleep()
print("Проверка: будет ли играть пока спит")
cat.Play()
print("Проверка: будет ли кот просыпаться")
cat.Awake()
print("Проверка: будет ли кот просыпаться, если он уже проснулся")
cat.Awake()
print("Проверка: сработало ли пробуждение и будет ли он играть")
cat.Play()
