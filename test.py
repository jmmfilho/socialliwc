from Social_LIWC import words_categorizer, phrases_categorizer, analise_social_liwc
import pandas as pd

df = pd.read_csv('Social_LIWC/dados/Testes_frases.csv')
analise = phrases_categorizer(df)
print(analise)