#the highest and lowest values in the dictionary.

Arun= {'English':88,'Hindi':95,'Maths':62,'Science':42,'Social Studies':56}

print("Arun got",Arun)
Maximum= max(Arun, key = Arun.get)
Maximum_value=max(Arun.values())
print("Arun got Highest marks in:",Maximum,Maximum_value,"out of 100")


Minimum= min(Arun, key = Arun.get)
Minimum_value=min(Arun.values())
print("Arun got least marks in:",Minimum,Minimum_value,"out of 100")

