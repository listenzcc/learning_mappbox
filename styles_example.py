# %%
import webbrowser
from my_styles import styles

for j, name in enumerate(styles.get_names()):
    print(j, name)

i = input('Select a style to browse:')
name = styles.get_names()[int(i)]
url = styles[name]['url']
print(url)

# webbrowser.open(url)

# %%
