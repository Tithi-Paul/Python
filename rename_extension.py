filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for i , name in enumerate(filenames):
  if name.find(".hpp") >= 0:
    filenames[i] = name[0:len(name)-2]
    


# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

print(filenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
