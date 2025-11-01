🚗AI POWERED Tint Detection & Compliance System  

> Detect tinted car windows.  
> Check compliance.  
> Predict violations.  
> All using Computer Vision and Machine Learning.  

🧭 Overview  

Too many vehicles on the road violate tint regulations — often unnoticed.  
This project changes that.  
It’s an AI-powered system that automatically detects window tint levels in vehicles using **OpenCV** and **Python**.  
If a car exceeds the legal transparency limit, the system triggers an instant alert — visual, audio, and logged for record.  

What makes it powerful is not just detection, but insight.  
The system also generates analytics, predicts tint-level trends, and highlights non-compliant patterns using statistical models.  
Built to mimic a **real-world Intelligent Transport Monitoring System**, it combines real-time detection, compliance analysis, and future forecasting — all in one setup.  



✨ Key Features  
- 🎥 Real-Time Tint Detection — Uses OpenCV to capture and analyze live video frames.  
- ⚠️ Instant Compliance Alerts — Triggers warnings when tint levels exceed legal limits.  
- 📊 Smart Data Logging — Every detection is stored in logs and CSVs for further study.  
- 📈 Analytics & Visualization — Generates plots, averages, and compliance summaries.  
- 🔮 Predictive Modeling — Employs linear regression to forecast future tint levels.  
- 🧠 Outlier & Anomaly Detection — Spots unusual or extreme tint patterns automatically.  
- 🖥️ IoT Simulation Mode — Mimics a live dashboard that monitors multiple vehicle feeds.  

Each feature is modular — so you can plug, test, and extend easily.  

🛠️Tech Stack  

Language - Python 3.10+ 
Computer Vision - OpenCV 
Data Handling - Pandas, NumPy 
Visualization -  Matplotlib 
Machine Learning - Scikit-Learn 
Alerts & Audio - playsound 
Detection Model - Haar Cascade Classifier


📁 Project Structure  
da.py - Core tint detection and video feed
├── vi.py - Video analysis + fine alerts + CSV export
├── sim.py - IoT simulation and dashboard
├── basel.py - Log analysis and stats summary
├── baselv.py - Visual distribution of tint data
├── dan.py - Time-series analytics
├── histo.py - Histogram generator
├── pra.py - Linear regression model
├── fpy.py - Future prediction engine
├── irrv.py - Outlier detection
├── rcav.py - Anomaly visualization
├── test_cascade.py - Haar cascade test module
├── haarcascade_car.xml - Vehicle detection model
├── tint_levels_dataset.csv - Tint dataset (auto-generated)
└── tint_detection.log - Detection log file

⚙️ Installation & Usage  
1. Clone the Repository  
bash
git clone https://github.com/yourusername/Smart-Vehicle-Tint-Detection.git
cd Smart-Vehicle-Tint-Detection

2.Install Dependencies 
pip install opencv-python pandas numpy matplotlib scikit-learn playsound

3.Run tint detection 
python vi.py

4.View Reports and Analytics
python basel.py
python histo.py
python dan.py

5.Simulate IOT Dashboard 
python sim.py
##sample python file to make simulations currently 


📊 Sample Output
[INFO] Vehicle detected...
[ALERT] Tint Level: 72% → Exceeds Legal Limit!
[LOG] Data recorded to tint_levels_dataset.csv
[RESULT] Average Tint Level: 41.27%
[REPORT] Non-Compliant Entries: 12
