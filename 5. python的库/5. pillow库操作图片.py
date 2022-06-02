from PIL import Image, ImageFilter
image = Image.open('D:/杂/图片/衡水/1.jpeg')
print(image.format, image.size, image.mode)#图像信息
image.show()

#裁剪图像
def cut():
    image = Image.open('D:/杂/图片/衡水/1.jpeg')
    rect = 80, 20, 310, 360
    image.crop(rect).show()

#生成缩略图
def suolue():
    image = Image.open('D:/杂/图片/衡水/1.jpeg')
    size = 128, 128
    image.thumbnail(size)
    image.show()

def fugu():
    image = Image.open('D:/杂/图片/衡水/1.jpeg')#先显示一下原图
    image.filter(ImageFilter.CONTOUR).show()#再显示处理后的图片

def main():
    fugu()

main()



