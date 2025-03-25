# 🎧 Playlist Generator

Una aplicación web interactiva que recomienda canciones basadas en el estado emocional del usuario, utilizando clustering de datos musicales. Construida con Python, Flask, y datos reales de más de 20.000 canciones extraídas desde una fuente abierta.

---

## 🧠 Objetivo del Proyecto

Desarrollar un sistema de recomendación de playlists personalizadas basado en las características acústicas de las canciones, con el fin de sugerir música alineada al estado emocional del usuario.

---

## 🚀 Demo local

Puedes ejecutar la app localmente y probarla accediendo a:

[Playlist Generator](https://playlistgenerator-vwec.onrender.com/)


---

## 🧪 Tecnologías utilizadas

- Python 3
- Jupyter Notebook
- Flask
- Pandas / Scikit-learn / Matplotlib / Seaborn
- HTML + Bootstrap (visual simple)

---

## 🧬 Metodología

1. **Dataset:** Más de 20.000 canciones con variables como valence, energy, danceability y tempo. Obtenido desde [Google Dataset Search](https://datasetsearch.research.google.com/), redirigido a Kaggle.

2. **EDA:** Análisis exploratorio para entender la distribución emocional de las canciones.

3. **Clustering:** Uso de K-Means para agrupar canciones según características acústicas en distintos "moods".

4. **Recomendación:** El usuario elige una emoción y la app recomienda canciones del cluster más alineado a ella.

5. **Migración a web:** El código fue trasladado a Flask y desplegado como una app web funcional.

---

## 🎯 Características principales

- Selección de emoción por parte del usuario
- Recomendación de canciones alineadas al estado emocional
- Botón para regenerar una nueva playlist con la misma emoción
- Botón para cambiar de emoción
- Flujo intuitivo y 100% funcional localmente

---

## 🛠️ Instalación local

1. **Clona este repositorio:**
   ```bash
   git clone git clone https://github.com/affec-ds/Playlist-Generator.git
