#GeneQR is a Qr Code Generator Script make in Python by SrAdryX (Adrian Duran Guillen)
#_____________________________________________________________________________________
#Importar modulos
#Import modules
import qrcode
from PIL import Image
#Crear variable para los datos que contendra el qr
#Create variable for the data that will contain the qr
content = "put any text or website here"
#Crear variable qr para modificar el tamaño
#Create variable qr to modify the size
qr = qrcode.QRCode(version=1, box_size=10, border=5)
#Añadir los datos al codigo qr
#Add the data to the qr code
qr.add_data(content)
qr.make(fit=True)
#Cambiar color al qr
#Change color to qr
img = qr.make_image(fill_color = "Blue", back_color="White")
#Guardar el qr en la ruta especificada (Tienes que cambiarla a la que quieras o usar)
#Save the qr in the specified path (You have to change it to the one you want or use)
img.save("C://users//username/downloads/GeneQR/img/geneqr.png")