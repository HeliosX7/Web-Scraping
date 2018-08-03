
from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve

# using this image scraper from the location that 
# we want to save scraped images to


def get_images(url):
    
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")

    #images is a list of bs4 element tags

    images = [img for img in soup.findAll('img')]

    total_images=str(len(images))
    
    print( total_images + " images found.")
    print('Downloading images to current working directory.')

    i=1
    
    for each in images:
        image_links = each.get('src')
        filename=image_links.split('/')[-1]
        urlretrieve(image_links,filename)   #copying the images
        print(i,"out of " + total_images +" downloaded")
        i=i+1


link=input("Enter the url:")

get_images(link)


