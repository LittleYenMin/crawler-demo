Crawler demo
=========

In this project, I will show you how to implement a crawler in two different way (by framework and by package)

Before you start
-----------
pre-requirement
```
python 3.5+
```
clone this project
```shell
git clone https://github.com/LittleYenMin/Crawler-demo.git
```
Install dependency.
```
pip3 install -r requirements.txt
```

Scrapy (by the framework)
--------------------------
check the code [here](./scrapy-demo.py)

run (by scrapy)
```shell
scrapy runspider scrapy-demo.py -o scrapy.json
```

Common way (by requests and lxml)
--------------------------
check the code [here](./common-demo.py)

run
```shell
python common-demo.py
```
