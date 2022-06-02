from pynput.keyboard import Key, Listener
import winsound

def Soundplay(filename):
    winsound.PlaySound(filename, winsound.SND_ASYNC)#winsound.SND_ASYNC的意思是当播放下一个音频时，上一个音频停止播放

def on_press(key):
    key_string=str(key)
    key_string=key_string[1:-1] #默认转出来的字符串是带两侧引号的，所以要去掉
    #print(type(key_string))
    print(key_string)
    if key_string=='1' or key_string=='97':
        Soundplay('do.wav')
    if key_string=='2' or key_string=='98':
        Soundplay('re.wav')
    if key_string=='3' or key_string=='99':
        Soundplay('mi.wav')
    if key_string=='4' or key_string=='100':
        Soundplay('fa.wav')
    if key_string=='5' or key_string=='101':
        Soundplay('so.wav')
    if key_string=='6' or key_string=='102':
        Soundplay('la.wav')
    if key_string=='7' or key_string=='103':
        Soundplay('xi.wav')
    if key_string=='8' or key_string=='104':
        Soundplay('dogao.wav')
    if key_string=='9' or key_string=='105':
        Soundplay('regao.wav')
    if key_string=='-' or key_string=='+':
        Soundplay('migao.wav')
    if key_string == 'ey.backspac' or key_string == 'ey.ente':
        Soundplay('fagao.wav')
    print(key_string)


def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()