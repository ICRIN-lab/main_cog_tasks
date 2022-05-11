import os
import time

ts = time.time()
os.chdir('../seven_diff/')
os.system('python seven_diff.py')

ts_1 = time.time()
os.chdir('../lucifer')
os.system('python lucifer.py')

ts_2 = time.time()
os.chdir('../where_is_tockie')
os.system('python where_is_tockie.py')

<<<<<<< HEAD
os.chdir('../symmetry')
os.system('python symmetry.py')
=======
ts_3 = time.time()
os.chdir('../symetry')
os.system('python symetry.py')

ts_end = time.time()

L = [ts, ts_1, ts_2, ts_3, ts_end]
print("time stamps : ", L)

>>>>>>> e9914d843876c23aff8ba9e6a669a9ee19098817
