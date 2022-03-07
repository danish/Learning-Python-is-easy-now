import importlib
import my_module as mm

importlib.reload(mm)
importlib.reload(mm)

mm.display()
print(mm.add(10, 20))

print(mm.my_module_x)