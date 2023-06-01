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
* Search for the maximize discount on products.
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

Start with a python file with any machine learning model ex.NaiveBayes.py  
Download code and repalce the api_key to your own.

### Prerequisites


1. Get a free API Key at [NewsAPI](https://newsapi.org/docs/client-libraries/python)
2. Replace api_key to your own.
   ```sh
   newsapi = NewsApiClient(api_key=' your api key here ')
   ```
3. Run the python file
   
4. Check the plot to see predict results



<!-- USAGE EXAMPLES -->
## Usage

Use the plots to check result.  
### Data 
Articles: {'science': 61, 'general': 226, 'health': 133, 'business': 294, 'entertainment': 270, 'sports': 341}
![DataAccumulation][product-screenshot0]  
![Data][product-screenshot1]  
 
### Accuracy
- Naive Bayes: 0.539156
- SVM: 0.608433
- Logistic Regression: 0.551204  
![SupervisedLearning][product-screenshot2]  

### confused matrix 
![NaiveBayes][product-screenshot3]  

or copy an article content and apply it on the model to make predition.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).


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
[product-screenshot]: images/screenshot.png
