[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Estee WebCrawler on Momoshop</h2>

  <p align="center">
    Crawler products info on Momoshop through restful-API.  
    Analyze product price fluctuations for a week.  
    <br />
    <a href="https://github.com/angelxd84130/Estee_WebCrawler/issues">Report Bug</a>
    ·
    <a href="https://github.com/angelxd84130/Estee_WebCrawler/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#schedule-crawlers">Schedule Crawlers</a></li>
        <li><a href="#web-connection">Web Connection</a></li>
        <li><a href="#data-extraction">Data Extraction</a></li>
        <li><a href="#data-analysis">Data Analysis</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Track daily and weekly price fluctuations of products.
The crawler is automatically driven three times a day, and the crawled target values are stored in a JSON file which is in noSQL mode.

Here's why:
* Find the lowest price of each product.
* Search for the maximum discount on products.
* Rank the saving prices to help visualized analysis.

### Schedule Crawlers  
Set up a schedule to automatically wake up the crawler.  
Evoked three times a day, respectively at 12:00, 15:00, and 18:00.    

### Web Connection
Open the webpage to be crawled in inspect mode. After confirming the product information API, create a request with the urllib package.  

### Data Extraction  
After obtaining all product codes from the catalog page, connect to the single product shopping page one by one, and then obtain the specified data. 

### Data Analysis  
After crawling the data each time, store it in a JSON file, and then extract all product data for analysis.  
Mainly analyze daily product price fluctuations and discount rankings.   


### Built With

* [urllib](https://docs.python.org/3/library/urllib.html)
* [pandas](https://pandas.pydata.org/)
* [JSON](https://docs.python.org/3/library/json.html)
* [schedule](https://schedule.readthedocs.io/en/stable/)



<!-- GETTING STARTED -->
## Getting Started

Start from main.py file. After setting out scheduled times, the process will be called automatically.

### Prerequisites


1. import required python packages.
2. Checkout the product category URL.
   - open the webpage in inspect mode.
   - search the network connections.
   - click any product, and check which API response product information.  
3. Rename the JSON file's name, which is used on storage data.  



<!-- USAGE EXAMPLES -->
## Usage

Check the rank result.  
### Data 
Target shopping mall: Momoshop  
Target brand: Estee  
Target website: [Momoshop_Estee](https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E9%9B%85%E8%A9%A9%E8%98%AD%E9%BB%9B&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType)  
![Momoshop_Estee][product-screenshot0]  

 
### Daily Analysis
Rank the maximum discount of products.    
![Daily_discount_rank][product-screenshot1]   

Check the weekly price fluctuations.  
![Weekly_price_change][product-screenshot2]   
 



<!-- CONTACT -->
## Contact

Yu-Chieh Wang - [LinkedIn](https://www.linkedin.com/in/yu-chieh-wang/)  
email: angelxd84130@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Multi-Class Text Classification with Scikit-Learn](https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f)
* [Text Classification Using Naive Bayes: Theory & A Working Example](https://towardsdatascience.com/text-classification-using-naive-bayes-theory-a-working-example-2ef4b7eb7d5a)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/angelxd84130/Estee_WebCrawler.svg?style=for-the-badge
[contributors-url]: https://github.com/angelxd84130/Estee_WebCrawler/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/angelxd84130/Estee_WebCrawler.svg?style=for-the-badge
[forks-url]: https://github.com/angelxd84130/Estee_WebCrawler/network/members
[stars-shield]: https://img.shields.io/github/stars/angelxd84130/Estee_WebCrawler.svg?style=for-the-badge
[stars-url]: https://github.com/angelxd84130/Estee_WebCrawler/stargazers
[issues-shield]: https://img.shields.io/github/issues/angelxd84130/Estee_WebCrawler.svg?style=for-the-badge
[issues-url]: https://github.com/angelxd84130/Estee_WebCrawler/issues
[license-shield]: https://img.shields.io/github/license/angelxd84130/Estee_WebCrawler.svg?style=for-the-badge
[license-url]: https://github.com/angelxd84130/Estee_WebCrawler/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yu-chieh-wang/
[product-screenshot0]: Estee_WebCrawler.png
[product-screenshot1]: Estee_daily_discount_rank.png
[product-screenshot2]: Estee_weekly_price_change.png
