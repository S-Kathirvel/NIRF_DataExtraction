import requests

# K88374091488957
# K89119071788957
# K86636457988957
def ocr_space_file(filename, overlay=False, api_key='K86636457988957', language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()



def extract(image):
    return ocr_space_file(filename=image, language='pol')
