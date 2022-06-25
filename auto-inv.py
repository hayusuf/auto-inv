from bs4 import BeautifulSoup
import urllib
from os.path import exists

def make_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, features="html5lib")

def get_images(url, pallet):
    soup = make_soup(url)

    tag = soup.find(id="thd-helmet__link--preloadImg")
    if tag is None:
        print('No matching item and image found')
        return
    link = tag.get('href')
    if exists("/home/yusuf/src/auto-inv/second_{}".format( link.split('/')[-1] )):
       urllib.request.urlretrieve(link, "/home/yusuf/src/auto-inv/third_{}".format( link.split('/')[-1] ))    
    elif exists("/home/yusuf/src/auto-inv/{}".format( link.split('/')[-1] )):
       urllib.request.urlretrieve(link, "/home/yusuf/src/auto-inv/second_{}".format( link.split('/')[-1] ))    
    else:
        urllib.request.urlretrieve(link, "/home/yusuf/src/auto-inv/{}".format( link.split('/')[-1] ))
    return

def main():
    inp = input("Enter a UPC code or anything that should work in HomeDepot.com search bar\n")
    pallet = input("What pallet number is this item from(what folder should it be added to)?\n")
    get_images("https://www.homedepot.com/s/{}?".format( inp ), pallet);

if __name__ == "__main__":
    main()
