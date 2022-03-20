import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("Aynı adla klasör var!")


    