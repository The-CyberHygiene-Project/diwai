import http.server
import os
import plistlib
import socket
import subprocess
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "packaging" / "DIWAI Library.app"


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def test_bundle_runs_the_launch_script():
    info = plistlib.loads((APP / "Contents" / "Info.plist").read_bytes())
    assert info["CFBundleExecutable"] == "launch"
    assert info["CFBundleName"] == "DIWAI Library"
    launch = APP / "Contents" / "MacOS" / "launch"
    assert os.access(launch, os.X_OK)


def test_launcher_binds_loopback_only():
    text = (APP / "Contents" / "MacOS" / "launch").read_text()
    assert "--host 127.0.0.1" in text and "0.0.0.0" not in text


def test_running_server_is_reused_not_restarted(tmp_path):
    port = free_port()

    class Health(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"ok":true}')

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", port), Health)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        env = {**os.environ, "DIWAI_LIBRARY_PORT": str(port), "DIWAI_LIBRARY_OPEN": "echo",
               "DIWAI_LIBRARY_LOG": str(tmp_path / "log.txt")}
        out = subprocess.run([str(APP / "Contents" / "MacOS" / "launch")], env=env,
                             capture_output=True, text=True, timeout=30)
        assert out.returncode == 0
        assert f"http://127.0.0.1:{port}/" in out.stdout
        assert "reusing" in (tmp_path / "log.txt").read_text()
    finally:
        srv.shutdown()


def test_bundle_has_its_icon():
    info = plistlib.loads((APP / "Contents" / "Info.plist").read_bytes())
    assert info["CFBundleIconFile"] == "AppIcon"
    icns = APP / "Contents" / "Resources" / "AppIcon.icns"
    assert icns.read_bytes()[:4] == b"icns"
