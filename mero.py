import os
filepath = '/my/directory/filename.txt'
script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, filepath)
directory = os.path.dirname(dest_dir)
print directory
import errno
if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
with open(filepath, 'w') as my_file:
    print("hello world in the new file")
