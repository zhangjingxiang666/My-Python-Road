import pyautogui#pyautogui使用0.9.2版本
mouse_position=pyautogui.position()
x=mouse_position[0]
print(x)
y=mouse_position[1]
print(y)
def x_positive_move():
    pyautogui.moveTo(x+10,y,duration=0.1)

def y_positive_move():
    pyautogui.moveTo(x,y+10,duration=0.1)

def x_negative_move():
    pyautogui.moveTo(x-10,y,duration=0.1)

def y_negative_move():
    pyautogui.moveTo(x,y-10,duration=0.1)



