class Human:
    height = 180
    weight = 55
    def sleep(self, numberOfHours):
        print(self.weight * numberOfHours)
        # print("Human has gone to sleep")
    def walk(self):
        print("Human has gone to walk")
    
# Human
numberOfHours = int(input("Enter the number of hours you sleep "))
man = Human()
man.sleep(numberOfHours)
man.walk()
