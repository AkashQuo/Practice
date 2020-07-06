import os

print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))  

print(os.path.join('/Users/pilgrim/diveintopython3/examples', 'humansize.py'))    

print(os.path.expanduser('~'))      

print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py')) 
