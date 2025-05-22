# Color_Detector 

A web-based application built with Streamlit to detect the most dominant color in an image. The app allows users to upload an image or capture an image using the webcam, and it will return the name of the color and its hex code selected by the user.


## 📂 Project Structure

    Color_Detector/
    │
    ├── views/                             
    │   ├── image_color_detection.py       
    │   └── web_color_detection.py
    ├── data/                             
    │    └── colors.csv
    ├── app.py
    ├── README.md
    ├── LICENSE  
    └── requirements.txt             
    
## 🚀 Features
   - Streamlit web app with custom navigation 
   - Upload an image to detect its dominant color
   - Display the color's name and its hex code


## 🛠️ Setup Instructions

### 1. Clone the Repository
    
    git clone https://github.com/Dhivakar2005/Color_Detector.git
    cd Color_Detector

### 2. Create a Virtual Environment
    
    python -m venv cenv

### 3. Activate the Environment 

    .\cenv\Scripts\activate

### 4. Install Dependencies
    
    pip install -r requirements.txt


### 5. Run the App
streamlit run app.py


## 🤝 Contributing

Contributions are welcome! Whether it's bug fixes, improvements, documentation updates, or new features — your help is appreciated.


## 📌 Guidelines
- Keep code clean and well-documented

- Write descriptive commit messages

- Try to maintain consistency with existing code style

- Always test your changes before submitting

## 📃 License

This project is licensed under the MIT License.



