import requests

thelist = ["apple_juice.jpg","apple_pressings.jpg","dumplings.jpg","lemon_juice.jpg","bad_fruit.jpg"]
for x in thelist:
    website = requests.get("https://juice-shop.herokuapp.com/assets/public/images/products/" + x)

    if(website.status_code == 200):
        with open(x, 'wb') as pic:
            pic.write(website.content) 