from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import torch

def load_datasets():
    df = pd.read_pickle()
    X_train, X_test, y_train, y_test = train_test_split(df, stratify='accident', train_size=0.2)
    

    train_dataset = torch.utils.data.TensorDataset(X_train, y_train, seq_lens_train)
    val_dataset = torch.utils.data.TensorDataset(X_val, y_val, seq_lens_val)
    test_dataset = torch.utils.data.TensorDataset(X_test, y_test, seq_lens_test)

    return train_dataset, val_dataset, test_dataset