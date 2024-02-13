class Human:
    def james(self):
        print("I can walk")
    def tom(self):
        print("can run")

# hh = Human()
# print(hh.james())

class Racoon(Human):
    def racoon(self):
        print("smile")
jj = Racoon()
print(f"I am James and  {jj.james()},{jj.tom()} {jj.racoon()})

