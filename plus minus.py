#!/usr/bin/env python
# coding: utf-8

# In[53]:


def plusMinus(arr):
    b=0
    c=0
    d=0
    n=len(arr)
    for i in range(0,n):
        if (arr[i]>0):
            b=b+1
        elif arr[i]<0:
            c=c+1
        else:
            d=d+1
    c=c/n
    d=d/n
    b=b/n
    return b,c,d


# In[54]:


arr=[-4, 3, -9, 0, 4, 1 ]

b,c,d=plusMinus(arr)
print(b)
print(c)
print(d)


# In[ ]:





# In[ ]:




