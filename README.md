# confref-ontology

The terms of confref: our own (`cr:`, `https://id.confref.org/ontology/`) and how we use the terms of other
vocabularies. The source is [`confref-ontology.md`](confref-ontology.md); [`confref-ontology.ttl`](confref-ontology.ttl)
is generated from it with `python3 generate.py` (commit both). CC0.

Rendered on [www.confref.org/ontology/](https://www.confref.org/ontology/) (a copy made by
`confref-site/deploy/sync-ontology.py`). The namespace `https://id.confref.org/ontology/` resolves to that page for
HTML and to the Turtle file for RDF; each term resolves on its own (confref-data decision 0014). Every change becomes
a version of the dataset `confref-ontology` in confref-data, loaded into the SPARQL endpoint of labs.confref.org.

Questions and proposals: [issues](https://github.com/confref/confref-ontology/issues).
