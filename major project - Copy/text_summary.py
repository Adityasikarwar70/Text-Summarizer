import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from textblob import TextBlob as tbp
from string import punctuation
from heapq import nlargest

text = "A powerful fox known as the Nine-Tails attacks Konoha, the hidden leaf village in the Land of Fire, one of the Five Great Shinobi Countries in the Ninja World. In response, the leader of Konoha and the Fourth Hokage, Minato Namikaze, at the cost of his life, seals the fox inside the body of his newborn son, Naruto Uzumaki, making him a host of the beast.[i] The Third Hokage returns from retirement to become the leader of Konoha again. Naruto is often scorned by Konoha's villagers for being the host of the Nine-Tails. Due to a decree by the Third Hokage forbidding any mention of these events, Naruto learns nothing about the Nine-Tails until 12 years later, when Mizuki, a renegade ninja, reveals the truth to him. Naruto defeats Mizuki in combat, earning the respect of his teacher, Iruka Umino.[ii] Shortly afterward, Naruto Naruto becomes a ninja and joins with Sasuke Uchiha, against whom he often competes, and Sakura Haruno, on whom he has a crush, to form Team 7, under an experienced sensei, the elite ninja Kakashi Hatake. Like all the ninja teams from every village, Team 7 completes missions requested by the villagers, ranging from doing chores and being bodyguards to performing assassinations."


def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)
   
    tokens = [token.text for token in doc]
    # print(tokens)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
            
    # print(word_freq)

    max_freq = max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
                
    # print(sent_scores)

    select_len = int(len(sent_tokens) * 0.4)
    # print(select_len)
    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(text )
    
     #print("\n")
    # print(summary)

    # print("Length of original text - " , len(text.split(' ')))
    # print("Length of summary text - " , len(summary.split(' ')))
    
    return summary, doc ,len(rawdocs.split(' ')), len(summary.split(' '))