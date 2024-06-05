# wyświetlanie najliczniejszego aminokwasu w białku
from rdkit import Chem
from rdkit.Chem import Draw

fenyloalanina_smiles = "NC(Cc1ccccc1)C(=O)O"
fenyloalanina_molecule = Chem.MolFromSmiles(fenyloalanina_smiles)

image = Draw.MolToImage(fenyloalanina_molecule, size=(300, 300))
image.show()

# porównanie sekwencji białek, szacowanie podobieństwa




# oznaczenie hydrofobowych i hydrofilowych fragmentów białka