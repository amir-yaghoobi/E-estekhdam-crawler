# E-estekhdam-crawler
Python crawler for http://www.E-estekhdam.com/ that looks for specific keywords.

## How to install
1. clone project into your pc with: `git clone https://github.com/ayagh/E-estekhdam-crawler.git`  
2. cd into project folder: `cd ./E-estekhdam-crawler` 
3. install require packages: `pip install -r pip-freeze.txt`

## How to use
Open **"config.py"** file and edit it with your needs.
after that run it with `python ./run.py`.  
results will be saved into **"result.json"** file.

#### Sample config.py:
```
SITE_URL = 'http://www.e-estekhdam.com/search/استخدام-برنامه-نویس-در-تهران/'

PAGE_LIMIT = 10

KEYWORDS = ['کارآموز',]
```

#### Note:
* **SITE_URL** Must be url from this path http://www.e-estekhdam.com/search/ .
* **PAGE_LIMIT** Must be an integer and greater than zero.
* **KEYWORDS** Must be list of strings *(keywords)* and have at least one item.
