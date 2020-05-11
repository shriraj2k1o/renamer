import os

# create a list of files in the directory
files = os.listdir()

# ADDing EXTENSION to the file
for x in files:
    # check if its ending with .jpg
    if x.endswith('.jpg'):
        print(x)
    # check if its ending with .py
    elif x.endswith('.py'):
        print(x)
    # check if its ending with .jpeg
    elif x.endswith('.jpeg'):
        print(x)
    # check if its ending with .png
    elif x.endswith('.png'):
        print(x)
    # add .jpg at the end of the file name
    else:
        f = os.path.join(x + '.jpg')
        print(f)
        # completely rename the file
        os.rename(x, f)







# # DELETING EXTENSION from the file
# for a in files:
    
#     if a.endswith('.py'):
#         print(a)
#     else:
#         name, ext = os.path.splitext(a)
#         os.rename(a, name)
#         print(a)


# #DELETING all file except .py
# for c in files:
#     if c.endswith('.py'):
#         print(c)
#     else:
#         os.remove(c)