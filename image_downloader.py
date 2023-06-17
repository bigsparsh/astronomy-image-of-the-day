import requests

for i in range(1, 101):
    url = f'https://picsum.photos/1920/1080?random={i}'
    image = requests.get(url).content
    with open(f'Images/Image-{i}.png', 'wb') as img:
        img.write(image)
