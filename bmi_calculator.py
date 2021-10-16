import bisect
from math import ceil
import threading

MAX_REC_PER_THREAD = 10000

BMI_TABLE = {
    18.4: ["Underweight", "Malnutrition risk"],
    24.9: ["Normal weight", "Low risk"],
    29.9: ["Overweight", "Enhanced risk"],
    34.9: ["Moderately obese", "Medium risk"],
    39.9: ["Severely obese", "High risk"],
    40: ["Very severely obese", "Very high risk"]
}

BMI_INDEX = (18.4, 24.9, 29.9, 34.9, 39.9, 40)


class BMI:
    # this is the class to calculate BMI

    def __init__(self, records):
        self.records = records
        self.response = []
        self.person_id = 1
        self.overwt_count = 0
        self.faulty_records = 0

    def get_item(self, bmi):
        # return the category and risk level in accordance with the BMI supplied
        bmi_key = bisect.bisect_left(BMI_INDEX, bmi)

        # if bmi key is last key from dictionary so do -1 to avoid index out of bound error
        if bmi_key == len(BMI_INDEX):
            bmi_key -= 1
        return {"id": self.person_id, "bmi": bmi, "category": BMI_TABLE[BMI_INDEX[bmi_key]][0],
                "risk": BMI_TABLE[BMI_INDEX[bmi_key]][1]}

    def calculate_bmi(self, records_slice):
        # check records receive in post request
        count = 0
        for element in records_slice:
            count += 1
            try:
                ht = element["HeightCm"]
                wt = element["WeightKg"]
                if ht < 0 or wt < 0:
                    self.faulty_records += 1
                    continue
                bmi = wt / ((ht * ht) / 10000)
                res = self.get_item(bmi)
                self.response.append(res)
                if res["category"] == "Overweight":
                    self.overwt_count += 1
                self.person_id += 1
            except KeyError:
                self.faulty_records += 1

    def calculate_bmi_main(self):
        # create threads based on number of records to process
        # each thread can process 10k records
        record_sent = 0
        record_from = 0
        record_to = 0

        total_records = len(self.records)
        record_remaining = total_records
        total_threads = ceil(total_records / MAX_REC_PER_THREAD)
        threads = []

        # create threads to handle records and calculate BMI for each one
        for _ in range(0, total_threads):
            if record_remaining <= MAX_REC_PER_THREAD:
                record_sent = record_remaining
                record_remaining -= record_sent
            else:
                record_sent = MAX_REC_PER_THREAD
                record_remaining -= MAX_REC_PER_THREAD
            record_from = _ * MAX_REC_PER_THREAD
            record_to = record_from + record_sent
            th = threading.Thread(target=self.calculate_bmi, name=f"Thread {_}", args=
            (self.records[record_from:record_to],))
            threads.append(th)
            th.start()

        # wait for each thread to finish execution
        for th in threads:
            th.join()

        # adding faulty records and over weight count to the final response packet
        self.response.append({"faulty_records": self.faulty_records})
        observations = " people are over weight out of "
        self.response.append(
            {"Overweight count": self.overwt_count,
             "observations": f"{self.overwt_count} people are over weight out of {self.person_id - 1}"})
        return self.response
