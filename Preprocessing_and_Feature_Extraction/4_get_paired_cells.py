import numpy as np
import pickle
from dataclasses import dataclass
import os

# Import general functions from preprocess_utils file.
from preprocess_utils import load_config_from_json

# Create a class to extract the required elements from the config.json that are used here, and load as config. 
@dataclass
class Config:
    RecordingFolder: str
    AnalysisFile: str
    CellMatchFile: str
    RecordingFolder2: str

# If config.json is in the parent directory
config_path = os.path.join('..', 'config.json')
config = load_config_from_json(config_path, Config)

BASE_PATH = config.RecordingFolder
BASE_PATH_2 = config.RecordingFolder2
CELL_DICT_FILE = config.AnalysisFile
CELL_DICT_FILE_OUT = CELL_DICT_FILE
CELL_MATCH_FILE = config.CellMatchFile


# Create file paths to load the pre and post recording cell dictionaries.
dict_path_1 = BASE_PATH + 'cells.pkl'
dict_path_2 = BASE_PATH_2 + 'cells.pkl'

iscell_1 = BASE_PATH + 'iscell.npy'
iscell_2 = BASE_PATH_2 + 'iscell.npy'

# Open cell dictionaries
with open(dict_path_1, 'rb') as f:
    cell_dict_1 = pickle.load(f)

with open(dict_path_2, 'rb') as f:
    cell_dict_2 = pickle.load(f)

    
iscell_1 = np.load(iscell_1)
iscell_2 = np.load(iscell_2)

ROI_indices_1 = (iscell_1[:,0] == 1).nonzero()
ROI_indices_1 = ROI_indices_1[0] # extracting the first part of the tuple
cell_IDs_1 = ROI_indices_1 + 1 # add 1 so we don't have zero indexing

# print(cell_IDs_1[436])

ROI_indices_2 = (iscell_2[:,0] == 1).nonzero()
ROI_indices_2 = ROI_indices_2[0] # extracting the first part of the tuple
cell_IDs_2 = ROI_indices_2 + 1 # add 1 so we don't have zero indexing

# print(cell_IDs_2[255])

# Load the CSV file into a NumPy array
matched_cells_output = np.genfromtxt(BASE_PATH_2 + CELL_MATCH_FILE, delimiter=',', skip_header=0)
matched_cells_output = matched_cells_output.astype(int) -1  # Subtract 1 and convert to int (we subtract 1 here as the csv is created in MATLAB,
                                              # which doesn't have zero indexing).

# Extract the two columns
column_0 = matched_cells_output[:, 0]
column_1 = matched_cells_output[:, 1]

# Make sure the indices don’t go out of range
valid_idx_mask = (column_0 < len(cell_IDs_1)) & (column_1 < len(cell_IDs_2))

# Apply mask
column_0 = column_0[valid_idx_mask]
column_1 = column_1[valid_idx_mask]

# Map to Suite2p-style cell IDs (which are used in cell_dicts)
cell_array = np.zeros((len(column_0), 2), dtype=int)
cell_array[:, 0] = cell_IDs_1[column_0]
cell_array[:, 1] = cell_IDs_2[column_1]

# Filter matched pairs to only those where both cells are in the dictionaries
cell_array_filtered = np.array([
    [pre, post] for pre, post in cell_array
    if pre in cell_dict_1 and post in cell_dict_2
    ])

# Save the matched_cells array in the FIRST cell of each dictionary (saved inside sub_dict so that it doesn't mess up code that iterates through the dict cells)

cell_dict_1[next(iter(cell_dict_1))]['matched_cells'] = cell_array_filtered
cell_dict_2[next(iter(cell_dict_2))]['matched_cells'] = cell_array_filtered

with open(BASE_PATH+'cells.pkl','wb') as f:
        pickle.dump(cell_dict_1,f)

with open(BASE_PATH_2+'cells.pkl','wb') as f:
        pickle.dump(cell_dict_2,f)

print(CELL_MATCH_FILE + " complete")