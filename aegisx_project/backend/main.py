from fastapi import FastAPI
from backend.scanners.nmap_scanner import NmapScanner

app = FastAPI(title="AegisX")

scanner = NmapScanner()

@app.get("/")
def home():
    return {"message": "AegisX Running"}

@app.post("/scan")
def scan_target(target: str):
    result = scanner.scan(target)
    return result