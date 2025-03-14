import json
import os
from collections import defaultdict

# Input and output folder
input_file = "WebQSP-test-eval.json"
output_folder = "WebQSP-test-eval"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Dictionary to store grouped objects by score
grouped_data = defaultdict(list)

# Read and group by score
with open(input_file, "r") as file:
    for line in file:
        obj = json.loads(line.strip())  # Parse JSON line
        res = obj.get("response")
        if "Score: 0" in res:
            grouped_data[0].append(obj)
        elif "Score: 1" in res:
            grouped_data[1].append(obj)  
        elif "Score: 2" in res:
            grouped_data[2].append(obj) 
        elif "Score: 3" in res:
            grouped_data[3].append(obj)  
        elif "Score: 4" in res:
            grouped_data[4].append(obj)  
        elif "Score: 5" in res:
            grouped_data[5].append(obj)  

# Write each group to a separate file
for score, objects in grouped_data.items():
    output_path = os.path.join(output_folder, f"score_{score}.json")
    with open(output_path, "w") as file:
        json.dump(objects, file, indent=4)  # Pretty-print JSON

print(f"JSON files saved in '{output_folder}'")
