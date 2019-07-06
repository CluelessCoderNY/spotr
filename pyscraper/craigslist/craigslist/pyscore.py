import nltk 
import re

def tag_list(keywords):
  return nltk.pos_tag(keywords)

def split_statement(statement):
  return nltk.word_tokenize(statement)

def split_sentences(paragraph):
  return re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)

def combine_sentences(statements):
  joined_statement = ''
  for statement in statements:
    joined_statement += statement

  return joined_statement


def doc_score(scored_statements):
  global_score = 0

  for idx, key in enumerate(scored_statements):
    global_score += scored_statements[idx]

  return global_score

def MatchNLP(tagged_keywords, statement, point_value = 1):
  tokens = nltk.word_tokenize(statement)
  tagged_words = nltk.pos_tag(tokens)

  score = 0
  for tagged_keyword in tagged_keywords:
    for tagged_word in tagged_words:
      if tagged_word == tagged_keyword:
        score += point_value

  return score

def MatchExact(keywords, statement, point_value = 2):
  tokens = nltk.word_tokenize(statement)
  
  score = 0
  for keyword in keywords:
    for token in tokens:      
      if token == keyword:
        score += point_value

  return score
