import qrcode
from PIL import Image

# -------------------------
# TEXTO OU LINK PARA O QR
# -------------------------
data = "https://www.google.com"  # pode ser qualquer texto ou link

# -------------------------
# CONFIGURAÇÃO DO QR CODE
# -------------------------
qr = qrcode.QRCode(
    version=None,  # tamanho automático
    error_correction=qrcode.constants.ERROR_CORRECT_Q,  # alta correção
    box_size=20,  # tamanho dos quadradinhos
    border=4,     # borda do QR
)

qr.add_data(data)
qr.make(fit=True)

# -------------------------
# GERA A IMAGEM
# -------------------------
img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# -------------------------
# TORNA O FUNDO TRANSPARENTE
# -------------------------
pixels = img.getdata()
new_pixels = []

for p in pixels:
    if p[0] == 255 and p[1] == 255 and p[2] == 255:
        # branco vira transparente
        new_pixels.append((255, 255, 255, 0))
    else:
        # preto permanece
        new_pixels.append(p)

img.putdata(new_pixels)

# -------------------------
# SALVA O QR CODE
# -------------------------
img.save("qr_transparente.png")
print("QR Code gerado com sucesso!")
