import pandas as pd # Add to imports
from chembl_webresource_client.new_client import new_client

def get_molecules(limit=25):
    molecule = new_client.molecule
    # Fetching first 'limit' molecules. 
    # specific fields are selected to reduce bandwidth and ensure no "dead data" is processed.
    res = molecule.all().only(['molecule_chembl_id', 'pref_name', 'molecule_structures'])[0:limit]
    return res

def parse_molecule_data(raw_molecules):
    clean_list = []
    for mol in raw_molecules:
        # specific handling for potential missing keys
        chembl_id = mol.get('molecule_chembl_id')
        pref_name = mol.get('pref_name')
        
        # Structure data is nested
        structure = mol.get('molecule_structures')
        smiles = structure.get('canonical_smiles') if structure else None

        clean_list.append({
            'ChEMBL_ID': chembl_id,
            'Name': pref_name,
            'SMILES': smiles
        })
    return clean_list

def save_to_file(data, filename="chembl_molecules.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} rows to {filename}")

# Update main block
if __name__ == "__main__":
    raw_data = get_molecules()
    cleaned_data = parse_molecule_data(raw_data)
    save_to_file(cleaned_data)
