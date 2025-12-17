class Cars:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def display(self):
        print(self.model,self.year)
car1=Cars("BMW",2025)
car2=Cars("Audi",2025)
car3=Cars("Mercedes",2025)
print(car1.model)
print(car1.year)
print(car2.model)
print(car2.year)
print(car3.model)
print(car3.year)
