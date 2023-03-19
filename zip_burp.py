import sys
import threading
import zipfile
import argparse
# 定义暴力破解函数
def Extarcat_zip(Zfile,password):
    try:
    
        """"
        破解方法不断的密码尝试
        param 密码字典
        password zip_passwd
        """
        Zfile.extractall(pwd=password.encode())
        print('Found Password:{} '.format(password))
        return password
    except:
        pass
        print('burp error')

        
         
# 定义主函数
def main():
    parser = argparse.ArgumentParser()
    print('[-h help] [-f DISTNAME] [-d ZIPNAME]')
    parser.add_argument('-f',type=str,dest='distname',help='please Dictionary path',default="")
    parser.add_argument('-d',type =str,dest ='zipname',help='please zipfile',default="")
    temp = parser.parse_args()
    zipname = temp.zipname
    distname = temp.distname
    Zfile = zipfile.ZipFile(zipname)
    Pass_File = open(distname)
    for line in Pass_File.readlines():
        if len(line) == 0:
            return 'This dictionary is None'
        else:
            PassWord = line.strip("\n")
    t = threading.Thread(target=Extarcat_zip,args=(Zfile,str(PassWord)))
    t.start()
if __name__=="__main__":
    main()

