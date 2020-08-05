class Animal:
	def __init__(self, name):
		self.name = name
	def GetRoar(self):
		print(self.name + " - кричит")
	def Eating(self):
		print(self.name + " ест")

class Cat(Animal):
	# Типо доступ private
	__sleep = False
	def __init__(self, name):
		super().__init__(name)
	def Eating(self):
		print("Кот " + self.name + " наелся и спит")
		self.__sleep = True
	def Sleep(self):
		print("Кот спит")
		self.__sleep = True
	
	def Awake(self):
		if self.__sleep == True:
			self.__sleep = False
			print("Кот не доволен...")
		else:
			print("Кот и так не спит!")

	def Play(self):
		if self.__sleep == True:
			print("Кот спит! Играть не может!")
		else:
			print("Мрррр...")

cat = Cat("Том")
print("Проверка: наследования")
cat.GetRoar()
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
print("Проверка: полимофизма")
cat.Eating()

# Изменение приватного доступа(
cat._Cat__sleep = True
cat._Cat__sleep = False