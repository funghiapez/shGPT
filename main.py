"""
reference: https://github.com/rossning92/ai-lyrics-writing/tree/master
"""
import torch
import numpy as np
from torch.utils.data import DataLoader, Dataset, random_split

seq_len = 48
input_file_path = "data/OUTPUT_FanHua.txt"

class TxtDataSet(Dataset):
    def __init__(self, seq_len = seq_len, file = input_file_path):
        SOS = 0
        EOS = 1

        self.seq_len = seq_len
        with open(file, encoding="utf-8") as f:
            lines = f.read().splitlines()

        self.word2index = {"<SOS>": SOS, "<EOS>": EOS}

        # convert words to indices
        indices = []
        num_words = 0

        for line in lines:
            indices.append(SOS)
            for word in line:
                if word not in self.word2index:
                    self.word2index[word] = num_words
                    num_words += 1
                indices.append(self.word2index[word])
            indices.append(EOS)
    
        self.index2word = {v: k for k, v in self.word2index.items()}
        self.data = np.array(indices, dtype=np.int64)

    def __len__(self):
        return (len(self.data) - 1) // self.seq_len
    
    def __getitem__(self, index):
        start = index * self.seq_len
        end = start + self.seq_len
        return(
            torch.as_tensor(self.data[start: end]), #input
            torch.as_tensor(self.data[start + 1: end + 1]), # output
        )
        
dataSet = TxtDataSet()