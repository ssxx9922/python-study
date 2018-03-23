import os
from PIL import Image

def open():
    g=os.walk("/Users/yy/Downloads/bubbleIcon")
    for path,d,filelist in g:  
        for filename in filelist:
            if filename.endswith('png'):
                print (os.path.join(path, filename))
                dispose(os.path.join(path, filename),filename)

def dispose(path,name):
    im = Image.open(path)
    w, h = im.size
    new_name = name[0:-4]
    im.save(new_name+'@3x.png', 'png')
    im.thumbnail((w//2, h//2))
    im.save(new_name+'@2x.png', 'png')
    im.thumbnail((w//3, h//3))
    im.save(new_name+'.png', 'png')
    


open()