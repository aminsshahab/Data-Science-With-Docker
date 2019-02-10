import ccxt
from sklearn import datasets

print(ccxt.exchanges) # print a list of all available exchange classes

print(" ")

iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data)