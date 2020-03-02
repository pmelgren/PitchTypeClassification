import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import scale

all_data = pd.read_csv('./2018_trackman.csv')

pitchers = all_data.groupby('pitcher').count()
pitchers = pitchers[pitchers.p_hand >= 200]
pitchers = pitchers.sort_values('p_hand',ascending = False).index

pit = st.sidebar.selectbox('select pitcher',options = pitchers)

tm = all_data[all_data.pitcher == pit]
tm = tm.loc[:,['velocity','spin_rate','horz_break','vert_break']].dropna()

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
plt.scatter(tm.horz_break,tm.vert_break,c=tm.cluster,cmap = "Set1")
plt.title('hbreak vs vbreak')
plt.subplot(2,2,4)
plt.scatter(tm.horz_break,tm.velocity,c=tm.cluster,cmap = "Set1")
plt.title('hbreak vs velo')
plt.subplot(2,2,2)
plt.scatter(tm.horz_break,tm.spin_rate,c=tm.cluster,cmap = "Set1")
plt.title('hbreak vs spin')
plt.subplots_adjust(hspace=0.4)

st.pyplot()


st.dataframe(tm.groupby('cluster').mean())