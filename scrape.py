import pandas as pd
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import sys


class PlantScraper(object):
    def __init__(self, start, end, collected):
        self.plantDB = dict()
        self.plantList = []
        self.collected = collected
        self.pageRange = set(list(range(start, end+1))) - self.collected


    def getInfo(self, url, i):
        # Pull URL, parse with bs4
        req = requests.get(url)
        bs4_res = BeautifulSoup(req.text, 'html.parser')

        currPlant = dict()

        ### Information to Parse ###

        # Plant Index
        currPlant['id'] = i
        # Plant Name
        try:
            currPlant['name'] = bs4_res.find('div', {'class': 'left-column-layout plants-files'}).h1.text
        except:
            currPlant['name'] = None
        # URL
        currPlant['url'] = url
        # img
        try:
            currPlant['img'] = bs4_res.find('div', {'class': 'plantfiles-gallery-image'}).img['src']
        except:
            currPlant['img'] = None
        # Family, Genus, Species
        for e in bs4_res.find('div', {'class': 'plant-details'}).find_all('tr'):
            try:
                currPlant[e.find('td').text[:-1]] = e.find('a').text
            except:
                continue
        # Fillna missing
        for e in ['Family', 'Genus', 'Species']:
            if e not in currPlant:
                currPlant[e] = None
        # Hardiness
        valid_h4 = ['Hardiness:', 'Propagation Methods:', 'Water Requirements:', 'Sun Exposure:', "Where to Grow:"]
        for item in valid_h4:
            try:
                result = bs4_res.find(text=item).next
                data = []
                tag = 'p'
                while tag == 'p':
                    data.append(result.text)
                    # Iterate to next tag and check if still <p>
                    result = result.next.next
                    tag = result.name
                currPlant[item] = data
            except:
                currPlant[item] = None

        return currPlant

    def iterate(self):
        # Iterate through Page Range
        for i in tqdm(self.pageRange):
            if i in self.collected:
                continue
            # Get current URL
            url = 'https://davesgarden.com/guides/pf/go/' + str(i)
            try:
                self.plantList.append(self.getInfo(url, i))
            except:
                continue


if __name__ == '__main__':
    try:
        collected = set(list(pd.read_csv('plantDB2.csv', header=None).set_index(0).index))
    except:
        collected = set()

    print("to go: ", int(sys.argv[2]) - len(collected))

    if len(sys.argv) < 3 or int(sys.argv[2]) <= int(sys.argv[1]):
        print('Usage is: python scrape.py {start_index} {end_index}')
        print('end_index must be > start_index')
        sys.exit()

    scraper = PlantScraper(int(sys.argv[1]), int(sys.argv[2]), collected)
    scraper.iterate()

    df = pd.DataFrame(scraper.plantList).set_index('id')

    # fileName = 'plantDB_' + sys.argv[1] + '_' + sys.argv[2] + '.csv' 
    fileName = 'plantDB2.csv'
    with open(fileName, 'a') as f:
        df.to_csv(f, header=False)
