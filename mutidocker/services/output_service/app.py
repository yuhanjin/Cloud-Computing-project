from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_results():
    data = request.get_json()
    df = pd.DataFrame(data)
    df.to_csv('output/result.csv', index=False)
    return jsonify({"message": "Results saved successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003) 