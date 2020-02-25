from wordcloud import WordCloud, ImageColorGenerator
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Read the whole text.
text = open('C:/Richard/R and Python/Kaggle/Blog.txt').read()
cachedStopWords = stopwords.words("german")
cachedStopWords.append("Da")
cachedStopWords.append("dass")
text = ' '.join([word for word in text.split() if word not in cachedStopWords])
text=text.decode('unicode-escape')
#text.replace(u'\xed', 'i')


alice_mask = np.array(Image.open("C:/Richard/R and Python/Kaggle/Mask.png"))


# lower max_font_size
wordcloud = WordCloud(max_font_size=100,background_color="white", max_words=1000, 
	mask=alice_mask).generate(text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
