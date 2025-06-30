import os
import json

# Paths and URLs
base_url = "https://sample-imgs.vercel.app/"
input_json = "updated.scene.json"
output_json = "final.scene.json"

# Load the scene JSON
with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix font URLs inside <font path="..."> tag and style.font
for child in data.get("scene", {}).get("children", []):
    if child["type"] == "text":
        if "text" in child:
            child["text"] = child["text"].replace(
                'path="text/', f'path="{base_url}text/'
            )
        if "style" in child and "font" in child["style"]:
            font_path = child["style"]["font"]
            if not font_path.startswith("http"):
                child["style"]["font"] = base_url + font_path

# Save updated JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"✅ Final scene saved to: {output_json}")
