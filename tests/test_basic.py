import os
import tempfile
from mobilegraph.graphify import build_code_graph
from mobilegraph.security import run_security_audit


def test_graphify_execution():
    with tempfile.TemporaryDirectory() as temp_dir:
        sample_file = os.path.join(temp_dir, "sample.dart")
        with open(sample_file, "w") as f:
            f.write("class ModernHomeScreen extends StatelessWidget { }\n")

        res = build_code_graph(temp_dir)
        assert res["nodes_count"] == 1
        assert res["nodes"][0]["classes"] == ["ModernHomeScreen"]


def test_security_audit_execution():
    with tempfile.TemporaryDirectory() as temp_dir:
        sample_manifest = os.path.join(temp_dir, "AndroidManifest.xml")
        with open(sample_manifest, "w") as f:
            f.write('<activity android:name=".MainActivity" android:exported="true" />')

        findings = run_security_audit(temp_dir)
        assert len(findings) == 1
        assert findings[0]["id"] == "SEC-002"
