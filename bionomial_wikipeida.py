
# coding: utf-8

# In[47]:


from scipy.special import comb
import numpy as np
n = np.arange(32)
print(n)
pmf = []


# In[59]:


pmf=[]
j=0
value =0
for i in n:
    x0 = comb(31,i)
    x1 = 0.447**i
    x2 = 0.553**(31-i)
    pmf.append(x0*x1*x2)
print(pmf[15])
print(pmf[30])
import matplotlib.pyplot as plt
print(n)
print(len(pmf))
pmf
plt.plot(n,pmf)
plt.show()

