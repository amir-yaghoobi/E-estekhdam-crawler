# E-estekhdam-crawler
> Python crawler for [E-estekhdam](http://www.E-estekhdam.com/) that looks for specific keywords.

## How to install
1. clone project into your pc with: `git clone https://github.com/ayagh/E-estekhdam-crawler.git`  
2. cd into project folder: `cd ./E-estekhdam-crawler` 
3. install require packages: `pip install -r pip-freeze.txt`

## How to use
Open **"config.py"** file and edit it with your needs.
after that run it with `python ./run.py`.  
results will be saved into **"result.json"** file.

#### Sample config.py:
```python
SITE_URL = 'http://www.e-estekhdam.com/search/استخدام-برنامه-نویس-در-تهران/'

KEYWORDS = ['کارآموز',]

BOT_TOKEN = '<YOUR-TELEGRAM-BOT-TOKEN>'

# Your channel id for bot to send results into it
CHANNEL_ID = int

```

#### Note:
* **SITE_URL** Must be url from this path http://www.e-estekhdam.com/search/ .
* **CHANNEL_ID** Must be an integer.
* **KEYWORDS** Must be list of strings *(keywords)* and have at least one item.
