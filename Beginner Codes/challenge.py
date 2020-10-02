#Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
vocab=np.array([[]])

#Uploading File (this part is only for collab)

import io
from google.colab import files
uploaded = files.upload()


#playing with data sets

data = pd.read_csv(io.StringIO(uploaded['input.csv'].decode('utf-8')))
data['question'][0]
vocab=[]

k=[]      
z=[]   #sentence

m1=pd.Series(data['answer'])
m2=pd.Series(data['question'])
m=pd.concat([m1,m2])   

for i in m:
  vocab.extend(i.split())
  
vocab=list(set(vocab))

#Sentence Retrival
for i in range(0,data.shape[0]):
  kk=data.loc[i]
  for j in kk:
    k=j.split()
    z.append(k)
    
#Conversion of sentences to 2d Numpy array
def find( le,count,a,ze ):
  for i in range(0,len(vocab)):
    if(a == vocab[i]):
      ze[count,i]=1
      return(ze)
      
#final step
 
for i in z:
  n=np.zeros((len(i),len(vocab)))
  count=0
  for j in i:
    n=find(len(i),count,j,n)
    count=count+1
  print(n)  


#END
