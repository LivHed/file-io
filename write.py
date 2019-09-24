f = open("newfile.txt", "a") #a stands for append (before we had w whcih stands for write)
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.writelines(text) 
f.close()