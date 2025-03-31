#!/usr/bin/env python3
import json
import os
from typing import Dict, List

class LocalizationValidator:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.glossary = self.load_glossary(os.path.join(base_dir, "data/glossary.json"))

    @staticmethod
    def load_glossary(path: str) -> Dict:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def validate(self, source: Dict, target: Dict) -> Dict:
        results = {}
        for key, src_text in source.items():
            tgt_text = target.get(key, "")
            results[key] = {
                'missing': not bool(tgt_text),
                'terminology': self.check_terms(src_text, tgt_text),
                'length_diff': f"{abs(len(src_text) - len(tgt_text)) / len(src_text):.0%}"
            }
        return results

    def check_terms(self, src: str, tgt: str) -> List[str]:
        errors = []
        for term, trans in self.glossary.items():
            if term.lower() in src.lower() and trans not in tgt:
                errors.append(f"'{term}' → '{trans}' 누락")
        return errors

if __name__ == "__main__":
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    validator = LocalizationValidator()
    
    # sample data load
    with open(os.path.join(base_dir, 'data/en-US/payments.json'), 'r') as f:
        en_data = json.load(f)
    with open(os.path.join(base_dir, 'data/ko-KR/payments.json'), 'r') as f:
        ko_data = json.load(f)
    
    # validation 
    results = validator.validate(en_data, ko_data)
    print(json.dumps(results, indent=2, ensure_ascii=False))
