import hashlib,json
from pathlib import Path
def seal(root):
 root=Path(root);m={"contract_version":"1.0.0","files":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob("*") if p.is_file() and p.name!="manifest.json"}}; (root/"manifest.json").write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__":
 import sys;seal(sys.argv[1])
