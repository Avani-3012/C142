from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

p1 = pd.read_csv("shared_articles.csv")
p2 = pd.read_csv("users_interactions.csv")
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(p1['title'])

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

p1 = p1.reset_index()
indices = pd.Series(p1.index, index=p1['contentId'])

def get_recommendations(contentId, cosine_sim):
    idx = indices[contentId]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return p1['contentId'].iloc[movie_indices]

get_recommendations(-4029704725707465084, cosine_sim2)