#biblioteki
from rdkit import Chem
from rdkit.Chem import Draw
from termcolor import colored
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# wyświetlanie najliczniejszego aminokwasu w białku

fenyloalanina_smiles = "NC(Cc1ccccc1)C(=O)O"
fenyloalanina_molecule = Chem.MolFromSmiles(fenyloalanina_smiles)

image = Draw.MolToImage(fenyloalanina_molecule, size=(300, 300))
#image.show()

# oznaczenie hydrofobowych i hydrofilowych fragmentów białka

hydrophobicity_scale = {
    'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
    'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
    'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
    'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

    # określenie progu hydrofobowości
hydrophobicity_threshold = 1.6

hydrophobic_aa = []
hydrophylic_aa = []

    # pętla ustalająca, jakie przy danym progu aminokwasy uwazane są za hydrofobowe lub hydrofilowe
for aa, hydrophobicity_value in hydrophobicity_scale.items():
    if hydrophobicity_value > hydrophobicity_threshold:
        hydrophobic_aa.append(aa)
    else:
        hydrophylic_aa.append(aa)

    # pokolorowanie symboli aminokwasów w zalezności od ich hydrofobowości/hydrofilowości

peptide_sequence = 'MYDKERHTFCIVLFIFLVYCSER'

phobic_phylic_peptide_sequence = ''

for i in peptide_sequence:
    if i in hydrophobic_aa:
        phobic_phylic_peptide_sequence += (colored(i, 'red'))
    else:
        phobic_phylic_peptide_sequence += (colored(i, 'blue'))

print(phobic_phylic_peptide_sequence)

# porównanie sekwencji białek z uzyciem biopython

peptide_sequence2 = "MENSDGVFCQAY"

alignments = pairwise2.align.globalxx(peptide_sequence, peptide_sequence2)

for alignment in alignments:
    print(format_alignment(*alignment))

#ADA
import os
import requests
import json
import joblib
from Bio import PDB
import numpy as np

def ObliczLiczbaResztAminokwasowych(pdb_entry_path):
  parser=PDB.PDBParser()
  protein=parser.get_structure('bialko',pdb_entry_path)

#liczanie reszt aminowkasowych
  residues=set()
  for model in protein:
    for chain in model:
      for residue in chain:
        if PDB.is_aa(residue, standard=True):
          residues.add(residue.id)
        
  return len(residues)

pdb_entry_path="/1AKI.pdb"

LiczbaResztAminokwasowych=ObliczLiczbaResztAminokwasowych(pdb_entry_path)
print(f"Dlugosc bialka wynosi {LiczbaResztAminokwasowych} aminokwasow")
