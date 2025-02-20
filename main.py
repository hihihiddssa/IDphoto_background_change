from rembg import remove
import cv2
import numpy as np
from PIL import Image
import io

def change_background_to_white(input_path, output_path):
    # 1. 去除背景
    with open(input_path, 'rb') as i:
        input_image = i.read()
        # 使用rembg去除背景
        output_image = remove(input_image)
        
    # 将字节转换为PIL图像
    img = Image.open(input_path)
    # 创建白色背景
    white_background = Image.new('RGBA', img.size, (255, 255, 255, 255))
    # 将去除背景的图像转换为PIL图像
    transparent_img = Image.open(io.BytesIO(output_image))
    # 将透明图像粘贴到白色背景上
    white_background.paste(transparent_img, (0, 0), transparent_img)
    # 保存结果
    white_background.convert('RGB').save(output_path)

def main():
    input_path = r'D:\AMY_PROJECTS\NLP_learning\个人照片.png'  # 在字符串前加 r 表示原始字符串
    # 或者使用正斜杠：
    # input_path = 'D:/AMY_PROJECTS/NLP_learning/个人照片.png'
    output_path = '结果.png'   # 改为.png后缀以保持透明度
    
    try:
        change_background_to_white(input_path, output_path)
        print('处理完成！')
    except Exception as e:
        print(f'发生错误: {str(e)}')

if __name__ == '__main__':
    main()
