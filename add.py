def File_Seek_Fun():
    f=open('test1.txt','r')
    f.seek(7)
    f_data=f.read()
    print('Content of f_data is =',f_data)
    f.close()
File_Seek_Fun()