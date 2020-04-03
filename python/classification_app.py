import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as sa

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import scale

def query_data(pitcher_id):
    
    query_raw = """select velocity, spin_rate, break_x, break_z
                    from tm.pitch p inner join tm.pitch_measures pm
                    on pm.pitch_id = p.pitch_id
                    where pitcher_id = {}"""
    query_text = query_raw.format(pitcher_id)
    
    # create an SQL Alchemy engine and query the data
    conn_string = 'postgresql://postgres:Melgren1224@localhost:5432/Baseball'
    engine = sa.create_engine(conn_string)
    tm = pd.read_sql_query(query_text,engine,coerce_float = False)
            
    return(tm)

def query_pitchers():
    
    query_text = """select distinct name_first || ' ' || name_last as name
                        ,cast(pitcher_id as int) id
                    from tm.pitch pt inner join mlb.players py 
                        on py.player_id = pt.pitcher_id"""
    
    # create an SQL Alchemy engine and query the data
    conn_string = 'postgresql://postgres:Melgren1224@localhost:5432/Baseball'
    engine = sa.create_engine(conn_string)
    pl = pd.read_sql_query(query_text,engine,coerce_float = False)
            
    return(pl)    


pl = query_pitchers()

pit = st.sidebar.selectbox('select pitcher',options = pl.name)

tm = query_data(pl.loc[pl.name == pit,'id'].values[0])
tm = tm.dropna()

norm = st.sidebar.checkbox('Normalize Data',value = False)

if norm:
    eps_param = st.sidebar.slider('eps parameter',value = .5
                                  ,min_value = .05,max_value = 1.0,step = .05)
    tm['cluster'] = DBSCAN(eps = eps_param).fit_predict(scale(tm))
else:
    # determine slider params based on the mean standard deviation of the cols
    maxval = tm.std().mean()
    stepval = maxval/20
    eps_param = st.sidebar.slider('eps parameter',value = stepval*10
                                  ,min_value = stepval, max_value = maxval
                                  ,step = stepval)
        
    tm['cluster'] = DBSCAN(eps = eps_param).fit_predict(tm)

plt.subplot(2,2,1)
plt.scatter(tm.velocity,tm.spin_rate,c=tm.cluster,cmap = "Set1")
plt.title('velo vs spin')
plt.subplot(2,2,3)
plt.scatter(tm.break_x,tm.break_z,c=tm.cluster,cmap = "Set1")
plt.title('hbreak vs vbreak')
plt.subplot(2,2,4)
plt.scatter(tm.break_x,tm.velocity,c=tm.cluster,cmap = "Set1")
plt.title('hbreak vs velo')
plt.subplot(2,2,2)
plt.scatter(tm.break_x,tm.spin_rate,c=tm.cluster,cmap = "Set1")
plt.title('hbreak vs spin')
plt.subplots_adjust(hspace=0.4)

st.pyplot()


st.dataframe(tm.groupby('cluster').mean())