import time
import datetime

def run(n):
    i=0
    with open("testpoint.txt",'a+',encoding='utf-8') as f:
        f.write('\n'+str(datetime.datetime.now().strftime('%H:%M:%S'))+'  →  ')
        while i < int(n):
            print(i)
            f.write(str(i))
            i +=1
            time.sleep(1)
        f.write('\n')
        
if __name__=='__main__':
    n=input('输入多少秒')
    run(n)