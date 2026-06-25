import serial
import threading
import time
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from ai_engine import run_detailed_analysis

app = Flask(__name__)
CORS(app)

latest_data = {}

# ====== Arduino Connection ======
try:
    ser = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)  
    # if the arduino connected succeed we will take sensors value 
    simulation_mode = False
    print("✅ Connected to Arduino on COM5")
    #if the arduino i snt found it will simulate contant values to continue the program
except Exception as e:
    ser = None
    simulation_mode = True
    print("❌ Arduino not found → Simulation Mode")

# ====== DATA LOOP ======
def data_fetcher():
    global latest_data

    while True:
        try:
            # Default fallback (only if no Arduino)
            moisture, tds = 40, 300

            if ser:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print("RAW:", line)

                if "," in line:
                    moisture, tds = map(float, line.split(","))

            # AI Processing
            latest_data = run_detailed_analysis(moisture, tds)

        except Exception as e:
            print("ERROR:", e)

        time.sleep(2)

# ====== ROUTES ======
@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    return jsonify(latest_data)

# ====== START ======
if __name__ == "__main__":
    t = threading.Thread(target=data_fetcher, daemon=True)
    t.start()
    app.run(debug=False)