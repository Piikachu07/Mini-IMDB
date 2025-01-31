# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 22:56:34 2024

@author: User
"""

import pickle

def load_movie_data():
    with open('recommend/movie_list.pkl', 'rb') as f:
        movie = pickle.load(f)
    return movie

def load_content_similarity():
    with open('recommend/similarity.pkl', 'rb') as f:
        content_similarity = pickle.load(f)
    return content_similarity

def load_knn_model():
    with open('recommend/knn.pkl', 'rb') as f:
        knn = pickle.load(f)
    return knn