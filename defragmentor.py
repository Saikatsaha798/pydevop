import os

c = 0
l = os.listdir()

nl = ('defragmentor.py', 'Images', 'Zips', 'Documents', 'Videos', 'Musics', 'Codes', 'Softwares', 'Others')

for i in nl:
    if i in l:
        l.remove(i)

imageext = ('.jpeg','.png','.ico','.jpg','.bmp')
zipext = ('.7z','.zip','.rar')
docsext = ('.docx','.txt','.csv','.odt','.doc','.pdf','.ppt','.pptx','.accdb','.db', '.xlsx')
videoext = ('.mp4','.mkv','.gif','.webm')
musicext = ('.mp3')
codesext = ('.py','.js','.bat','.cgi','.com','.jar')
appext = ('.exe','.msi')

def cine(name):
    if not os.path.exists(name):
        os.makedirs(name)

def aiinserter(file):
    ext = os.path.splitext(file)
    cwd = os.getcwd()
    extensions = {imageext : 'Images', zipext : 'Zips', docsext : 'Documents', videoext : 'Videos', musicext : 'Musics', codesext : 'Codes', appext : 'Softwares'}
    for x in list(extensions.keys()):
        if ext[-1].lower() in x:
            os.rename(f'{cwd}\\{file}',f'{cwd}\\{extensions[x]}\\{file}')
            break
    else:
        os.rename(f'{cwd}\\{file}', f'{cwd}\\Others\\{file}')

cine('Images')
cine('Zips')
cine('Documents')
cine('Musics')
cine('Codes')
cine('Softwares')
cine('Videos')
cine('Others')

for i in l:
    aiinserter(i)
    c += 1

print(f'{c} files have been defragmeted .....')