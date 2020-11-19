import os
ten="0001"
file_goc =os.getcwd() #lay file goc
file_txt_can=file_goc+'/config/'+ten+'.txt'# ten file txt du lieu

file_image=file_goc+'/image_function/'+ten+'.jpg'
flie_image_cut=file_goc+'/cut_image_function/'+ten+'.jpg'



ten=int(ten)


file_cofig=os.listdir(file_goc+'/config')#list file /config
file_image_list=os.listdir(file_goc+'/image_function')
file_image_cut_list=os.listdir(file_goc+'/cut_image_function')



file_cofig=sorted(file_cofig,reverse=True)
leng_file=len(os.listdir(file_goc+'/config'))


file_image_list = file_image_list[::-1]
file_image_cut_list = file_image_cut_list[::-1]
file_cofig = file_cofig[::-1]

os.remove(file_txt_can)
file_1=file_goc+'/config'+'/'+file_cofig[ten]
file_2=file_goc+'/config'+'/'+file_cofig[ten-1]
print (file_1)
print(file_2)
for i in range(ten,leng_file):
    file_1=file_goc+'/config'+'/'+file_cofig[i]
    file_2=file_goc+'/config'+'/'+file_cofig[i-1]
    os.rename( file_1,file_2 )







    
list_ten=os.listdir(file_goc+'/config')
list_ten=sorted(list_ten,reverse=True)
list_ten = list_ten[::-1] 
leng_file=len(os.listdir(file_goc+'/config'))                  
print(leng_file)
for i in range(0,leng_file-1):
    ten=int(i)
    file_config=file_goc+'/config/'+list_ten[ten]
    print(file_config)
    studentList = []
    File = open (file_config, "r")
    #print(File)
    studentList = File.readlines()
   # print(studentList)
#studentList[0]="adas\n"
    ten_1=studentList[0]
    ten_2=studentList[1]
    str_1="config"
    vitri=ten_1.find(str_1)
    vitri_2=ten_2.find(str_1)

    str_ten_thay=ten_1[vitri+7:vitri+11]
    str_ten_thay_2=ten_2[vitri+7:vitri+11]
    
    str_canthay=file_config[vitri+7:vitri+11]
    
    studentList[0]=ten_1.replace(str_ten_thay,str_canthay)
    studentList[1]=ten_2.replace(str_ten_thay_2,str_canthay)
    File_1 = open (file_config, "w")
    File_1.writelines(studentList)

    File_1.close()
