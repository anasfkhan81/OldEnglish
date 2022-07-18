import wn
import csv

def word2syn(s):
    word_syn = {}
    words = wn.words(s)

    for w in words:
        lemma = w.lemma()+'_'+ w.pos
        word_syn[lemma] = {'lemma':w.lemma(), 'pos': w.pos, 'syn':{}}
        for sy in w.synsets():
            lemma_list = '; '.join(sy.lemmas())
            word_syn[lemma]['syn'][sy.ili.id] = {'definition': sy.definition(), 'synonyms': lemma_list}

    return word_syn


def write_syns(d,s):
    file_name = s+ '_syns.csv'
    field_names = ['lemma', 'part of speech', 'synset_ili', 'definition', 'synonyms']
    with open(file_name, mode = 'w', encoding='UTF8', newline='') as syn_file:
        #syn_writer = csv.writer(syn_file,delimiter='\t')
        syn_writer = csv.writer(syn_file)
        syn_writer.writerow(field_names)
        for k in d.keys():
            for ss in d[k]['syn']:
                print(d[k]['syn'][ss]['synonyms'])
                syn_writer.writerow([d[k]['lemma'], d[k]['pos'], ss, d[k]['syn'][ss]['definition'], d[k]['syn'][ss]['synonyms']])
