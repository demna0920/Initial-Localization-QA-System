#!/bin/bash

echo "🔧 1. 용어집 생성 중..."
python3 scripts/generate_glossary.py

echo "🔍 2. 번역 검증 시작..."
python3 scripts/evaluate.py

echo "✅ 모든 작업 완료!"
