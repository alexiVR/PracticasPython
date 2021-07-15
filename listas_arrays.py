#arrays
array = ["hola","pc",10.2,12,32,[2,1,2,1],True,False,"pc"]
array2 = [120,130,21]
#vista del array
print(array[5])
print(array[-1])
print(array[:3])
print(array[:])
print(len(array))

#agregar datos al array
array.append("perro")
print(array)
array.insert(0, 88)
print(array)
array.extend([1,89,True,100])
print(array)

#union de array
array3 = array+array2
print(array3)
#busqueda de datos
print("pc" in array)

print(array.index("pc"))
print(array.count(""))
array.remove("pc")
print(array)
array.reverse()
print(array)
array2.sort()
print(array2)