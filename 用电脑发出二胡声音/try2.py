from pynput.mouse import Listener

def on_move(x, y):
    global x1,y1
    print('Pointer moved to {0}'.format(
        (x, y)))

with Listener(
        on_move=on_move,
        on_click=None,
        on_scroll=None) as listener:
    listener.join()






