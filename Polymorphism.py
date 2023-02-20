'''class Principal:
    def role(self):
        print("Im a Principal of this college !")

class Dean:
    def role(self):
        print("Im a Dean of this college !")

class Hod:
    def role(self):
        print("Im a Hod of this college !")

class Faculty:
    def responsibility(self):
        print("Im a Faculty of this college !")


def func(obj):     # Function decalaration
    obj.role()

campus = [Principal(), Dean(), Hod(), Faculty()]

for obj in campus:
    func(obj)        # Calling to Function

'''

# =======================Solution of above problem ================
class Principal:
    def role(self):
        print("Im a Principal of this college !")

class Dean :
    def order(self):
        print("Im a Dean of this college !")

def call(obj): 
    if hasattr(obj, "role"):
        obj.role()
    elif hasattr(obj, 'order' ):
        obj.order()

obj = Principal()
call(obj)

obj = Dean()
call(obj)