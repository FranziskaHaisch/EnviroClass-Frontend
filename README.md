# EnviroClass – Exploring Environmental Wildfire Patterns with Satellite Data

**EnviroClass** is an interactive app developed to detect wildfires and classify land cover types based on satellite imagery.  
It uses deep learning models to identify environmental features such as forests, rivers, agricultural zones, and urban areas.

> 🚫 **Note:** The app is currently not deployed, as the trial period for our Google Cloud Platform environment has ended.  
> However, the full codebase and model logic are documented in this repository and the backend repository (see below).

---

## 🧠 How it works

- **YOLOv8**: Used to classify environmental land cover (e.g. rivers, agriculture, urban areas)
- **CNNs**: Used to detect wildfire-affected areas
- **Frontend**: Built with Streamlit for interactivity and visualization
- **Backend**: Provided API endpoints using FastAPI

---

## 📁 Repositories

- 🔹 **Frontend (this repo):** Streamlit UI, data visualizations, app logic  
- 🔹 **[Backend Repository](https://github.com/FranziskaHaisch/EnviroClass):** Model training, data processing, FastAPI server

---

## 🛠️ Tech Stack

- **Languages:** Python  
- **Frameworks:** Streamlit, FastAPI  
- **Models:** YOLOv8, CNNs (TensorFlow/Keras)  
- **Tools:** Docker, Jupyter Notebooks  
- **Cloud:** Google Cloud Platform  
- **Data Sources:** Curated Kaggle datasets

---

## 👩‍💻 Contributors

- Bhupen Dabholkar – [GitHub](https://github.com/bhupen-git) | [LinkedIn](https://www.linkedin.com/in/bhupen-dabholkar-1291221b2/)  
- Franziska Haisch – [GitHub](https://github.com/FranziskaHaisch) | [LinkedIn](https://www.linkedin.com/in/franziska-haisch-26125234b)  
- Lukas Berger – [GitHub](https://github.com/Luulyberg) | [LinkedIn](https://www.linkedin.com/in/lb341ab39a/)  
- Therese Hempel – [GitHub](https://github.com/Theresaurus) | [LinkedIn](http://www.linkedin.com/in/therese-hempel)

---

## 📄 License

This project was created for educational purposes during the [Le Wagon Data Science & AI Bootcamp](https://www.lewagon.com/) (Berlin, 2024).  
No commercial use intended. If you'd like to reuse any part of the code, feel free to fork or reference – proper attribution is appreciated.
