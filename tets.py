import pickle

with open('con.dat', 'wb') as f:
    pickle.dump([1,2,3], f)
