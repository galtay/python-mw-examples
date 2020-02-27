import bz2
import os
import mwxml
import mwtext
import mwparserfromhell


data_path = os.path.join(
    '/home',
    'galtay',
    'Data',
    'WikiconferenceNorthAmerica2019')
file_path = os.path.join(
    data_path,
    'enwiki-20190801-pages-articles-multistream.xml.bz2')
dump = mwxml.Dump.from_file(bz2.open(file_path))

forbidden_link_prefixes = ["File"]
wikitext_preprocessor = mwtext.WikitextPreprocessor(forbidden_link_prefixes)

num_pages = 0
for page in dump:
    if page.redirect:
        continue
    num_pages += 1
    print(page.title)
    rev = next(page)

    wikicode = mwparserfromhell.parse(rev.text)

    for line in wikitext_preprocessor.process(rev.text):
        print(line)
        break

    print()
    if num_pages > 2:
        break
