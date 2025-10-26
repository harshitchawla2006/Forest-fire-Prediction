# Forest Fire Prediction using Ridge Regression

A Flask web application that predicts the Fire Weather Index (FWI) for forest fires using Ridge Regression machine learning model.

## 🚀 Features

- Machine Learning model trained on Algerian Forest Fires dataset
- Ridge Regression algorithm for FWI prediction
- Interactive web interface built with Flask
- Input form for weather and fire danger parameters
- Real-time predictions with visualization

## 📋 Prerequisites

- Python 3.7+
- pip

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the trained models (or train your own):
   - Place `ridge.pkl` in the `models/` folder
   - Place `sc.pkl` in the `models/` folder

## 🎯 Usage

1. Run the Flask application:
```bash
python application.py
```

2. Open your browser and navigate to:
```
http://localhost:5000/predictdata
```

3. Enter the following parameters:
   - Temperature (°C)
   - RH (Relative Humidity %)
   - Ws (Wind Speed km/h)
   - Rain (mm)
   - FFMC (Fine Fuel Moisture Code)
   - DMC (Duff Moisture Code)
   - ISI (Initial Spread Index)
   - Classes (0 for not fire, 1 for fire)
   - Region (0 or 1)

4. Click "Predict" to get the FWI prediction

## 📊 Model Performance

- **Algorithm**: Ridge Regression
- **R² Score**: 0.984
- **Mean Absolute Error**: 0.564

## 📁 Project Structure

```
.
├── application.py          # Main Flask application
├── requirements.txt        # Python dependencies
├── models/                 # Trained models (ridge.pkl, sc.pkl)
│   ├── ridge.pkl          # Trained Ridge Regression model
│   └── sc.pkl             # Standard Scaler
├── templates/              # HTML templates
│   ├── index1.html        # Home page
│   ├── home.html          # Prediction form
│   ├── success.html       # Prediction result page
│   └── error.html         # Error page
├── notebooks/              # Jupyter notebooks for analysis
│   └── Algerian_forest_dataset.ipynb
└── Learnings/              # Learning and practice notebooks
```

## 🔧 Model Training

The model was trained on the Algerian Forest Fires Dataset with the following features:
- Features used: Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region
- Dropped features: DC, BUI (due to high correlation)
- Target variable: FWI (Fire Weather Index)

## 🌐 API Endpoints

- `GET /` - Home page
- `GET /predictdata` - Display prediction form
- `POST /predictdata` - Process prediction and return results

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Your Name

## 🙏 Acknowledgments

- Algerian Forest Fires Dataset
- scikit-learn for machine learning tools
- Flask for web framework
