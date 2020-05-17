import pickle
file=open("QlearningData","rb")

l=pickle.load(file)
print(l,sep="\n")
