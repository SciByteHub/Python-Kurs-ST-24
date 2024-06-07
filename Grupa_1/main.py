#biblioteki
from rdkit import Chem
from rdkit.Chem import Draw
from termcolor import colored
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# wyświetlanie najliczniejszego aminokwasu w białku

aminokwasy ={
    'fenyloalanina': "NC(Cc1ccccc1)C(=O)O",
    'glicyna': "NCC(=O)O",
    "alanina": "CC(C(=O)O)N",
    "cysteina": "C(C(C(=O)O)N)S",
    "lizyna": "C(CCN)CC(C(=O)O)N",
    'walina': 'CC(C)C(C(=O)O)N',
    'leucyna': 'CC(C)CC(C(=O)O)N',
    'izoleucyna': 'CCC(C)C(C(=O)O)N',
    'prolina': 'C1CC(NC1)C(=O)O',
    'tyrozyna': 'NC(Cc1ccc(O)cc1)C(=O)O',
    'tryptofan': 'NC(Cc1c[nH]c2c1cccc2)C(=O)O',
    'seryna': 'C(O)C(C(=O)O)N',
    'treonina': 'CC(O)C(N)C(=O)O',
    'metionina': 'CSCCC(C(=O)O)N',
    'asparagina': 'C(N)(=O)CC(N)C(=O)O',
    'glutamina': 'C(CC(=O)N)C(C(=O)O)N',
    'kwas asparaginowy': 'C(=O)(O)C(N)CC(=O)O',
    'kwas glutaminowy': 'C(CC(=O)O)C(C(=O)O)N',
    'arginina': 'C(C(C(=O)O)N)CCNC(=N)N',
    'histydyna': 'C(=O)(O)C(N)C(c1cNcn1)'
}

aa_molecule = Chem.MolFromSmiles(aminokwasy['histydyna'])

image = Draw.MolToImage(aa_molecule, size=(300, 300))
image.show()

# oznaczenie hydrofobowych i hydrofilowych fragmentów białka
"""
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

#Obliczanie ilości reszt aminokwasowych
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

#Obliczanie dlugosci bialka w angstremach
def ObliczDlugoscBialka(pdb_entry_path):
  parser=PDB.PDBParser()
  protein=parser.get_structure('bialko',pdb_entry_path)

#wyznaczenie "krawędzi" białka
  min_coord = np.array([np.inf, np.inf, np.inf])
  max_coord = np.array([-np.inf, -np.inf, -np.inf])

#przeliczanie po strukturze
  for model in protein:
    for chain in model:
      for residue in chain:
        for atom in residue:
          coord=atom.coord
          min_coord = np.minimum(min_coord, coord)
          max_coord = np.maximum(max_coord, coord)

#wyznaczenie wektora odleglosci i jego zmierzenie
  dlugosc = max_coord - min_coord
  DlugoscBialka=np.linalg.norm(dlugosc)

  return DlugoscBialka
    
#import białka
  pdb_entry_path="/1AKI.pdb"
  
#Printowanie odpowiedzi
DlugoscBialka=ObliczDlugoscBialka(pdb_entry_path)
print(f"Dlugosc bialka: {DlugoscBialka:2f} Å")

#wizualizacja białka

import icn3dpy

def WizualizacjaStrukturyBialka(ID, protein_style='cylinder and plate', ligand_style='ball and stick'):
    style = f'bialko {protein_style}; ligand {ligand_style}'
    
    # Tworzenie widoku 3D
    scene = icn3dpy.view(q=ID, command=style)
    
    return scene

# podanie ID białka i otworzenie wizualizacji
ID = 'pdbid=5tyc'
scene = WizualizacjaStrukturyBialka(ID)
scene
"""