#!/usr/bin/env python3

from pyswip import Prolog

def query_disease(s1, s2, s3, s4, s5):
    prolog = Prolog()
    prolog.consult('./database.pl')
    s = "doenca(X, %s, %s, %s, %s, %s)" % (s1, s2, s3, s4, s5)
    print(s)
    query = list(prolog.query(s))
    print(query)
    if len(query) > 0:
        return query[0]["X"]
    else:
        return 'virose'

query_disease("febre", "dor_cabeca", "coceira", "bolhas", "dor_barriga")

def test_catapora():
    assert query_disease("febre", "dor_cabeca", "coceira", "bolhas", "dor_barriga") == 'catapora'
    assert query_disease("febre", "dor_cabeca", "coceira", "bolhas", "rabiga") == 'virose'

def test_caxumba():
    assert query_disease("febre", "dor_cabeca", "dor_garganta", "dor_facial", "inchaco_temporas") == 'caxumba'
    assert query_disease("febre", "dor_cabeca", "coceira", "dor_nenhuma", "teste") == 'virose'

def test_dengue():
    assert query_disease("febre", "dor_cabeca", "perda_paladar", "tontura", "dor_olhos") == 'dengue'
    assert query_disease("febre", "dor_cabeca", "perda_paladar", "tontura", "dor_vista") == 'virose'
