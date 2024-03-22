import qrcode
def generar_codigo_qr(contenido,nombre_archivo):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(contenido)
    qr.make(fit=True)

    imagen_qr=qr.make_image(fill_color="black",back_color="white")
    imagen_qr.save(nombre_archivo)

contenido="https://pypi.org/project/qrcode/"
nombre_archivo="codigo_qr_python.png"
generar_codigo_qr(contenido,nombre_archivo)
print(f"Contenido Qr Generado y guardado como {nombre_archivo}")



