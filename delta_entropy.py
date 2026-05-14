# delta_entropy.py
import pandas as pd

greece = pd.read_csv("entropy_greece.txt", sep="\t", header=None, names=["Position","Entropy"])
europe = pd.read_csv("entropy_europe.txt", sep="\t", header=None, names=["Position","Entropy"])

delta = pd.DataFrame()
delta["Position"] = greece.Position
delta["Delta"] = europe.Entropy - greece.Entropy
delta.to_csv("delta_entropy.txt", sep="\t", index=False)

