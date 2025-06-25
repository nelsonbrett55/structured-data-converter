from pathlib import Path
from lxml import etree
import json

# Use pathlib for clean and readable paths
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def apply_xslt(xml_path, xsl_path, output_path):
    dom = etree.parse(xml_path)
    xslt = etree.parse(xsl_path)
    transform = etree.XSLT(xslt)
    result = transform(dom)

    # Proper way to get bytes from an XSLTResultTree
    with open(output_path, "wb") as f:
        f.write(bytes(result))
    print("✅ XSLT transformation complete.")

def json_to_xml(json_path, output_path):
    with open(json_path) as f:
        data = json.load(f)

    def build_xml(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = etree.SubElement(parent, key)
                build_xml(child, value)
        elif isinstance(data, list):
            for item in data:
                item_elem = etree.SubElement(parent, "item")
                build_xml(item_elem, item)
        else:
            parent.text = str(data)

    root = etree.Element("root")
    build_xml(root, data)
    tree = etree.ElementTree(root)
    tree.write(output_path, pretty_print=True)
    print("✅ JSON to XML complete.")

if __name__ == "__main__":
    try:
        input_json = DATA_DIR / "input.json"
        output_xml = OUTPUT_DIR / "output.xml"
        input_xsl = DATA_DIR / "transform.xsl"
        output_html = OUTPUT_DIR / "output.html"

        json_to_xml(input_json, output_xml)
        apply_xslt(output_xml, input_xsl, output_html)

    except Exception as e:
        print(f"❌ Error: {e}")
