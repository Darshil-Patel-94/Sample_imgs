import json

# Your Vercel deployed base URL
base_url = "https://sample-imgs.vercel.app/"

# Load the scene file
with open("converted.scene.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Go through each child and update `uri` or `style.font`
for child in data.get("scene", {}).get("children", []):
    if "uri" in child:
        child["uri"] = base_url + child["uri"]
    if child.get("style", {}).get("font"):
        font_path = child["style"]["font"]
        if not font_path.startswith("http"):
            child["style"]["font"] = base_url + font_path

# Save to a new file
with open("updated.scene.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ Updated scene saved to updated.scene.json")
