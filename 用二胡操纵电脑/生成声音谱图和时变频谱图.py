#加载声音
import librosa
import numpy
x,sr = librosa.load("a.wav", sr=1600)
print(x.shape, sr)

#生成声音的频谱图
import matplotlib.pyplot as plt
import librosa.display
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)
plt.show()

#画出时变频谱图
X = librosa.stft(x,win_length=500)#傅里叶变换
Xdb = librosa.amplitude_to_db(abs(X))   # 把幅度转成分贝格式
print(type(Xdb))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb,sr=sr,x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()
'''时变频谱图横轴为时间，纵轴为频率，颜色深度为声音强度'''

import numpy
#print("数组的维度数目",Xdb.ndim)      #打印数组的维度数目
numpy.savetxt( "Xdb.csv", Xdb, delimiter=",")
print(Xdb[567])

print(numpy.mean(Xdb[567]))





