import pandas as pd

rcols = ['user_id','movie_id','rating']
ratings = pd.read_csv(r'C:\Users\win\Downloads\udemy-frank-master\udemy-frank-master\ml-100k\u.data', sep='\t', names= rcols, usecols = range(3))