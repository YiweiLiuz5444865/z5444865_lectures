#Class_Excercise_1 in the following dataframe, replace the values col2 that are avaliable by both 2 and 3 with -1.                            import pandas as pd

import pandas as pd

df = pd.DataFrame(
    {
        'col1': range(10),
        'col2': range(10, 20)
    }
)

cond = (df['col2'] % 2 == 0) & (df['col2'] % 3 == 0)

df.loc[cond, 'col2'] = -1

print(df)

#Excercuse_2 what is the highest points per game (ppg) scored by a player from each team?

import pandas as pd

nba_stats = pd.DataFrame(
    {
        'team': ['lakers', 'lakers', 'nets', 'nets', '76ers', '76ers'],
        'players': ['lebron', 'davis', 'kyrie', 'durant', 'harden', 'embiid'],
        'ppg': [30, 20, 29, 16, 26, 28 ]
    }
)

print(nba_stats.max())

