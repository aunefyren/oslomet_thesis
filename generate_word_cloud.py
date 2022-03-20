# Get modules
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
import pandas as pd
import json
import numpy as np
from PIL import Image
from os import path
import os

# Define variables
comment_words = ''
stopwords = set(STOPWORDS)
directory = 'words'

# Import PNG of Norwegian flag for mask and coloring
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
norwegian_flag = np.array(Image.open(path.join(d, "norwegian_flag.png")).convert('RGB'))

# create mask  white is "masked out"
norwegian_flag_mask = norwegian_flag.copy()
norwegian_flag_mask[norwegian_flag_mask.sum(axis=2) == 0] = 255

# some finesse: we enforce boundaries between colors so they get less washed out.
# For that we do some edge detection in the image
edges = np.mean([gaussian_gradient_magnitude(norwegian_flag[:, :, i] / 255., 2) for i in range(3)], axis=0)
norwegian_flag_mask[edges > .08] = 255

# Iterate over files in words directory, checking each file and adding words to stopwords
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # If the path is a file
    if os.path.isfile(f):
        text = open(f, encoding="utf-8").read()
        stopword_array = text.split()
        for word in stopword_array:
            stopwords.add(word.lower())


# Generate variable with words found in Tweets within tweets.json
with open('tweets.json', encoding='utf-8') as file:
    tweets = json.load(file)
    for i, row in enumerate(tweets):
        user_id = tweets[i]['user_id']

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        
        comment_words += " ".join(tokens)+" "


# Create wordcloud, 2000x2000, grey background color, no collocations, none of the stopwords
wordcloud = WordCloud(width = 2000, height = 2000,
				background_color ='white',
                mask = norwegian_flag_mask,
				stopwords = stopwords,
                collocations = False,
				min_font_size = 10).generate(comment_words)

# Create coloring from image
image_colors = ImageColorGenerator(norwegian_flag)

# Create and show grapich, color using the coloring created earlier
plt.figure()
plt.imshow(wordcloud.recolor(color_func = image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()
