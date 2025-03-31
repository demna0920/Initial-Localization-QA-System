import csv
import json
import os

def csv_to_json(csv_path, json_path):
    glossary = {}
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            glossary[row['term_en']] = row['term_ko']
    
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(glossary, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_to_json(
        csv_path=os.path.join(base_dir, "config/glossary.csv"),
        json_path=os.path.join(base_dir, "data/glossary.json")
    )
