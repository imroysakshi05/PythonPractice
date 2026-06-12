import csv
import json

filtered_data = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["age"]) >= 18:
            filtered_data.append({
                "name": row["name"],
                "age": int(row["age"]),
                "salary": int(row["salary"])
            })

with open("output.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

print("JSON file created successfully!")
