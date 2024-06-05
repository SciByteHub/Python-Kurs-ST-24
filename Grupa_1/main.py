# wyświetlanie najliczniejszego aminokwasu w białku
from rdkit import Chem
from rdkit.Chem import Draw
from colorama import Fore, Style

fenyloalanina_smiles = "NC(Cc1ccccc1)C(=O)O"
fenyloalanina_molecule = Chem.MolFromSmiles(fenyloalanina_smiles)
'''
image = Draw.MolToImage(fenyloalanina_molecule, size=(300, 300))
image.show()
'''
# oznaczenie hydrofobowych i hydrofilowych fragmentów białka

hydrophobicity_scale = {
    'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
    'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
    'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
    'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}


    # określenie progu hydrofobowości
hydrophobicity_threshold = 3

hydrophobic_aa = []
hydrophylic_aa = []

    # pętla ustalająca, jakie przy danym progu aminokwasy uwazane są za hydrofobowe lub hydrofilowe
for aa, hydrophobicity_value in hydrophobicity_scale.items():
    if hydrophobicity_value > hydrophobicity_threshold:
        hydrophobic_aa.append(aa)
    else:
        hydrophylic_aa.append(aa)

    # pokolorowanie symboli aminokwasów w zalezności od ich hydrofobowości/hydrofilowości




'''
print(f"{Fore.BLUE}Niebieski")

    # przyklad kolorowej sekwencji liter
colored_string = (
    f"{Fore.RED}H{Fore.GREEN}e{Fore.YELLOW}l{Fore.BLUE}l{Fore.MAGENTA}o{Style.RESET_ALL}, "
    f"{Fore.CYAN}W{Fore.RED}o{Fore.GREEN}r{Fore.YELLOW}l{Fore.BLUE}d!"
)

print(colored_string)
'''
# porównanie sekwencji białek, szacowanie podobieństwa



