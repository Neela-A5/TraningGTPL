#"If it walks like a duck and quacks like a duck, treat it like a duck."
#So, different classes can be used in the same way if they provide the required method
class Python:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Converting Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()

#ide = Python()
ide = MyEditor()


lap1 = Laptop()
lap1.code(ide)