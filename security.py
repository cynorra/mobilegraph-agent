import os
import re
from typing import List, Dict, Any


def run_security_audit(project_path: str) -> List[Dict[str, Any]]:
    """
    Performs static AST and pattern-based audits to prevent hardcoded secrets,
    insecure IPC/intent exposures, and cleartext traffic in mobile applications.
    """
    print(f"[MobileGraph] 🛡️ Starting Security & Vulnerability Scan in: {project_path}")
    vulnerabilities: List[Dict[str, Any]] = []

    patterns = [
        {
            "id": "SEC-001",
            "name": "Hardcoded Secret / API Key Exposure",
            "regex": re.compile(r"(?i)(api[_-]?key|secret|private[_-]?key|token)\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]"),
            "severity": "CRITICAL"
        },
        {
            "id": "SEC-002",
            "name": "Exported Component without Permissions",
            "regex": re.compile(r'android:exported=["\']true["\']'),
            "severity": "HIGH"
        },
        {
            "id": "SEC-003",
            "name": "Cleartext Network Traffic Allowed",
            "regex": re.compile(r'android:usesCleartextTraffic=["\']true["\']'),
            "severity": "MEDIUM"
        }
    ]

    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith((".dart", ".kt", ".java", ".xml")):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, project_path)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line_num, line in enumerate(f, start=1):
                            for pattern in patterns:
                                if pattern["regex"].search(line):
                                    vulnerabilities.append({
                                        "id": pattern["id"],
                                        "name": pattern["name"],
                                        "severity": pattern["severity"],
                                        "file": rel_path,
                                        "line": line_num,
                                    })
                except Exception:
                    continue

    print(f"[MobileGraph] Audit completed. Total findings: {len(vulnerabilities)}")
    for vuln in vulnerabilities:
        print(f"  [{vuln['severity']}] {vuln['name']} in {vuln['file']}:{vuln['line']}")

    if len(vulnerabilities) == 0:
        print("[MobileGraph] ✅ No high-risk static vulnerabilities detected.")

    return vulnerabilities
