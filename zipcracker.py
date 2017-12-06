import zipfile
print("""
***************************************************************************************************************
!!!!! KEEP YOUR ZIP FILE, PASSWORD LIST/DICTIONARY AND THIS PROGRAM IN THE SAME FOLDER. !!!!!

Made by Picha
One day you'll know me for sure...
***************************************************************************************************************
""")
zipfilename = input("Enter your (.zip)file's name:")
dictionary = input("Enter your (.txt)file's name:")

zip_file = zipfile.ZipFile(zipfilename)
with open(dictionary, 'r',encoding="utf-8") as file:
	for line in file.readlines():
		password = line.strip('\n')
		try:
			zip_file.extractall(pwd=password)
		except:
			pass
print("Password :", password)
