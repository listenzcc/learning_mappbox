# %%
from my_styles import styles
import plotly.express as px

# %%
px.set_mapbox_access_token(styles._token)
carshare = px.data.carshare()

# %%
fig = px.scatter_mapbox(carshare, lat="centroid_lat", lon="centroid_lon",
color="peak_hour", size="car_hours",
color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
zoom=10)
fig.show()
