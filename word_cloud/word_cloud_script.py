import jieba
import wordcloud

# 创建并配置词云对象
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        scale=15)

# 读取文件文件
f = open('word.txt', encoding='utf-8')
txt = f.read()
# 关闭文件句柄
f.close()

# 使用jieba分词，获取分词结果
txt_list = jieba.lcut(txt)
# 对分词结果进行拼接
string = " ".join(txt_list)

# 将分词结果传递给词云绘制对象w
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file('out_img.png')
