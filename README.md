# WikiSourceScrapper
WikiSourceScrapper is a dynamic python web application which takes a  wikipedia URL as input and downloads the html source code of the wikipedia page. Then it scrapes out the table of contents and paste it in a new page. The starter scaffold which comes bundle with pyramid was used. The requirements specifications as well as the developed bonus features are described in the pdf file included in this project directory.This pdf file contains screen shorts of sample input and output.

#Project stucture

.
├── wikiapp
│   ├── CHANGES.txt
│   ├── development.ini
│   ├── MANIFEST.in
│   ├── production.ini
│   ├── README.txt
│   ├── setup.py
│   ├── wikiapp
│   │   ├── __init__.py
│   │   ├── static
│   │   │   ├── pyramid-16x16.png
│   │   │   ├── pyramid.png
│   │   │   ├── theme.css
│   │   │   └── theme.min.css
│   │   ├── templates
│   │   │   ├── result.pt
│   │   │   ├── result.pt~
│   │   │   ├── welcome.pt
│   │   │   └── welcome.pt~
│   │   ├── tests.py
│   │   ├── views.py
│   └── wikiapp.egg-info
│       ├── dependency_links.txt
│       ├── entry_points.txt
│       ├── not-zip-safe
│       ├── PKG-INFO
│       ├── requires.txt
│       ├── SOURCES.txt
│       └── top_level.txt
└── wikiapp_1-1.zip


# Some dependencies of the project

1. BeautifulSoup 4
2. lxml
3. urllib2
4. pyramid
5. HTMLParser
6. re
7. nose

# How to run the project

1. Make sure you have an active internet connection before running this web application else you will get an error from the urllib2 package.
2. Uncompress the zip archive containing the application.
3. Using a terminal, Change directory to the root folder of the application. Make sure the directory you are found in contains the following files 

CHANGES.txt
development.ini
MANIFEST.in
production.ini
README.txt
setup.py

4. Start the application server. To do so, If you are using a virtual environment to run the application, simply type $VENV/bin/pserve production.ini --reload otherwise pserve production.ini
5. Once the server is started you get the following message in the terminal.

Starting subprocess with file monitor
Starting server in PID 11784.
serving on http://0.0.0.0:6543

6. This confirms that the application has been deployed and can be accessed from a web browser through the url http://0.0.0.0:6543 or http://localhost:6543.

7. Open your web browser and insert the url http://0.0.0.0:6543.


# Running the unit tests

1. Change directory to the root folder of the application. Folder containing development.ini and production.ini
2. Run the command $VENV/bin/nosetests wikiapp 

Please see attached PDF for further explanations and source codes for comments.


