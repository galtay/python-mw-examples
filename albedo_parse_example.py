import mwtext

albedo_wikitext = """
{{Other uses}}
{{Use dmy dates|date=April 2019}}
[[File:Albedo-e hg.svg|thumb|upright=1.3|The percentage of [[diffuse reflection|diffusely reflected]] [[sunlight]] relative to various surface conditions]]

'''Albedo''' ({{IPAc-en|æ|l|ˈ|b|iː|d|oʊ}}) ({{lang-la|albedo}}, meaning 'whiteness') is the measure of the [[diffuse reflection]] of [[sunlight|solar radiation]] out of the total [[solar radiation]] received by an [[astronomical body]] (e.g. a [[planet]] like [[Earth]]). It is [[dimensionless number|dimensionless]] and measured on a scale from 0 (corresponding to a [[black body]] that absorbs all incident radiation) to 1 (corresponding to a body that reflects all incident radiation).
"""

forbidden_link_prefixes = ["File"]
wikitext_preprocessor = mwtext.WikitextPreprocessor(forbidden_link_prefixes)

for line in wikitext_preprocessor.process(albedo_wikitext):
    print(line)
    break
