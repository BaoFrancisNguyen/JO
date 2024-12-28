import qrcode
from io import BytesIO
from django.core.files import File

def generate_qr_code(data):
    """
    Génère un QR code à partir des données fournies
    """
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return File(buffer, name="qr_code.png")
