#!/usr/bin/env python
# coding: utf-8

# Puzzle1

# In[272]:


passwords = open("C:\\Users\\Weronika\\Desktop\\aoc2020.txt", "r").read().splitlines()


# In[273]:


import pandas as pd 


# In[274]:


df = pd.DataFrame(passwords)


# In[275]:


df[['Range','Letter','Password']] = df[0].str.split(expand=True) 


# In[276]:


df[['Min','Max']] = df["Range"].str.split("-",expand=True) 


# In[277]:


df['Letter'] = df['Letter'].str.replace(':', '')


# In[278]:


list1=[]


# In[279]:


for i in range(len(df)):
    x = df.loc[i,'Password'].count(df.loc[i,'Letter'])
    df['Min'] = pd.to_numeric(df['Min'])   
    df['Max'] = pd.to_numeric(df['Max'])   
    if x >= df.loc[i,'Min'] and x <= df.loc[i,'Max']:
            list1.append(x)


# In[280]:


valid_pass=len(list1)


# Puzzle2

# In[266]:


list_passwords1=[]
list_passwords2=[]


# In[267]:


df['Min'] = pd.to_numeric(df['Min'])   
df['Max'] = pd.to_numeric(df['Max'])
for i in range(len(df)):
    Letter = df.loc[i,'Letter']
    FirstAppearance = df.loc[i,'Min']-1
    SecondAppearance = df.loc[i,'Max']-1
    x = df.loc[i,'Password'][FirstAppearance]
    y = df.loc[i,'Password'][SecondAppearance]
    
    if x == Letter or y==Letter:
        list_passwords1.append(df.loc[i,'Password'])
        if x==y:
            list_passwords2.append(df.loc[i,'Password'])


# In[281]:


valid_pass=len(list_passwords1) - len(list_passwords2)


# In[282]:


valid_pass


# In[ ]:




