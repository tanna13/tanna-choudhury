import pickle
import os
import pandas as pd

def countingPhrase():
    
    dictionary_phrase = {} #make a dictionary that used key value
    f = open("D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/dictionary",'rb')
    spam_dict = pickle.load(f)
    f.close()
    files = os.listdir(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR")
    for file in files:
        fp = open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR/"+file,encoding='utf-8')
        try:
            text = fp.read()
        except:
            continue
        count = 0
        for phrase in spam_dict:
            text = text.lower()
            phrase = phrase.lower()
            if phrase in text:
                count += 1
        dictionary_phrase[file] = count
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/phrasecount", 'wb') as fp:
        pickle.dump(dictionary_phrase,fp)
        fp.close()

def countLines():
    dictionary_lines = {}
    files = os.listdir(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR")
    for file in files:
        fp = open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR/"+file,encoding='utf-8')
        try:
            text = fp.read()
        except:
            continue
        count = text.count("\n")
        dictionary_lines[file] = count
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/linecount", 'wb') as fp:
        pickle.dump(dictionary_lines,fp)
        fp.close()        

def count_attachments():
    num_of_attachments = {}
    files = os.listdir(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR")
    for file in files:
        fp = open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR/"+file,encoding='utf-8')
        try:
            text = fp.read()
        except:
            continue
        index = text.lower().find("attachment")
        count = 0
        if index > 0:
            i = index + len("attachment")
            while text[i]!='\n':
                if text[i].isnumeric():
                    count = count*10 + int(text[i])
                i += 1
        num_of_attachments[file] = count
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/attachcount","wb") as fp:
        pickle.dump(num_of_attachments,fp)
        fp.close()


def character_count():
    num_of_characters = {}
    files = os.listdir(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR")
    for file in files:
        fp = open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR/"+file,encoding='utf-8')
        try:
            text = fp.read()
        except:
            continue
        count = 0
        character_array = {"$","#","*","_","%"}
        for char in character_array:
            count += text.count(char)
        num_of_characters[file] = count

    with open("char_count",'wb') as f:
        pickle.dump(num_of_characters,f)
        f.close()

def gather_features_into_dataframe():
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/phrasecount", 'rb') as fp:
        phrase_count = pickle.load(fp)
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/charcount", 'rb') as fp:
        char_count = pickle.load(fp)
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/linecount", 'rb') as fp:
        line_count = pickle.load(fp)
    with open(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/attachcount", 'rb') as fp:
        attach_count = pickle.load(fp)

    #list_of_emails = os.listdir(r"D:/CSE 8th semester/PROJECT IDEAS/8thsem_project/TR")
    #index_of_emails = map(lambda eml: int(''.join([x for x in eml if x.isdigit()])),list_of_emails)
    records = []
    for key in char_count.keys():
        index = int(''.join([x for x in eml if x.isdigit()]))
        records.append((index, char_count[key], attach_count[key], line_count[key], phrase_count[key]))
    labels = ["index","charactercount","attachmentcount","linecount","spamphraseccount"]
    features = pd.DataFrame.from_reccords(records, columns=labels)
    with open("features","rb") as fp:
        pickle.dump(features,fp)

