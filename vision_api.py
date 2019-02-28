import requests
import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from base64 import b64encode

class ApiClient:
    def __init__(self, type):
        self.type = type

    def call(self, image_path):
        ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

        api_key_file = open("api_key", "r")
        api_key = api_key_file.read()

        print("Request Vision API using following picture")
        im = Image.open(image_path)
        plt.imshow(np.asarray(im))
        plt.show()

        image = open(image_path, 'rb')
        ctxt = b64encode(image.read()).decode()

        image_requests = {}
        image_requests['image'] = {'content': ctxt}
        image_requests['features'] = [{ 'type': self.type, 'maxResults': 5 }]

        response = requests.post(
            ENDPOINT_URL,
            data=json.dumps({"requests": image_requests}).encode(),
            params={'key': api_key},
            headers={'Content-Type': 'application/json'}
        )
        return response
