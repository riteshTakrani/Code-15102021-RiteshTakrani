from flask import Flask, request, jsonify
import json
import bmi_calculator

app = Flask(__name__)


@app.route('/post/', methods=['POST'])
def update_record():
    records = json.loads(request.data)
    calc_bmi = bmi_calculator.BMI(records)
    response_final = calc_bmi.calculate_bmi_main()

    return jsonify(response_final)


if __name__ == '__main__':
    app.run(debug=True)
