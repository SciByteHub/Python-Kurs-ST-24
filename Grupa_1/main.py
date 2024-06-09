#biblioteki
from rdkit import Chem
from rdkit.Chem import Draw
from termcolor import colored
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.PDB.PDBParser import PDBParser
from ramachandraw.utils import fetch_pdb, plot
import json
import joblib
from Bio import PDB
import icn3dpy


aminokwasy ={
    'F': "NC(Cc1ccccc1)C(=O)O",
    'G': "NCC(=O)O",
    "A": "CC(C(=O)O)N",
    "C": "C(C(C(=O)O)N)S",
    "K": "C(CCN)CC(C(=O)O)N",
    'V': 'CC(C)C(C(=O)O)N',
    'L': 'CC(C)CC(C(=O)O)N',
    'I': 'CCC(C)C(C(=O)O)N',
    'P': 'C1CC(NC1)C(=O)O',
    'Y': 'NC(Cc1ccc(O)cc1)C(=O)O',
    'W': 'NC(Cc1c[nH]c2c1cccc2)C(=O)O',
    'S': 'C(O)C(C(=O)O)N',
    'T': 'CC(O)C(N)C(=O)O',
    'M': 'CSCCC(C(=O)O)N',
    'N': 'C(N)(=O)CC(N)C(=O)O',
    'Q': 'C(CC(=O)N)C(C(=O)O)N',
    'D': 'C(=O)(O)C(N)CC(=O)O',
    'E': 'C(CC(=O)O)C(C(=O)O)N',
    'R': 'C(C(C(=O)O)N)CCNC(=N)N',
    'H': 'C(=O)(O)C(N)C(c1cNcn1)'
}

hydrophobicity_scale = {
    'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
    'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
    'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
    'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

#os things
pdb_entry = input("Wprowadź PDB ID białka które chcesz zbadać: ")
os.mkdir(pdb_entry) #tworzy folder o nazwie pdb_entry
os.chdir(pdb_entry) #zmienia PWD na folder pdb_entry, wszystkie dane będą zapisywane w tym folderze

# pierwsza funkcja, pobiera PDB
def Download(pdb_entry):
    url = f"https://files.rcsb.org/download/{pdb_entry}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{pdb_entry}.pdb", "wb") as file:
            file.write(response.content)
            print(f"Plik został pobrany pomyślnie w folderze {pdb_entry}!")
    else:
        print("Nie udało się pobrac pliku!")
Download(pdb_entry)

# druga funkcja zapisuje sekwencję białka do pliku seq_pdb_entry.txt
def GetSequence(pdb_entry):
    sequence = f'{pdb_entry}.pdb'
    for sequence in SeqIO.parse(sequence, "pdb-seqres"):
        file1 = open(f'seq_{pdb_entry}.txt', 'w')
        file1.write(f'Sekwencja białka {pdb_entry}:\n {sequence.seq}')
        file1.close()
        print(f'Sekwencja została pomyślnie zapisana do pliku seq_{pdb_entry}.txt!')
GetSequence(pdb_entry)

#trzecia funkcja liczy częstotliwość pojawiania się aminokwasu w sekwencji i zapisuje wykres do pliku Plot1.png oraz wyświetlająca najliczniejszy aminokwas
def AAcount(pdb_entry):
    sequence = f'{pdb_entry}.pdb'
    for sequence in SeqIO.parse(sequence, "pdb-seqres"):
        sequence = str(sequence.seq)
        analysed_sequence = ProteinAnalysis(sequence)
        aacount = analysed_sequence.count_amino_acids()
        labels = list(aacount.keys())
        sizes = list(aacount.values())
        max_amino_acid = max(aacount, key=aacount.get)
        fig, ax = plt.subplots(figsize=(10,10))
        ax.pie(sizes,labels=labels,autopct='%1.1f%%', pctdistance=1.2, labeldistance=0.6, startangle=90)
        plt.title(f'Udział procentowy aminokwasów w sekwencji białka {pdb_entry}')
        plt.savefig(f'Sequence_plot_{pdb_entry}.png')
        print(f'Procentowa zawartość aminokwasów została pomyślnie zapisana na wykresie pliku Sequence_plot_{pdb_entry}.png!')
    aa_molecule = Chem.MolFromSmiles(aminokwasy[max_amino_acid])
    image = Draw.MolToImage(aa_molecule, size=(300, 300))
    image.show()

AAcount(pdb_entry)

#czwarta funkcja rysuje wykres Ramachandrana na podstawie danych w PDB
def RamachandranPlot(pdb_entry):
    ram_plot = f"{pdb_entry}.pdb"
    plot(ram_plot, save=True, show=False, filename=f'Ramachandran_plot_{pdb_entry}.png')
    print(f'Wyres Ramachandrana został pomyślnie zapisany do pliku Ramachandran_plot_{pdb_entry}.png!')

RamachandranPlot(pdb_entry)

# określenie progu hydrofobowości
hydrophobic_aa = []
hydrophylic_aa = []


# pokolorowanie symboli aminokwasów w zalezności od ich hydrofobowości/hydrofilowości

def FragmentyHydrofobowe(pdb_entry):
    threshold = float(input('Podaj granicę hydrofobowości: '))
    for aa, hydrophobicity_value in hydrophobicity_scale.items():
      if hydrophobicity_value > threshold:
        hydrophobic_aa.append(aa)
      else:
        hydrophylic_aa.append(aa)
    
    phobic_phylic_peptide_sequence = ''

    sequence = f'{pdb_entry}.pdb'
    for sequence in SeqIO.parse(sequence, "pdb-seqres"):
        sequence = str(sequence.seq)

    for i in sequence:
      if i in hydrophobic_aa:
        phobic_phylic_peptide_sequence += (colored(i, 'red'))
      else:
        phobic_phylic_peptide_sequence += (colored(i, 'blue'))
    print(phobic_phylic_peptide_sequence)

FragmentyHydrofobowe(pdb_entry)

'''
# porównanie sekwencji białek z uzyciem biopython
peptide_sequence = 'MYDKERHTFCIVLFIFLVYCSER'
peptide_sequence2 = "MENSDGVFCQAY"

alignments = pairwise2.align.globalxx(peptide_sequence, peptide_sequence2)

for alignment in alignments:
    print(format_alignment(*alignment))
'''
#ADA


#Obliczanie ilości reszt aminokwasowych
def ObliczLiczbaResztAminokwasowych(pdb_entry):
  parser=PDB.PDBParser()
  protein=parser.get_structure('bialko', f'{pdb_entry}.pdb')

#liczanie reszt aminowkasowych
  residues=set()
  for model in protein:
    for chain in model:
      for residue in chain:
        if PDB.is_aa(residue, standard=True):
          residues.add(residue.id)
        
  print(f'W białku jest {len(residues)} reszt aminokwasowych')

ObliczLiczbaResztAminokwasowych(pdb_entry)


#Obliczanie dlugosci bialka w angstremach
def ObliczDlugoscBialka(pdb_entry):
  parser=PDB.PDBParser()
  protein=parser.get_structure('bialko', f'{pdb_entry}.pdb')

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

  print(f"Dlugosc bialka: {DlugoscBialka:2f} Å")
  
ObliczDlugoscBialka(pdb_entry)


#wizualizacja białka

def WizualizacjaStrukturyBialka(pdb_entry, protein_style='cylinder and plate', ligand_style='ball and stick'):
    style = f'bialko {protein_style}; ligand {ligand_style}'
    
    # Tworzenie widoku 3D
    scene = icn3dpy.view(q=pdb_entry, command=style)
    
    return scene

# podanie ID białka i otworzenie wizualizacji
ID = 'pdbid=5tyc'
WizualizacjaStrukturyBialka(pdb_entry)=scene

