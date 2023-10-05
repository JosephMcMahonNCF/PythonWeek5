import pandas as pd

data = {
    "CharacterName": ["Arwen", "Frodo", "Gimli", "Legolas"],
    "Terrain": ["Forest", "Mountain", "Swamp", "Village"],
    "Stamina": [100, 100, 100, 100]  # Assuming each character starts with 100 stamina
}
df = pd.DataFrame(data)

import random

def stamina_adjustment(terrain):
    adjustments = {
        "Forest": random.randint(5, 15),     # Randomly adjust between 5 and 15 for Forest
        "Mountain": random.randint(-25, -15),  # Randomly adjust between -25 and -15 for Mountain
        "Swamp": random.randint(-35, -25),     # Randomly adjust between -35 and -25 for Swamp
        "Village": random.randint(10, 20)      # Randomly adjust between 10 and 20 for Village
    }
    return adjustments.get(terrain, 0)


df["Stamina Adjustment"] = df["Terrain"].apply(stamina_adjustment)

df["New Stamina"] = df["Stamina"] + df["Stamina Adjustment"]





print(df)
