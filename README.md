README:
Project Components: 
1- Hardware:
•	Arduino Board
•	Soil Moisture Sensor 
•	TDS Sensor 
•	Water Pump 
•	Jumper Wires
2- Software & Libraries

Python Libraries
Install the following libraries before running the project:
•	flask
•	flask-cors 
•	pyserial 
•	pandas
•	scikit-learn
•	joblib

Project Files Explanation
•	server.py  Main backend server using Flask
•	ai_engine.py  AI analysis and decision-making logic
•	train_model.py  Trains the AI model
•	soil_ai_model.pkl  Saved trained AI model
•	soil_data.csv  Dataset used for training
•	arduino_code.ino  Arduino code for sensor reading and pump control
•	dashboard.html  Web dashboard interface







How to Run the Project
Step 1: Extract the zip file and save it on your computer 
Step 2: Install Required Libraries 
Open terminal and write:
py -m pip install flask flask-cors pyserial pandas scikit-learn joblib
Step 3: Upload the Arduino code 
1.	Open Arduino IDE 
2.	Open file: arduino_code.ino 
3.	Connect Arduino to the computer
4.	Select the correct board and port 
5.	Upload the code to the Arduino 
Note: If no Arduino is connected, the system will automatically switch to Simulation Mode. In this mode, the dashboard will generate simulated sensor readings so the AI system and website can still be tested and demonstrated without physical hardware.
Step 4: Run the AI Server 
Open terminal inside the project folder and run server.py 

Step 5: Open Dashboard
Open browser and go to: http://127.0.0.1:5000
The dashboard will display:
•	Live sensor readings 
•	Soil health score 
•	Alerts 
•	Pump status 
•	AI recommendations


