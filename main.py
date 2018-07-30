#!/usr/bin/env python3

from pyswip import Prolog

def query_disease(s1, s2, s3, s4, s5):
    prolog = Prolog()
    prolog.consult('./database.pl')
    s = "doenca(%s, %s, %s, %s, %s)" % (s1, s2, s3, s4, s5)
    print(s)
    query = list(prolog.query(s))
    if len(query) <= 0:
        return False
    else:
        return True

def test_catapora():
    assert query_disease("febre", "dor_cabeca", "coceira", "bolhas", "dor_barriga") == True
    assert query_disease("febre", "dor_cabeca", "coceira", "bolhas", "rabiga") == False

def test_caxumba():
    assert query_disease("febre", "dor_cabeca", "dor_garganta", "dor_facial", "inchaco_temporas") == True
    assert query_disease("febre", "dor_cabeca", "coceira", "dor_nenhuma", "teste") == False

def test_dengue():
    assert query_disease("febre", "dor_cabeca", "perda_paladar", "tontura", "dor_olhos") == True
    assert query_disease("febre", "dor_cabeca", "perda_paladar", "tontura", "dor_vista") == False
