### Financial News Headlines Sentiment Analysis

### Software & Tools Requiremntts

1. [Github Accounts](https://github.com)
2. [GitCLI](https://git-scm.com/)
3. [Anaconda](https://www.anaconda.com/)
4. [VS Code IDE](https://code.visualstuido.com/)


Create a new environment
```
conda create -p venv python -y
```

Assign User Name

```
git config --global user.name "Your name"
```

Assign Email used to create Github Account

```
git config --global user.email "You@example.com"
```

Install ipykernel within the environment in the terminal before running jupyter notebook.

```
pip install ipykernel
```

### Introduction (Problem Statement)

News headlines play a crucial role as they assist people in analyzing whether that particular news is worth their time or not. More importantly, it also helps in analyzing whether the news is positive, negative, or neutral as the polarity of the news helps in making investment decisions. In this project, we are required to predict the sentiment of the news by assessing the sentiment of the news headlines.

### Information about the dataset

The data set includes news headlines from three news forums, namely Reuters, CNBC & The Guardian. The dataset used was downloaded from Kaggle.

##### Columns Provided in the Dataset:-

CNBC headline:
1. Time
2. Headlines
3. Description

The Guardian headline:
1. Time
2. Headline

Reuters headline:
1. Time
2. Headline
3. Description

### Basic EDA of CNBC Headlines dataset

1. The dataset was loaded using pd.read_csv & stored in the cnbc_headlines attribute.
2. The first 5 rows of the dataset were checked using cnbc_headlines.head()
3. Then the shape of the dataset was checked to analyze the number of rows & columns in the dataset using cnbc_headlines.shape
4. The columns used in the dataset were also checked using guardian_headlines.colulmns.
5. The analysis of the data type of the columns & data points was performed using cnbc_headlines.info()
6. After this, whether the dataset consisted of any null/nan values, was checked using cnbc_headlines.isnull().sum() & dropped the null/nan values using cnbc_headlines.dropna() since the count of null/nan values was significantly smaller than the total count of the data points in the dataset.
7. After this, the duplicate values present in the dataset were dropped using cnbc_headlines.drop_duplicates()

### Basic EDA of Guardian headlines dataset

1. The dataset was loaded using pd.read_csv & stored in the guardian_headlines attribute.
2. The first 5 rows of the dataset were checked using guardian_headlines.head()
3. Then the shape of the dataset to analyze the number of rows & columns in the dataset was checked using guardian_headlines.shape
4. The columns used in the dataset were checked using guardian_headlines.colulmns.
5. The analysis of the data type of the columns & data points was performed using guardian_headlines.info()
6. After this, whether the dataset consisted of any null/nan values was checked using guardian_headlines.isnull().sum() & found that the dataset did not contain any null values.
7. After this, the duplicate values present in the dataset were dropped using guardian_headlines.drop_duplicates()

### Basic EDA of Reuters Headlines dataset

1. The dataset was loaded using pd.read_csv & stored in the reuters_headlines attribute.
2. The first 5 rows of the dataset were checked using reuters_headlines.head()
3. The shape of the dataset to analyze the number of rows & columns in the dataset was checked using reuters_headlines.shape
4. The columns used in the dataset were checked using reuters_headlines.colulmns.
5. The analysis of the data type of the columns & data points was performed using reuters_headlines.info()
6. After this, whether the dataset consisted of any null/nan values was checked using reuters_headlines.isnull().sum() & found that the dataset did not contain any null values.
7. After this, the duplicate values present in the dataset were dropped using reuters_headlines.drop_duplicates()

### Data Preprocessing

Here, a function 'preprocession_text' was created which was used to lower the text within the dataset to lowercase. Also, stopwords, word_tokenize, PorterStemmer & WordNetLemmatizer were also used in this function for removing stopwords, tokenization of text & stemming & lemmatizing of the texts within all the 3 datasets respectively using Natural Language Toolkit (NLTK) library.

### Sentiment Analysis

Now, the 'SentimentIntensityAnalyzer' algorithm was imported using nltk.sentiment.vader for sentiment analysis and was stored in 'analyzer' attribute. A function 'get_analysis' was created with 'score' as the argument/parameter. An if-else condition was established in the function where

- if score < 0,  return 'negative'
- elif score == 0, return 'neutral'
- else > 0, return 'positive'

### Working with the description on datasets

1. Here, the descriptions from cnbc_headlines & reuters_headlines were concatenated using pd.concat and the concatenated data was stored in the new_data attribute.
2. A new attribute 'new_data_copy' was created which was used to store the copy of new_data attribute using 'copy' function.
3. On the description wihtin the new_data dataframe, the function 'preprocession_text' was applied using 'apply' function for preprocessing the description data.
4. The polarity score of the descriptions was deduced & stored in the column 'ds_score' using polarity_score
5. The function 'get_analysis' was applied on the 'ds_score' column using 'apply' function to analyze the sentiment of the description data and a count plot & a pie chart were plotted on the description score & proportion of different sentiments within the data set.




