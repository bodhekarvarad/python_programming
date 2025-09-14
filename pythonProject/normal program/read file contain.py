try:
    f=open('d:/myfile.txt','rt')
    print(f.read())
    f.close()
except:
    print("file not found")
