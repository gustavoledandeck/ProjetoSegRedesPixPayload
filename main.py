from pixqrcodegen import Payload
from PIL import Image

payload = Payload('Joao Silva', '12345678900', '100.00', 'Sao Paulo', 'LOJA01')
#

img = Image.open("pixqrcodegen.png")


if __name__ == '__main__':
    payload.gerarPayload()
    img.show()




