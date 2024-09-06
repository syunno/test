import streamlit as st # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from PIL import Image

import time
#C:\Users\81802\OneDrive\デスクトップ\stre
#streamlit run main.py

st.title("Streamlit 入門")

st.write("Display Image")

'Start!'
latest_iteration=st.empty()

bar=st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)








if st.checkbox('Show Image'):

 img=Image.open('Hakari.jpg')
               
 st.image(img,caption="Hakari Kinji",use_column_width=True)


left_column,right_column=st.columns(2)

button=left_column.button('右カラムに文字を表示')

if button:
  right_column.write('ここは右カラム')

expander=st.expander('問い合わせ')
expander.write('問い合わせ内容を記載')
#option=st.selectbox('あなたの好きな数字は何ですか？',list(range(1,11)))

#'あなたの好きな数字は、',option,'です'

#text=st.text_input('あなたの趣味は何ですか？')
#'趣味：',text
#cond =st.slider('あなたの今の調子は？',0,100,50)
#'コンディション：',cond


