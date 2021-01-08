
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import colorama

fail=open("data.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(float(line[n+1:len(line)].strip()))
fail.close()
plt.title("IKT turvameetodite kasutamise osatähtsus ettevõttes: 2018")
plt.barh(mas1,mas2,color="pink")
plt.show()