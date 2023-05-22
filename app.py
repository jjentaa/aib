import streamlit as st 
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from imageio import imread
from sentence_transformers import SentenceTransformer, util

st.title("Manga Recommendation 📚")

feedback = ''

df = pd.read_csv("data/df.csv")

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings_des = torch.load("data/embeddings_des.pt")
all_index = np.load("data/all_index.npy")

query = st.text_input('Enter query : ex. What manga has a character who is smooth and cool at work but a total softie at home?')

if(query):
    query_en = model.encode(query, convert_to_tensor=True)
    cosine_scores = util.cos_sim(query_en, embeddings_des)

    all_idx = torch.topk(cosine_scores.flatten(), 5).indices
    print(all_idx)
    st.write("We recommend : ")
    for i in range(len(all_idx)):
        print(i+1, df.loc[all_index[int(i)], "title"])
        st.write(f'{i+1}. {df.loc[all_index[int(i)], "title"]}')
        img_url = df.loc[int(i), "cover"]

        # show cover
        # img = imread(img_url)
        # plt.imshow(img)
        # plt.show()

fb = st.text_input('Enter Feedback :')

if(fb):
    feedback+=fb+'\n'

st.download_button('Download Feedback', feedback)
