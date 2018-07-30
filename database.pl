%%
% Diseases database

% Facts
sintoma(catapora, febre).
sintoma(catapora, dor_cabeca).
sintoma(catapora, coceira).
sintoma(catapora, bolhas).
sintoma(catapora, dor_barriga).

sintoma(caxumba, febre).
sintoma(caxumba, dor_cabeca).
sintoma(caxumba, dor_garganta).
sintoma(caxumba, dor_facial).
sintoma(caxumba, inchaco_temporas).

sintoma(dengue, febre).
sintoma(dengue, dor_cabeca).
sintoma(dengue, perda_paladar).
sintoma(dengue, tontura).
sintoma(dengue, dor_olhos).

% Rules
doenca(A,B,C,D,E) :- sintoma(X, A), sintoma(X, B), sintoma(X, C), sintoma(X, D), sintoma(X, E), write(X), !.
