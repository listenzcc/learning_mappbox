import collections
from pprint import pprint

class MyStyles(collections.defaultdict):
    def __init__(self):
        super().__init__(dict)
        self._token = 'pk.eyJ1IjoibGlzdGVuemNjIiwiYSI6ImNrMzU5MmpxZDAxMXEzbXQ0dnd4YTZ2NDAifQ.GohcgYXFsbDqfsi_7SXdpA'
    
    # Append [value] on [name] style's [key] entry
    def append(self, name, key, value):
        self[name][key] = value

    # Append [item] dict as [name] style
    def append_all(self, name, item):
        for key in item:
            self[name][key] = item[key]

    # Report function
    def report(self):
        print(self.keys())

    # Return current names
    def get_names(self):
        return list(self.keys())

    # Parse [zoom] and [center] from [name] style's 'url' entry
    # And make legal url
    def make_url(self, name, zoom=None, center=None):
        raw_url = self[name]['url']
        raw_split = raw_url.split('#', 1) 
        url, params = raw_split[0], raw_split[1]
        params_split = params.split('/')

        output = dict(
            raw_url = raw_url,
            raw_zoom = float(params_split[0]),
            raw_center = [float(params_split[j]) for j in [1, 2]]
        )

        if not zoom:
            zoom = output['raw_zoom']

        if not center:
            center = output['raw_center']

        url += '#{}/{}/{}/0'.format(zoom, center[0], center[1])

        output['url'] = url

        return output


styles = MyStyles()

styles.append_all('Dark', dict(
    url='https://api.mapbox.com/styles/v1/listenzcc/ck35a6nwf07yt1crxsx0h4lpb.html?fresh=true&title=copy&access_token=pk.eyJ1IjoibGlzdGVuemNjIiwiYSI6ImNrMzU5MmpxZDAxMXEzbXQ0dnd4YTZ2NDAifQ.GohcgYXFsbDqfsi_7SXdpA#2.3/41.879325/62.356510/0',
    description='description',
))

styles.append_all('Light', dict(
    url='https://api.mapbox.com/styles/v1/listenzcc/ck35a72x10o361cmjfoiw1q1r.html?fresh=true&title=copy&access_token=pk.eyJ1IjoibGlzdGVuemNjIiwiYSI6ImNrMzU5MmpxZDAxMXEzbXQ0dnd4YTZ2NDAifQ.GohcgYXFsbDqfsi_7SXdpA#6.9/39.894164/117.402370/0',
    description='description',
))

styles.append_all('Streets', dict(
    url='https://api.mapbox.com/styles/v1/listenzcc/ck35ht07o15mr1cqs7gcxubff.html?fresh=true&title=copy&access_token=pk.eyJ1IjoibGlzdGVuemNjIiwiYSI6ImNrMzU5MmpxZDAxMXEzbXQ0dnd4YTZ2NDAifQ.GohcgYXFsbDqfsi_7SXdpA#9.1/39.866395/116.329033/0',
    description='description',
))

styles.append_all('Basic', dict(
    url='https://api.mapbox.com/styles/v1/listenzcc/ck3596cqk0wjf1dmqut17ow0e.html?fresh=true&title=copy&access_token=pk.eyJ1IjoibGlzdGVuemNjIiwiYSI6ImNrMzU5MmpxZDAxMXEzbXQ0dnd4YTZ2NDAifQ.GohcgYXFsbDqfsi_7SXdpA#3.1/44.401942/51.811309/0',
    description='description',
))

styles.append_all('Navigation', dict(
    url='https://api.mapbox.com/styles/v1/listenzcc/ck35a0fj00xb11co58j6p0f33.html?fresh=true&title=copy&access_token=pk.eyJ1IjoibGlzdGVuemNjIiwiYSI6ImNrMzU5MmpxZDAxMXEzbXQ0dnd4YTZ2NDAifQ.GohcgYXFsbDqfsi_7SXdpA#10.5/39.910369/116.390083/0',
    description='description',
))


if __name__ == '__main__':
    pprint(styles)
    styles.report()
