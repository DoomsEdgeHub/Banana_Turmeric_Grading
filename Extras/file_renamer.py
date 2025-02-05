import os
i=0
path = os.chdir("/home/sandy0810/Documents/Banana_Turmeric/Dataset/Turmeric/Class_B")
for file in os.listdir(path):
    new_file = "{}.png".format(i)
    os.rename(file,new_file)
    i = i+1
    print(new_file)