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

ts_3 = time.time()
os.chdir('../symetry')
os.system('python symetry.py')

ts_end = time.time()
