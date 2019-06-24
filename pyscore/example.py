import pyscore

def gen_score(statement):
  score = 0
  score += pyscore.MatchExact(keywords, statement)
  score += pyscore.MatchNLP(tagged_keywords, statement)
  return score

keywords = ["roadtrek", "miles", "generator",  "condition"]

paragraph = "Clean original condition. It is the Cadillac of clack C motor homes V-10 6.8 L engine is the ideal power plant. Consistent 14 mpg. If you google 2007 Gulf Stream B Touring cruiser you can review the new model 6 page dealer brochure. They had evert reason to brag about the superior construction, design, fit and finish. I am the 2nd owner, purchased in 2012 when it had 3,800 miles. Photos reflect 3 flaws 1) vanity mirror cracked corner. 2) Leather couch base where it skims carpet when you bump it out has a tear at base. 3) passenger side rear corner scrapped a post and cracked trim piece and scratches. The adage good as new doesn't apply because I installed air ride bags to the rear axle. A $2,000 investment in 0 - 60 psi ride adjustability.. I bought it on my car dealership license and drove it with a dealer plate. I'll have to do the title paperwork for the purchaser."

tagged_keywords = pyscore.tag_list(keywords)
sentences = pyscore.split_sentences(paragraph) 

scored_statements = {}
for idx, statement in enumerate(sentences):
  scored_statements[idx] = gen_score(statement)

sorted_scored_statements = sorted(scored_statements.items(), key=lambda kv: kv[1])

print("Global Score: ", pyscore.doc_score(scored_statements))
for statement_key in sorted_scored_statements:
  print(sentences[statement_key[0]])