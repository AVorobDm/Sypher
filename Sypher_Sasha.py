
# coding: utf-8

# In[3]:


class Syp():

    def __init__(self,key=3):
        self.key = key

    l = [" ",",","!","?",":", ".", "'"]

    def encode(self,string):
        nstring = 0
        s = ""
        for i in string:
            if i in Syp.l:
                s= s+i
                continue 
            else:
                nstring = chr(ord(i)+self.key)
                if ord(nstring)>90 and ord(nstring)<97 or ord(nstring)>122:
                    nstring = chr(ord(nstring)-26)
                s = s+nstring
        return s

    def decode(self,string):
        ostring = 0
        s = ""
        for i in string:
            if i in Syp.l:
                s= s+i
                continue
            else:
                ostring = chr(ord(i)-self.key)
                if ord(ostring)<65 or ord(ostring)<97:
                    ostring = chr(ord(ostring)+26)
                s = s+ostring
        return s 


# In[4]:


text = Syp(2)
print(text.encode("La La Land!"))

