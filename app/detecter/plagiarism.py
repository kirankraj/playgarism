import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

from docx import *
import docx
import time
def read_docx(filename):
    try:
        doc = docx.Document(filename)  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)
        print(data)
 
    except IOError:
        print('There was an error opening the file!')
        return
# document = read_docx('C:\\Users\\sujit\\Desktop\\plarism\\1.docx')

from plagiarism.settings import STASTIC_FOLDER

def check_plagiarism(s_vectors,similarity):
    plagiarism_results = set()
    result = []
    for student_a, text_vector_a in s_vectors:

        new_vectors =s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            r = 'Duplicated' if sim_score>.60 else 'New Document'
            score = (student_pair[0],student_pair[1],r ,sim_score)
            plagiarism_results.add(score)
    for p in plagiarism_results:
        doc_path = os.path.join(STASTIC_FOLDER, 'document',p[0])
        mt = os.path.getmtime(doc_path)
        rt = time.ctime(mt)
        doc_path1 = os.path.join(STASTIC_FOLDER, 'document', p[1])
        mt1 = os.path.getmtime(doc_path1)
        rt1 = time.ctime(mt1)
        result.append({'doc1':p[0],"is":mt<mt1,'doc2':p[1],'status':p[2],'score':p[3],'doc1time':rt,'doc2time':rt1})
    return result


def checker():

    doc_path = os.path.join(STASTIC_FOLDER, 'document')


    student_files = [doc for doc in os.listdir(doc_path) if doc.endswith('.txt')]
    student_notes = [open(os.path.join(doc_path,File)).read() for File in student_files]

    vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
    similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

    vectors = vectorize(student_notes)
    s_vectors = list(zip(student_files, vectors))

    return (check_plagiarism(s_vectors,similarity))
    # for data in check_plagiarism(s_vectors,similarity):
    #     #     print(data)
        # return (np.asarray(data))