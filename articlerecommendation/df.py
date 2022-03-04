import pandas as pd
import numpy as np

p1 = pd.read_csv("shared_articles.csv")
p2 = pd.read_csv("users_interactions.csv")
p1.head()
p2.head()
p1 = p1[p1['eventType'] == 'CONTENT SHARED']
p1.head()
p2.shape
p1.shape

def find_total_events(df1_row):
    l = p2[(p2["contentId"] == df1_row["contentId"]) & (p2["eventType"] == "LIKE")].shape[0]
    v = p2[(p2["contentId"] == df1_row["contentId"]) & (p2["eventType"] == "VIEW")].shape[0]
    b = p2[(p2["contentId"] == df1_row["contentId"]) & (p2["eventType"] == "BOOKMARK")].shape[0]
    f = p2[(p2["contentId"] == df1_row["contentId"]) & (p2["eventType"] == "FOLLOW")].shape[0]
    c = p2[(p2["contentId"] == df1_row["contentId"]) & (p2["eventType"] == "COMMENT CREATED")].shape[0]
    return l+v+b+f+c

p1["total_events"] = p1.apply(find_total_events, axis=1)

p1.head()

p1 = p1.sort_values(['total_events'], ascending=[False])

p1.head()
output = p1["LIKE","VIEW","BOOKMARK","COMMENT CREATED"].head(20)