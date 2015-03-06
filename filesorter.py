
# coding: utf-8

# In[57]:




# In[58]:

def nsort(filename):
    with open(filename) as f:
        content = f.readlines()
        result = []
        for idx, val in enumerate(content):
            val = val.replace('\n', '')
            if idx == 0:
                result.append(val)
            elif val > result[len(result) - 1]:
                result.append(val)
            for i in range(len(result)):
                if val < result[i]:
                    result.insert(i, val)
                    break
        return result
        
print(nsort('sorttest.txt'))


# In[ ]:



