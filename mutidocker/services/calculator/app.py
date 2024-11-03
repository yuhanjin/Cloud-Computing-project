from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    df = pd.DataFrame(data)
    
    grade_columns = ['Chinese', 'Math', 'English', 'CloudComputing']
    result = {
        'Name': df['Name'].tolist(),
        'Total': df[grade_columns].sum(axis=1).tolist(),
        'Score_Gap': (df[grade_columns].max(axis=1) - df[grade_columns].min(axis=1)).tolist()
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002) 