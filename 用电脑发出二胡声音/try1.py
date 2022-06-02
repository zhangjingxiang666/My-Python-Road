from pynput.mouse import Listener
import time

def on_move1(x1, y1):
    return x1,y1
    print('Pointer moved to {0}'.format(
        (x1, y1)))

def on_move2(x2, y2):
    return x2,y2
    print('Pointer moved to {0}'.format(
        (x2, y2)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

# Collect events until released
with Listener(
        on_move=on_move1,
        on_click=on_click,
        on_scroll=on_scroll) as listener1:
    listener1.join()

with Listener(
        on_move=on_move1,
        on_click=on_click,
        on_scroll=on_scroll) as listener2:
    listener2.join()
