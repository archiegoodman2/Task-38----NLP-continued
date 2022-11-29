#since the similarties between cat, monkey and banana were already commented on in the notes,
#I'm going to experiment with an entirely new example 
print('''MD Module: 
''')
import spacy 
nlp = spacy.load('en_core_web_md')

word1 = nlp("river")
word2 = nlp("water")
word3 = nlp("bottle")

words = [word1, word2,  word3]

#we really dont need this loop here but I want to practise looping though and assigning similarities
for token1 in words :                 #we have 2 loops simultaneously to compare the two outputs
    for token2 in words:              
        if token1 != token2 :         #but we don't want to compare water and water for example
            print(f'''The similarity between {token1.text} and {token2.text} is: {token1.similarity(token2)}
        ''')

#OBSERVATIONS:
#similarity between river and water is high
#similarity between water and bottle is high
#but the similarity between river and bottle is about half of these! much lower
#so clearly spaCy has identified that while a river is made of water, we cannot really have...
#... a bottle of river. Whereas we can have a bottle of water.
#so here it is comprehending basic human common sense, which is pretty impressive

print('''SM Module 
''')

nlp = spacy.load('en_core_web_sm')

word1 = nlp("river")
word2 = nlp("water")
word3 = nlp("bottle")

words = [word1, word2,  word3]


for token1 in words :                 
    for token2 in words:              
        if token1 != token2 :        
            print(f'''The similarity between {token1.text} and {token2.text} is: {token1.similarity(token2)}
        ''')

#OBSERVATIONS:
#With this less advanced language model, the similarity between bottle and river (0.60) is roughly comparable to...
#... the similarity between water and river (0.61).
#This demonstrates the less advanced nature of this language model, as it is not able to distinguish that you can have a waterbottle...
#...but not a riverbottle, at least in coloquial language.
