from pynput.mouse import Listener
import winsound
#import Move

def Soundplay(filename):
    winsound.PlaySound(filename, winsound.SND_ASYNC)#winsound.SND_ASYNC的意思是当播放下一个音频时，上一个音频停止播放

def on_move(x, y):
    pass
    '''print('Pointer moved to {0}'.format((x, y)))'''

def on_click(x, y, button, pressed):
    if pressed:
        Soundplay('so.wav') #鼠标按下去是so
    else:
        Soundplay('la.wav') #抬起来是la
    '''print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False'''

def on_scroll(x, y, dx, dy):
    Soundplay('xi.wav') #滚动滚轮是xi
    '''print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))'''
def main():
    with Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:   #listener的类型为Treading.treading()
        listener.join()

if __name__=='__main__':
    main()