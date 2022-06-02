import pyautogui
import time
import winsound

def Soundplay(filename):
    winsound.PlaySound(filename, winsound.SND_ASYNC)

while True:
    a=pyautogui.position()
    x1=a[0]
    y1=a[1]
    print(x1,y1)
    time.sleep(0.1)

    b=pyautogui.position()
    x2=b[0]
    y2=b[1]
    print(x2,y2)

    #将挪动区域分成8个象限：左上上、左左上、左左下、左下下、右下下、右右下、右右上、右上上
    Derta_x=abs(x2-x1)
    Derta_y=abs(y2-y1)

    if y2-y1<0 and x2-x1<0 and Derta_x<Derta_y:#左上上
        Soundplay('do.wav')
    if y2-y1<0 and x2-x1<0 and Derta_x>Derta_y:#左左上
        Soundplay('re.wav')
    if y2-y1>0 and x2-x1<0 and Derta_x>Derta_y:#左左下
        Soundplay('mi.wav')
    if y2-y1>0 and x2-x1<0 and Derta_x<Derta_y:#左下下
        Soundplay('fa.wav')
    if y2-y1>0 and x2-x1>0 and Derta_x<Derta_y:#右下下
        Soundplay('so.wav')
    if y2-y1>0 and x2-x1>0 and Derta_x>Derta_y:#右右下
        Soundplay('la.wav')
    if y2-y1<0 and x2-x1>0 and Derta_x>Derta_y:#右右上
        Soundplay('xi.wav')
    if y2-y1<0 and x2-x1>0 and Derta_x<Derta_y:#右上上
        Soundplay('dogao.wav')
    time.sleep(0.1)
