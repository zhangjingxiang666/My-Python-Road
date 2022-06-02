import winsound
import pyautogui
import time

from pynput import mouse

def Soundplay(filename):
    winsound.PlaySound(filename, winsound.SND_ASYNC)#winsound.SND_ASYNC的意思是当播放下一个音频时，上一个音频停止播放

def main():
    while True:
        a=pyautogui.position()#先检测一下鼠标位置
        x1=a[0]
        y1=a[1]
        #print(x1,y1)
        time.sleep(0.1)#0.1秒后再检测一下鼠标位置
        b=pyautogui.position()
        x2=b[0]
        y2=b[1]
        #print(x2,y2)

        if y2-y1<0 and abs(y2-y1)>abs(x2-x1):
            Soundplay('do.wav')
            #print('向上挪')
        if y2-y1>0 and abs(y2-y1)>abs(x2-x1):
            Soundplay('re.wav')
            #print('向下挪')
        if x2-x1>0 and abs(y2-y1)<abs(x2-x1):
            Soundplay('mi.wav')
            #print('向右挪')
        if x2-x1<0 and abs(y2-y1)<abs(x2-x1):
            Soundplay('fa.wav')
           #print('向左挪')

if __name__=='__main__':
    main()




