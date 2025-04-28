import os
import base64
from fastapi import HTTPException
from openai import OpenAI


class JsonHelperAgent:
    def __init__(self):

      def parse_raw_content_to_json(self,raw_content):
        # Step 1: Split the raw content into sections
        lines = raw_content.strip().split("\n")
        structured_data = {}
        current_section = None
        sub_section = None

        for line in lines:
            line = line.strip()
            # Identify sections or sub-sections based on headings
            if line.startswith("###"):
                current_section = line.replace("###", "").strip()
                structured_data[current_section] = {}
                sub_section = None  # Reset sub-section
            elif line.startswith("####"):
                sub_section = line.replace("####", "").strip()
                if current_section:
                    structured_data[current_section][sub_section] = []
            # Process bullet points as list items
            elif line.startswith("- "):
                if current_section and sub_section:
                    structured_data[current_section][sub_section].append(line[2:].strip())
                elif current_section:
                    if "List" not in structured_data[current_section]:
                        structured_data[current_section]["List"] = []
                    structured_data[current_section]["List"].append(line[2:].strip())
            # Process other lines as key-value pairs or text
            else:
                if current_section and sub_section:
                    structured_data[current_section][sub_section].append(line)
                elif current_section:
                    if "Details" not in structured_data[current_section]:
                        structured_data[current_section]["Details"] = ""
                    structured_data[current_section]["Details"] += " " + line.strip()

        # Clean up whitespace and finalize the structure
        for section, content in structured_data.items():
            for key, value in content.items():
                if isinstance(value, str):
                    structured_data[section][key] = value.strip()
                elif isinstance(value, list):
                    structured_data[section][key] = [item.strip() for item in value]

        return structured_data