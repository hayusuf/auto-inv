auto-inv-selenium

STEP 1:
Download the file auto-inv-selenium:
    - Press on the file above named auto-inv-selenium,
    - Click Raw 
    - Right click and save page as auto-inv-selenium into prefered folder.


STEP 2:
Download the logo.jpg:
    - Press on logo.jpg
    - Press download and put in same folder as auto-inv-selenium
--- if you wish to use a different logo, put a logo.jpg(has to be called this) image into the same folder as auto-inv-selenium

STEP 3:
Inside command prompt paste the following command:
pip install openpyxl pillow beautifulsoup4 urllib3 selenium requests_html

STEP 4:
Download required chromedriver.exe
    - Visit https://chromedriver.chromium.org/
    - Press download latest stable release
    - Download chromedriver_win32.zip
    - extract chromedriver.exe file and put into same folder as auto-inv-selenium and logo.jpg.

Now you can use the auto-inv-selenium program in the command prompt to 

download the product image(+paste logo onto corner of it), 

scrape the product information,

and put it into an excel sheet called test.xlsx(which cannot be open in excel for the program to work).

The program takes a little while because it runs a headless browser with selenium so be patient. Please send me any question thats you have.

The command to run the program is:

python auto-inv-selenium.py

It may be easier to use the program to put data in the test.xlsx and download image, and then move the data from test.xlsx to a different excel sheet with other product inventory listings, and move the picture to the desired location.


