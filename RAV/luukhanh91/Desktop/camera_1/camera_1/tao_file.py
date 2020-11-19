import os
file_goc=os.getcwd()
file_config=file_goc+"/config/"
for i in range (1,100):
    length=len (str(i))
    if length==1:
        ten="000"+str(i)
    if length==2:
        ten="00"+str(i)
    if length==3:
        ten="0"+str(i)
    filedata=file_config+ten+".txt"
    detection_color_file = open(filedata, 'w')
    detection_color_file.write(filedata+"\n")
    detection_color_file.write(filedata+"\n")
