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

1. We loaded the dataset using pd.read_csv & stored it in the cnbc_headlines attribute.
2. We checked the first 5 rows of the dataset using cnbc_headlines.head()
3. Then we checked the shape of the dataset to analyze the number of rows & columns in the dataset using cnbc_headlines.shape
4. We also checked the columns used in the dataset using guardian_headlines.colulmns.
5. Then we analyzed the data type of the columns & data points using cnbc_headlines.info()
6. After this, we checked whether the dataset consisted of any null/nan values using cnbc_headlines.isnull().sum() & dropped the null/nan values using cnbc_headlines.dropna() since the count of null/nan values was significantly smaller than the total count of the data points in the dataset.
7. After this, we dropped the duplicate values present in the dataset using cnbc_headlines.drop_duplicates()

### Basic EDA of Guardian headlines dataset

1. We loaded the dataset using pd.read_csv & stored it in the guardian_headlines attribute.
2. We checked the first 5 rows of the dataset using guardian_headlines.head()
3. Then we checked the shape of the dataset to analyze the number of rows & columns in the dataset using guardian_headlines.shape
4. We also checked the columns used in the dataset using guardian_headlines.colulmns.
5. Then we analyzed the data type of the columns & data points using guardian_headlines.info()
6. After this, we checked whether the dataset consisted of any null/nan values using guardian_headlines.isnull().sum() & found that the dataset did not contain any null values.
7. After this, we dropped the duplicate values present in the dataset using guardian_headlines.drop_duplicates()

### Basic EDA of Reuters Headlines dataset

1. We loaded the dataset using pd.read_csv & stored it in the reuters_headlines attribute.
2. We checked the first 5 rows of the dataset using reuters_headlines.head()
3. Then we checked the shape of the dataset to analyze the number of rows & columns in the dataset using reuters_headlines.shape
4. We also checked the columns used in the dataset using reuters_headlines.colulmns.
5. Then we analyzed the data type of the columns & data points using reuters_headlines.info()
6. After this, we checked whether the dataset consisted of any null/nan values using reuters_headlines.isnull().sum() & found that the dataset did not contain any null values.
7. After this, we dropped the duplicate values present in the dataset using reuters_headlines.drop_duplicates()

### Data Preprocessing

Here, we created a function 'preprocession_text' which was used to lower the text within the dataset to lowercase. Also, stopwords, word_tokenize, PorterStemmer & WordNetLemmatizer was also used in this function for removing stopwords, tokenization of text & stemming & lemmatizing of the texts within all the 3 datasets.

