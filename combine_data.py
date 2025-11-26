'''
Functions to reorganize data for across exp analysis.
Created by Jorja Shires
'''

import pandas as pd
import os

#Global variables
# Experiment reward information: [column_index, low_reward_value, high_reward_value]
reward_info = {
    'Exp 1A': [8, 1, 3],  # Column 9 (index 8): low=1, medium=2, high=3
    'Exp 1B': [8, 1, 3],  # Column 9 (index 8): low=1, medium=2, high=3
    'Exp 2A': [4, 1, 2],  # Column 5 (index 4): low=1, high=2
    'Exp 2B': [5, 1, 3],  # Column 6 (index 5): low=1, high=3
    'Exp 2C': [5, 1, 3],  # Column 6 (index 5): low=1, high=3
    'Exp 2D': [5, 1, 2],  # Column 6 (index 5): low=1, high=2
    'Exp 2E': [5, 1, 3],  # Column 6 (index 5): low=1, high=3
    'Exp 3': [5, 1, 3]  # Column 6 (index 5): low=1, high=3
}

# Cue validity information: [column_index, valid_cue_value, neutral_cue_value]
cue_validity_info = {
    'Exp 1A': [4, 1, 0],  # Column 5 (index 4): Valid=1, Neutral=0
    'Exp 1B': [4, 1, 0],  # Column 5 (index 4): Valid=1, Neutral=0
    'Exp 2A': [4, 0, 1],  # Column 5 (index 4): Valid=0, Neutral=1
    'Exp 2B': [4, 0, 1],  # Column 5 (index 4): Valid=0, Neutral=1
    'Exp 2C': [4, 0, 1],  # Column 5 (index 4): Valid=0, Neutral=1
    'Exp 2D': [4, 0, 1],  # Column 5 (index 4): Valid=0, Neutral=1
    'Exp 2E': [4, 0, 1],  # Column 5 (index 4): Valid=0, Neutral=1
    'Exp 3': [3, 0, 1]    # Column 4 (index 3): Valid=0, Neutral=1
}

# Accuracy and reaction time column indices: [accuracy_col, reaction_time_col]
accuracy_rt_cols = {
    '1A': [1, 7],  # Column 2 (index 1): Accuracy, Column 8 (index 7): Reaction time
    '1B': [1, 7],  # Column 2 (index 1): Accuracy, Column 8 (index 7): Reaction time
    '2A': [1, 2],  # Column 2 (index 1): Accuracy, Column 3 (index 2): Reaction time
    '2B': [1, 2],  # Column 2 (index 1): Accuracy, Column 3 (index 2): Reaction time
    '2C': [1, 2],  # Column 2 (index 1): Accuracy, Column 3 (index 2): Reaction time
    '2D': [1, 2],  # Column 2 (index 1): Accuracy, Column 3 (index 2): Reaction time
    '2E': [1, 2],  # Column 2 (index 1): Accuracy, Column 3 (index 2): Reaction time
    '3': [1, 2]    # Column 2 (index 1): Accuracy, Column 3 (index 2): Reaction time
}

def open_file(folder, file_name):
    """
    Open a file and return as a pandas DataFrame.

    Parameters:
    -----------
    folder : str
        The folder/directory name where the file is located
    file_name : str
        The name of the file to open

    Returns:
    --------
    pd.DataFrame
        The file contents as a pandas DataFrame

    Usage:
    df = open_file('data_folder', 'data_file')
    """

    file_path = os.path.join(folder, file_name)
    if '1' in folder:
        #all exp 1 lack a column name
        df = pd.read_csv(file_path, header = None)
    else:
        df = pd.read_csv(file_path)
    return df


def isolate_column_by_value(df, exp_index, value_of_interest, cue_of_interest):
    """
    Isolate rows where a column has a specific value and append the filtered column to a list.

    Parameters:
    -----------
    df : pd.DataFrame
        The pandas DataFrame to filter
    exp_index : str
        The name of the exp folder to determine column and value to filter by (zero-indexed)
    value_of_interest : int
        The value to filter for (either 1 (low) or 2 (high))
    cue_of_interest : int
        The value to filer for (either 1 (valid) or 2 (neutral))
    result_list : list
        The list to append the filtered column to

    Returns:
    --------
    filtered_column : pd.DataFrame
        The dataframe filtered by reward and cue

    Usage:
    df = isolate_column_by_value(data, 9, 1, existing_list)
    """

    reward_col = reward_info[exp_index][0]
    reward = reward_info[exp_index][value_of_interest]
    cue_col = cue_validity_info[exp_index][0]
    cue = cue_validity_info[exp_index][cue_of_interest]

    # Filter rows where the column has the value of interest
    filtered_column = df[(df.iloc[:,reward_col] == reward) & (df.iloc[:,cue_col] == cue)]

    # Append to the list
    return filtered_column





