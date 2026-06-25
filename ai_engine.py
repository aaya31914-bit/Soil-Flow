import joblib

# download the (mind) from the training
model = joblib.load('soil_ai_model.pkl')

def estimate_temperature(moisture, tds):
    """function to estimate the temprature because there is no sensor(appear more realistic)"""
    temp = 30
    if moisture < 30:
        temp += 6
    elif moisture > 70:
        temp -= 3
    if tds > 800:
        temp += 2
    return round(temp, 1)

def run_detailed_analysis(moisture, tds):
    try:
        # 1. take temprature
        temp = estimate_temperature(moisture, tds)

        # 2. predict the soil status from ai 
        prediction = model.predict([[temp, tds, moisture]])[0]

        # 3. determine the status and health score based on ai predection
        if prediction == 0:
            status = "Healthy"
            score = 90
        elif prediction == 1:
            status = "Warning"
            score = 60
        else:
            status = "Critical"
            score = 30

        # 4. alerts based on ai predection
        alerts = []
        if moisture < 30:
            alerts.append("⚠️ Low Soil Moisture")
        if tds > 1000:
            alerts.append(" 🚫 High pollution")
        if temp > 38:
            alerts.append("🔥 Heat Stress")
        
        if not alerts:
            alerts.append("✅ Normal Conditions")

        # 5. Pump operating area -actions- contain water or Pollution treatment materials
        actions = []
        pump_status = "OFF"
        if moisture < 35 or tds > 800:
            actions.append("💧 Irrigation/treatment Activated")
            pump_status = "ON"
        else:
            actions.append(" No Action Needed in the current time")

        # 6. suggest solutions 
        solutions = []
        if moisture < 40:
            solutions.append("check the irrigation system and increase water supply.")
        if tds > 800:
            solutions.append("TDS levels exceed safety limits. Check fertilizer dosage.")
        if not solutions:
            solutions.append("Soil parameters are within the ideal range.")

        # return results to the dashboard
        return {
            "sensors": {
                "moisture": moisture,
                "tds": tds,
                "temperature": temp
            },
            "soil": {
                "status": status,
                "score": score
            },
            "analysis": {
                "alerts": alerts,
                "actions": actions,
                "solutions": solutions,
                "pump": pump_status
            }
        }

    except Exception as e:
        return {"error": str(e)}