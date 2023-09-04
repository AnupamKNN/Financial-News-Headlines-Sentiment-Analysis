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
5. The function 'get_analysis' was applied on the 'ds_score' column using 'apply' function to analyze the sentiment of the description data and a count plot was plotted on the description score to check the count of the sentiments of the 3 sentiment categories.



### Modeling on Description

1. The dataset was split for training and testing using train test split where the training data set contained 90% of 'Description' & 'ds_score' data & testing dataset contained
10 % of that data.
2 Various classification models were trained & tested as the problem is classification-based. The models were trained & tested for their accuracy of prediction. Here is the list of those models with their respective accuracy score:-

- Linear Support Vector Machine:- 93.43
- Logistic Regression - 89.46%
- Multinomial Naive Bayes - 62.31%
- Bernoulli Naive Bayes - 62.31%
- Gradient Boosting Classification Model - 42.68%
- XGBoost Classificattion Model - 49.62%
- Decision Tree  Classification - 51.2%
- K - Nearest Neighbour Classifier Model - 57.26%

3. The model with the highest accuracy was the Linear Support Vector Machine (LinearSVM) which was chosen for predicting sentiments of description data.

### Working with headlines + description

1. A new column 'info' was added to the new_data data frame which contained both headlines data along the description data.
2. Columns 'Headlines', 'Description' & 'ds_score' were dropped, retaining only 'info' column.
3. The text data in the 'info' column was again preprocessed using 'preprocession_text' column & polarity scores were deduced & stored in 'info_score' column. The function 'get_analysis' was applied on the 'info_score' column to get the sentiment analysis.
4. A count plot was distributed to analyze the count of each sentiment of the 3 sentiment categories.



### Modeling on headlines + description

1. The dataset was split for training and testing using train test split where the training data set contained 90% of 'info' & 'info_score' data & testing dataset contained
10 % of that data.
2 Various classification models were trained & tested as the problem is classification-based. The models were trained & tested for their accuracy of prediction. Here is the list of those models with their respective accuracy score:-

- Linear Support Vector Machine:- 90.7%
- Logistic Regression - 87.23%
- Multinomial Naive Bayes - 64.62%
- Bernoulli Naive Bayes - 64.62%
- Gradient Boosting Classification Model - 44.26%
- XGBoost Classificattion Model - 50.78%
- Decision Tree  Classification - 53.17%
- K - Nearest Neighbour Classifier Model - 56.16%

3. The model with the highest accuracy was the Linear Support Vector Machine (LinearSVM) which was chosen for predicting sentiments of headlines + description data.

### Working on headlines

1. 'new_data_copy' data frame is used here and 'Description' column was dropped.
2. In the 'guradian_headlines' data frame, column 'Date' was renamed to 'Time'.
3. A new data frame 'all_headlines' was created which contained headlines of all 3 news headlines dataset. 'pd.concat' was used to concatenate 'guardian_headlines' and 'new_data_copy' & this concatenated data was then stored in 'all_headlines' dataframe/
4. Now, the text data, i.e. the headlines was preprocessed using 'preprocession_text' function & their polarity score was deduced & stored in 'hl_score' column.
5. Thereafter, 'get_analysis' function was applied on the 'hl_score' column to get the sentiment analysis.
6. A count plot was distributed to analyze the count of each sentiment of the 3 sentiment categories.



### Modeling on headlines

1. The dataset was split for training and testing using train test split where the training data set contained 90% of 'Headlines' & 'hl_score' data & testing dataset contained
10 % of that data.
2 Various classification models were trained & tested as the problem is classification-based. The models were trained & tested for their accuracy of prediction. Here is the list of those models with their respective accuracy score:-

- Linear Support Vector Machine:- 97.45%
- Logistic Regression - 94.18%
- Multinomial Naive Bayes - 84.28%
- Bernoulli Naive Bayes - 84.28%
- Gradient Boosting Classification Model - 43.67%
- XGBoost Classificattion Model - 59.65%
- Decision Tree  Classification - 59.14%
- K - Nearest Neighbour Classifier Model - 65.38%

3. The model with the highest accuracy was the Linear Support Vector Machine (LinearSVM) which was chosen for predicting sentiments of headlines data.

# Prediction

1. Now that the model has been developed, the results can be checked om realtime news.
2. With the help of 'pickle', a pickle file was developed which was then utilized for the development of a web application.
