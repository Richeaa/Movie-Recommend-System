# 🎬 Movie Recommender System

A content-based movie recommendation app built using **Streamlit** and **TensorFlow**.  
This app suggests similar movies based on your selected title, leveraging a pretrained model with cosine similarity.

🚀 **Live App**: [rich-movie-recommend-system.streamlit.app](https://rich-movie-recommend-system.streamlit.app/)

---

## 📸 Preview

![Demo Screenshot](https://rich-movie-recommend-system.streamlit.app/_static/favicon.png)  
> Select a movie and get recommendations with posters instantly.

---

## ⚙️ Features

✅ Recommend movies based on a selected title  
✅ Show poster images using TMDb API  
✅ Fast model loading from `.pkl` file  
✅ Google Drive integration with `gdown`

---

## 🧠 How It Works

- Uses **cosine similarity** between movie vectors
- Movie metadata and vector data precomputed and loaded from `similarity.pkl`
- Poster images fetched from **TMDb API**

---

## 🧪 Tech Stack

- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Pandas](https://pandas.pydata.org/)
- [TMDb API](https://www.themoviedb.org/documentation/api)
- [gdown](https://pypi.org/project/gdown/)

---
