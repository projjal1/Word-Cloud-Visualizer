#Import modules
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt 
from PIL import Image 
import numpy as np

#Reading data from file
file=open('text.txt',encoding='utf-8')
data=' '.join(file.readlines())

#wordcloud object
wc=WordCloud(max_font_size=40)

#Generating cloud
wc.generate(data)

#Saving image
wc.to_file('visualize.png')

#Matplotlib plot
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
