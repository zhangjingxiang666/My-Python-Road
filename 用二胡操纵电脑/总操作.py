import pyautogui#pyautogui使用0.9.2版本
import pyaudio
import wave
import librosa
import numpy
import matplotlib.pyplot as plt
import librosa.display

'''录音参数的设置'''
CHUNK = 1024  # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16  # 采样位数
CHANNELS = 1  # 单声道
RATE = 44100  # 采样频率
'''录音函数的定义'''
def record_audio(wave_out_path, record_second):
    p = pyaudio.PyAudio()  # 实例化对象
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # 打开流，传入响应参数
    wf = wave.open(wave_out_path, 'wb')  # 打开 wav 文件。
    wf.setnchannels(CHANNELS)  # 声道设置
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 采样位数设置
    wf.setframerate(RATE)  # 采样频率设置
    for _ in range(0, int(RATE * record_second / CHUNK)):
        data = stream.read(CHUNK)
        wf.writeframes(data)  # 写入数据
    stream.stop_stream()  # 关闭流
    stream.close()
    p.terminate()
    wf.close()

'''鼠标操作函数的定义'''
def right_move():
    pyautogui.moveTo(x+30,y,duration=0.1) #0.1秒内右移30个像素.此处x、y的值在后面【4. 获取鼠标当前位置】那一步即可获得
def down_move():
    pyautogui.moveTo(x,y+30,duration=0.1)
def left_move():
    pyautogui.moveTo(x-30,y,duration=0.1)
def up_move():
    pyautogui.moveTo(x,y-30,duration=0.1)
def mouse_upscroll(): #向上滚动50个像素
    pyautogui.scroll(50)
def mouse_downscroll():
    pyautogui.scroll(-50)
def mouse_click(): #鼠标单击
    pyautogui.click()


while True: #死循环--一直运行
    '''1. 录音'''
    record_audio('d.wav',0.4)   #录音0.4秒，保存为d.wav

    '''2. 处理声音得到时变频谱矩阵'''
    sound,sr = librosa.load("d.wav", sr=1600)   #1600Hz为对录音采样的频率。后续时变频谱矩阵中横坐标的最大频率为采样频率的一半即800Hz
    Sound_After_Fourier = librosa.stft(sound,win_length=500)    #对声音进行傅里叶变换，拆解成不同频率
    Xdb = librosa.amplitude_to_db(abs(Sound_After_Fourier))   # 把幅度转成分贝格式。
    '''Xdb就是时变频谱矩阵。
    时变频谱矩阵的纵坐标为声音频率,
                  横坐标为时间。
                  单元格值为响度（即声音在该时间于该频率上的振幅）。'''

    '''为了便于理解，此处可以用以下四行代码将时变频谱矩阵以热图的形式plot出来。图的纵坐标为声音频率,横坐标为时间，每个单元格的颜色深度为响度。
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.show()'''

    '''3. 从时变频谱矩阵中找到每个音符的基音对应的行
    二胡控制的思路是：找到该音调的基音频率在时变频谱矩阵中的那一行。对该行的单元格值（响度）求时间上的平均值。如果平均值较大则说明有这个音'''
    avg_re = numpy.mean(Xdb[422])  # re音的基音【329.5Hz左右】在时变频谱矩阵中的行，为第433行左右。要是觉得不准，这个值可以自己调
    print('re的强度为',avg_re)
    avg_mi = numpy.mean(Xdb[477])  # mi音所在的行
    #print('mi的强度为',avg_mi)
    avg_fa = numpy.mean(Xdb[515])  # fa音所在的行
    #print('fa的强度为',avg_fa)
    avg_so=numpy.mean(Xdb[567])#so音所在的行
    #print('so的强度为',avg_so)
    avg_la=numpy.mean(Xdb[630])#la音所在的行
    #print('la的强度为',avg_la)
    avg_xi=numpy.mean(Xdb[710])#xi音所在的行
    #print('xi的强度为',avg_xi)
    avg_do=numpy.mean(Xdb[760])#高音do所在的行
    #print('高音do的强度为',avg_do)


    '''4. 获取鼠标当前位置'''
    mouse_position=pyautogui.position()
    #获取的位置是一个元组型数据。第1个值mouse_position[0]为x坐标，第2个值mouse_position[1]为y坐标
    x=mouse_position[0]
    y=mouse_position[1]

    '''5. 操作鼠标'''
    if avg_re>-55:  #如果re音的基音（时变频谱矩阵中的第433行）振幅的平均值大于-52，则说明有这个音。【觉得不准的话，这个阈值可以自己调】
        up_move()    #有re音的话则启动上面定义的right_move()函数，使鼠标向右移
    if avg_mi>-55:
        left_move()
    if avg_fa>-40:
        down_move()
    if avg_so>-30:
        right_move()
    if avg_la>-35:
        mouse_upscroll()
    if avg_xi>-30:
        mouse_downscroll()
    if avg_do>-30:
        mouse_click()