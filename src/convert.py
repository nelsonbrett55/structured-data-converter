from lxml import etree
import json

def apply_xslt(xml_path, xsl_path):
    dom = etree.parse(xml_path)
    xslt = etree.parse(xsl_path)
    transform = etree.XSLT(xslt)
    result = transform(dom)
    with open("src/output/output.html", "wb") as f:
        f.write(etree.tostring(result, pretty_print=True))
    print("✅ XSLT transformation complete.")

def json_to_xml(json_path):
    with open(json_path) as f:
        data = json.load(f)
    root = etree.Element("root")
    for key, value in data.items():
        child = etree.SubElement(root, key)
        child.text = str(value)
    tree = etree.ElementTree(root)
    tree.write("src/output/from_json.xml", pretty_print=True)
    print("✅ JSON to XML complete.")
