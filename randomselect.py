import tarfile
import json
import random

OUTPUT_FILE = "qald_9_plus_test_wikidata_sample.json"  # Output file for selected samples



def sample_json_from_tar_gz( output_file, sample_size=15):
        json_file_name = "qald_9_plus_test_wikidata.json"
        if not json_file_name:
            print("No JSON file found inside the archive.")
            return
        with open(json_file_name, "r", encoding="utf8") as f:
            try:
                # Try loading as a large JSON array
                data = json.load(f)
                sampled_records = random.sample(data, min(sample_size, len(data)))
                for s in sampled_records:
                    s["question"] = s["question"][0]["string"]
                    s["answers"] = s["answers"][0]["results"]["bindings"]
            except json.JSONDecodeError:
                # If it's JSONL, stream line-by-line
                f.seek(0)
                sampled_records = []
                for i, line in enumerate(f):
                    record = json.loads(line)
                    record.pop("ruleIds")
                    if i < sample_size:
                        sampled_records.append(record)
                    else:
                        j = random.randint(0, i)
                        if j < sample_size:
                            sampled_records[j] = record

        # Save the sampled records to a separate JSON file
        with open(output_file, "w", encoding="utf-8") as out_file:
            json.dump(sampled_records, out_file, indent=2)

        print(f"Saved {len(sampled_records)} samples to {output_file}")

if __name__ == "__main__":
    sample_json_from_tar_gz( OUTPUT_FILE)
