import json, xml.etree.ElementTree as ET
from pathlib import Path

def generate_oembed_files(page_data: dict) -> None:
    
    oembed_data = {
        "version": "1.0",
        "type": "rich",
        "provider_name": "Framebuffer",
        "provider_url": "https://framebuffer.cl",
        "title": page_data["title"],
        "author_name": page_data.get("author", ""),
        "html": f"<iframe src='{page_data['embed_url']}'></iframe>",
        "width": 600,
        "height": 400
    }
    
    with open(f"{page_data['path']}/oembed.json", 'w') as f:
        json.dump(oembed_data, f)
    
<<<<<<< HEAD
=======
    # Generate XML
>>>>>>> refs/remotes/origin/main
    root = ET.Element("oembed")
    for key, value in oembed_data.items():
        if key == "html":
            elem = ET.SubElement(root, key)
            elem.text = ET.CDATA(str(value)) # type: ignore
        else:
            ET.SubElement(root, key).text = str(value)
    
    ET.ElementTree(root).write(f"{page_data['path']}/oembed.xml")