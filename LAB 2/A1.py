import pandas as pd
import numpy as np


data = pd.read_csv('data.csv')
A = pd.DataFrame(data, columns=['Candies (#)','Mangoes (Kg)','Milk Packets (#)'])
C = pd.DataFrame(data, columns=['Payment (Rs)'])
print('main matrix\n',data,'\n')
dim = data.shape
print('Dimensions: ',dim,'\n')
number_of_vectors = dim[0]
rank = np.linalg.matrix_rank(A)
print('Number of vectors: ',number_of_vectors,'\n')
print('A matrix\n',A,'\n')
print('Rank of A: ',rank,'\n')
print('C matrix\n',C,'\n')
Ainv = np.linalg.pinv(A)
# print('A inverse\n',Ainv,'\n')

# result = np.dot(Ainv,A)
# print('A inverse * A\n',result,'\n')

X = np.dot(Ainv,C)
print('X matrix\n',X,'\n')

print('cost of milk: ',X[0][0],'\n')
print('cost of mango: ',X[1][0],'\n')
print('cost of candy: ',X[2][0],'\n')
# check = np.dot(A,X)
# print('A * X\n',check,'\n')

# A3

data['Rich/Poor'] = np.where(data['Payment (Rs)'] >= 200, 'Rich', 'Poor')
print('data with rich/poor\n',data,'\n')

# A4


