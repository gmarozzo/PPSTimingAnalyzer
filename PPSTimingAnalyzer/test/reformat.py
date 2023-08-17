filein = open("filelist.txt","r")
fileout = open("filelist2.txt","w")

for line in filein:
  fileout.write('      "'+line.strip()+'",\n')
