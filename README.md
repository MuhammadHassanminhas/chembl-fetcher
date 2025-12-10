

# 🧪 ChEMBL Molecule Fetcher

**Task 4: ChEMBL Molecule Search**
A Python-based workflow to query, retrieve, and process chemical molecule data using the ChEMBL API. This tool fetches raw data, parses it into a clean format, and exports it as a CSV file for further analysis.

## 📌 Project Overview

This project provides a modular solution for extracting chemical data. It is designed with a strict "no dead code" policy, ensuring every function serves a specific purpose in the data pipeline.

**Key Features:**

  * **Targeted Retrieval:** Fetches a specific batch of molecules (default: 25).
  * **Optimized Bandwidth:** Requests only essential fields (`ID`, `Name`, `Structure`) to reduce load.
  * **Data Flattening:** Converts nested API JSON responses into a flat, tabular format.
  * **Standard Export:** Saves processed data to a clean CSV file.

## ⚙️ Installation

### Prerequisites

  * Python 3.x
  * Internet connection (to access ChEMBL web resources)

### Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/MuhammadHassanminhas/chembl-fetcher.git
    cd chembl-fetcher
    ```

2.  **Install dependencies:**

    ```bash
    pip install chembl_webresource_client pandas
    ```

## 🚀 Usage

Run the main script to execute the full ETL (Extract, Transform, Load) pipeline:

```bash
python fetch_chembl.py
```

### What happens when you run this?

1.  **Connect:** The script initializes the `chembl_webresource_client`.
2.  **Fetch:** It retrieves the first 25 molecule records from the database.
3.  **Parse:** It extracts the `ChEMBL ID`, `Preferred Name`, and `Canonical SMILES`, handling missing data gracefully.
4.  **Save:** The cleaned data is saved to `chembl_molecules.csv` in your current directory.

## 📂 Project Structure

```text
.
├── fetch_chembl.py
├── test_chembl_import.py
├── chembl_search.py        # Main script containing the full workflow
├── chembl_molecules.csv   # (Output) The generated data file
└── README.md              # Project documentation
```

## 🧠 Workflow Breakdown

The solution follows a strict, testable 4-step workflow:

| Step | Action | Description |
| :--- | :--- | :--- |
| **1** | **Connection** | Establishes a session with the ChEMBL web resource client. |
| **2** | **Retrieval** | Fetches raw objects, filtering only for necessary fields to optimize speed. |
| **3** | **Parsing** | Flattens the nested `molecule_structures` JSON into a single dictionary per molecule. |
| **4** | **Export** | Uses Pandas to write the structured list of dictionaries to a CSV file. |

## 📊 Sample Output

The resulting `chembl_molecules.csv` will look like this:

| ChEMBL\_ID | Name | SMILES |
| :--- | :--- | :--- |
| CHEMBL123 | Aspirin | CC(=O)Oc1ccccc1C(=O)O |
| CHEMBL456 | Ibuprofen | CC(C)Cc1ccc(C(C)C(=O)O)cc1 |
| ... | ... | ... |

## 📜 License

This project is open-source and available under the MIT License.
