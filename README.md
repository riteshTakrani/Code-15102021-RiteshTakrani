# Code-15102021-RiteshTakrani


**Intorduction**
This is the program to calculate BMI. API endpoint is exposed to pass on the required parameters like gender, height and weight in JSON format. Response contains calculated BMI along with category (underweight, normal, obese, etc.) along with count of total over wieght people from the supplied records and faulty records as well.

**Pre-requisite**
1)Python installed preferrable python version 3.6+
2)Download zip file/clone the repository into your local machine.
3)Open command propt/terminal and goto Code-15102021-RiteshTakrani\venv\Scripts and execute activate.
(X:\Code-15102021-RiteshTakrani\venv\Scripts>activate)
4)Goto main folder Code-15102021-RiteshTakrani\ and run Python main.py to start the server
5)API verification tool like Postman or Insomnia to send request and receive response

**How to use**
1)Make a post request on http://127.0.0.1:5000/post/ 
2)Pass JSON formatted data, as shown below :
    [
      {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
      {"Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
      {"Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
      {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
      {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
      {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ]
3)Response received on your API verification tool will look like:
     [
      {
        "bmi": 32.83061454806607,
        "category": "Moderately obese",
        "id": 1,
        "risk": "Medium risk"
      },
      {
        "bmi": 32.79194475521778,
        "category": "Moderately obese",
        "id": 2,
        "risk": "Medium risk"
      },
      {
        "bmi": 23.76543209876543,
        "category": "Normal weight",
        "id": 3,
        "risk": "Low risk"
      },
      {
        "bmi": 22.49963710262738,
        "category": "Normal weight",
        "id": 4,
        "risk": "Low risk"
      },
      {
        "bmi": 31.11111111111111,
        "category": "Moderately obese",
        "id": 5,
        "risk": "Medium risk"
      },
      {
        "bmi": 29.402273297715947,
        "category": "Overweight",
        "id": 6,
        "risk": "Enhanced risk"
      },
      {
        "faulty_records": 0
      },
      {
        "Overweight count": 1,
        "observations": "1 people are over weight out of 6"
      }
    ]
