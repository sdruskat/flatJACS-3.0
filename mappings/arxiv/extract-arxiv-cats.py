from bs4 import BeautifulSoup
import csv

path = './arxiv-category-taxonomy.html'

data = [['domain', 'subdomain', 'subdomain-code', 'category-code', 'category-name', 'category-description']]
soup = None

with open(path) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Domains
h2s = soup.find_all("h2", class_="accordion-head")

def process_column_div(div):
    cols = div.findChildren('div', class_='column')
    # First div should have category, second should have description
    h4n = cols[0].findNext("h4")
    h4 = h4n.find(text=True, recursive=False)
    spans = h4n.findChildren("span", recursive=False)
    assert len(spans) == 1
    for span in spans:
        spant = span.find(text=True, recursive=False)
    description = cols[1].findChildren('p', rescursive=False)[0].find(text=True, recursive = False)
    return (h4, spant, description)


for h2 in h2s:
    # Physics has an extra categorization layer
    if h2.find(text=True, recursive=False) != 'Physics':
        # Next div of class accordion-body has categorization data
        body = h2.findNext('div', class_='accordion-body')
        col_divs = body.findChildren("div" , class_='columns divided')
        for div in col_divs:
            (h4, name, description) = process_column_div(div)
            data.append([h2.find(text=True, recursive=False).strip(), None, None, h4.strip(), name[1:-1].strip(), description])
    else:  # Special case: Physics
        body = h2.findNext('div', class_='accordion-body')
        h3s = body.findChildren('h3')
        for h3 in h3s:
            h3t = h3.find(text=True, recursive=False)
            h3span = h3.findNext('span')
            h3spant = h3span.find(text=True, recursive=False)
            col_divs = body.findChildren("div" , class_='columns divided')
            for div in col_divs:
                (h4, name, description) = process_column_div(div)
                data.append([h2.find(text=True, recursive=False).strip(), h3t.strip(), h3spant[1:-1].strip(), h4.strip(), name[1:-1].strip(), description])

with open('arxiv-category-taxonomy.csv', 'w') as outf:
    writer = csv.writer(outf)
    writer.writerows(data)