import base64
import os

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")

def get_asset_base64(filename: str) -> str:
    """Read an image asset file and return a base64 data URI string."""
    filepath = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode("utf-8")
    ext = os.path.splitext(filename)[1].lstrip(".").lower()
    mime = "image/png" if ext in ["png", ""] else f"image/{ext}"
    return f"data:{mime};base64,{b64_str}"

def get_asset_path(filename: str) -> str:
    """Return absolute path of an asset file."""
    return os.path.join(ASSETS_DIR, filename)
