import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def transform_text(input_text: str) -> str:
    input_text_copy=input_text
    input_text_copy = re.sub(r"\b\d{5}[- ]?\d{5}\b", "[REDACTED]", input_text_copy)
    input_text_copy= re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", input_text_copy)
    input_text_copy = input_text_copy.replace("Python", "🐍")
    return input_text_copy

str="Call me at 98123-45678 on 2025-08-23.I love Python more than Java."
print("Output: ",transform_text(str))
