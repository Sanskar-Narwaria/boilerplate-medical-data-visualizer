import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = df=pd.read_csv('medical_examination.csv')
# 2
df['overweight'] = df['overweight']=np.where(df['weight']/np.square(df['height']/100)>25,1,0)

# 3
df['cholesterol']=np.where(df['cholesterol']<=1,0,1)

# 4
df['gluc']=np.where(df['gluc']<=1,0,1)

def draw_cat_plot():
    # 5
    df_cat = df[['active','alco','cholesterol','gluc','overweight','smoke','cardio']]


    # 6
    df_cat = df_cat.melt(id_vars=['cardio'],var_name='variable', value_name='value')
    

    # 7

    # 8
    fig = sns.catplot(data=df_cat, x='variable', kind='count', hue='value', col='cardio', col_wrap=2)
    fig.set_titles('cardio = {col_name}')
    fig.set_ylabels('total')
    # 9
    
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['weight'] <= df['weight'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['height']<=df['height'].quantile(0.975)) & (df['height'] >= df['height'].quantile(0.025)) & (df['ap_lo'] <= df['ap_hi'])]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots(figsize=(15,10))
    

    # 15
    fig=sns.heatmap(corr, mask=mask, ax=ax,cmap='inferno', annot=True,fmt=".1f",linewidth=1,cbar=True, cbar_kws={'location': 'right', 'ticks': [-0.08,0.00,0.08,0.16,0.24],'aspect':30});
    fig.set(xlabel="", ylabel="")
    fig.xaxis.tick_bottom()
    fig.yaxis.tick_left()
    fig.grid(False)

    # 16
    fig.savefig('heatmap.png')
    return fig
