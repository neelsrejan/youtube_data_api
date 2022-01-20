from textblob import TextBlob
import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from collections import Counter

#Comment polarity
comments_df = pd.read_excel("./excel_to_tab/comment_sentiment_analysis.xlsx", header=0, na_values=['NaN', 'Null'])
all_comments = comments_df["Comment_0"].tolist() + comments_df["Comment_1"].tolist() + comments_df["Comment_2"].tolist() + comments_df["Comment_3"].tolist()
clean_comments = [comment for comment in all_comments if pd.isnull(comment) == False]
polarity = []
for comment in clean_comments:
    blob = TextBlob(comment)
    polarity.append(blob.sentiment.polarity)
word_polarity = pd.DataFrame(data = [round(sum(polarity)/len(polarity), 4)], columns=["Avg_Polarity_Of_Comments"])
word_polarity.to_excel("./excel_to_tab/comment_polarity.xlsx", index=False)


#Word Cloud
titles_df = pd.read_excel("./excel_to_tab/related_videos_word_cloud.xlsx", header=0)
titles = titles_df["Related_Video_Title"].str.lower().tolist()

stop_words = set(stopwords.words("english"))
stop_words.update([".", "?", "!", "|", "(", ")", "@", "$", "-", "`", "'", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
tokenizer = RegexpTokenizer(r'\w+')

filtered_titles = []
for title in titles:
    tokenized_word = tokenizer.tokenize(title)
    for token in tokenized_word:
        if token not in stop_words:
            filtered_titles.append(token)

counter = Counter(filtered_titles)
occurrences = pd.DataFrame.from_records(counter.most_common(), columns=["Word", "Num_Occurences"])
occurrences.to_excel("./excel_to_tab/word_cloud.xlsx", index=False)
