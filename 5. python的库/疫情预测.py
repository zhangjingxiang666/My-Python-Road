import numpy as np #导入数值计算模块
import pandas as pd #导入数据处理模块
import matplotlib.pyplot as plt #导入绘图模块
from scipy.optimize import curve_fit #导入拟合模块
plt.rcParams["font.sans-serif"]="SimHei" #黑体中文
plt.rcParams["axes.unicode_minus"]=False #显示负号
data=pd.read_csv("D/users/desktop/工作簿1.csv") #读取数据
date=data['date'] #日期
confirm=data['confirm'] #确诊数
t=range(len(confirm)) #构造横轴
print(data)

fig=plt.figure(figsize=(10,4)) #建立画布
ax=fig.add_subplot(1, 1, 1)
ax.scatter(t,confirm, color="k", label="确诊人数") #真实数据散点图
#ax.set_xlabel("天数") #横坐标
ax.set_ylabel("确诊人数") #纵坐标
ax.set_title("确诊人数随时间变化情况") #标题
ax.set_xticklabels(['', '1月13号', '1月23号', '2月2号', '2月10号','2月20号'], rotation=30, fontsize=10) #自定义横坐标标签

def logistic(t,K,P0,r): #定义logistic函数
    exp_value=np.exp(r*(t))
    return (K*exp_value*41)/(K+(exp_value-1)*41)

coef, pcov = curve_fit(logistic, t, confirm) #拟合
print(coef) #logistic函数参数
y_values = logistic(t,coef[0], coef[1], coef[2]) #拟合y值
ax.plot(t,y_values,color="blue", label="拟合曲线") #画出拟合曲线

x=np.linspace(23,46,24) #构造期货日期
y_predict=logistic(x,coef[0], coef[1], coef[2]) #未来预测值
ax.scatter(x,y_predict, color="green",label="未来预测") #未来预测散点
ax.legend() #加标签


