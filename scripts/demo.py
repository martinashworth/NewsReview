import os
import shutil
import datetime

# define source directories where demo data can be found
src0 = '../archive/demo1'
src1 = '../archive/demo1'
src2 = '../archive/demo2'
src3 = '../archive/demo3'
src4 = '../archive/demo4'
src5 = '../archive/demo5'
src6 = '../archive/demo6'

# define current (datestamped) directories to be populated if missing
dst0 = f'../archive/{datetime.date.today()}'
dst1 = f'../archive/{(datetime.date.today() - datetime.timedelta(days=+1))}'
dst2 = f'../archive/{(datetime.date.today() - datetime.timedelta(days=+2))}'
dst3 = f'../archive/{(datetime.date.today() - datetime.timedelta(days=+3))}'
dst4 = f'../archive/{(datetime.date.today() - datetime.timedelta(days=+4))}'
dst5 = f'../archive/{(datetime.date.today() - datetime.timedelta(days=+5))}'
dst6 = f'../archive/{(datetime.date.today() - datetime.timedelta(days=+6))}'

# lists of source and destination directories
src = (src0, src1, src2, src3, src4, src5, src6)
dst = (dst0, dst1, dst2, dst3, dst4, dst5, dst6)

# zip together the lists of directories
copies = zip(src, dst)

# copy from source to destination directory in cases where the destination is missing
[shutil.copytree(src, dst) for (src, dst) in (copies) if os.path.exists(dst) is False]

# run analysis
import analysis
