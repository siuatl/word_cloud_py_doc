<p align="center">
<img src="https://github.com/siuatl/word_cloud_py_doc/blob/main/python_wordcloud.png" alt="wordcloud" width="400" height="400">
</p>

# Python Documentation Word Cloud
This program allows the user to generate a [*word cloud*](https://en.wikipedia.org/wiki/Tag_cloud) from the [*Python documentation*](https://docs.python.org/3/).

The program works by using a search spider program to index the Python documentation website and store the result into a SQLite database. We read the HTML Text from from each of the URLs, and then make a dictionary that contains the frequency of all the words used. The visualization is generated with the [D3 JavaScript library](https://d3js.org/).

## Search Spider (`pagerank`)
The spider program comes from Dr. Chuck's Python for Everybody course ([pagerank](https://github.com/csev/py4e/tree/master/code3/pagerank)). It is a set of programs that perform search engine functions and store the indexed webpage data into a database. Its function is to crawl a website and extract a series of pages by recording the links between the pages in the database. The program randomly chooses the links that have not yet been visited on the web. 

## How to Execute
1. Generate a `spider.sqlite` using the instructions [here](https://github.com/csev/py4e/tree/master/code3/pagerank). Or use the provided `spider.sqlite` from this repo.
2. Run:
```
./pdwc.py -f spider.sqlite
```   
3. Open `gword.html` in your web browser. 

## How to Run the Unit Tests
```
./test.py
```
