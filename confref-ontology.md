## The confref ontology

Namespace: `https://id.confref.org/ontology/` (prefix `cr:`). This document is the source; the Turtle file
[confref-ontology.ttl](confref-ontology.ttl) is generated from its code blocks (`python3 generate.py`).

Status: draft (2026-11-08), not yet published.

### What this document describes

The **common layer** of the confref data: the classes and properties used by the identifier set `ids` (the series and
events behind the landing pages) and by our linksets, our own and those of other vocabularies. The model is described
in confref-data decision 0013.

Own terms are defined with `rdfs:label` and `rdfs:comment`. Terms of other vocabularies are described only with
`cr:label` and `cr:comment`; their definitions stay with their vocabularies. Our own terms are added only where no
term of another vocabulary fits.

The vocabularies of single sources are documented by the sources or by the vocabulary files of their datasets (dblp:
the dblp ontology; Wikidata: direct properties `wdt:`; GND: the GND Ontology; ConfIDent: the file
`confident-vocabulary.ttl.gz` of the dataset `confident`; the Springer LOD ontology: the file
`springer-lod-ontology.ttl.gz` of the dataset `springer-lod`).

### Namespaces

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix obo: <http://purl.obolibrary.org/obo/> .
@prefix cr: <https://id.confref.org/ontology/> .

<https://id.confref.org/ontology/>
    a owl:Ontology ;
    rdfs:label "confref ontology"@en ;
    dcterms:license <https://creativecommons.org/publicdomain/zero/1.0/> .
```

### Describing terms

Interfaces take the label of a term from `cr:label` (for our own terms: `rdfs:label`), so that they show our label
even when the original vocabulary is loaded as well.

#### cr:label
```
cr:label
    a owl:AnnotationProperty ;
    rdfs:label "label (confref)"@en ;
    rdfs:comment "The label confref uses for a term in its interfaces."@en ;
    rdfs:subPropertyOf rdfs:label .
```
#### cr:comment
```
cr:comment
    a owl:AnnotationProperty ;
    rdfs:label "usage note (confref)"@en ;
    rdfs:comment "How confref uses a term."@en ;
    rdfs:subPropertyOf rdfs:comment .
```

### Series and events

A series is a sequence of recurring events under one name: a conference, workshop or symposium series. An event is
one meeting: a conference, workshop or symposium, a joint or federated event (confref-data decisions 0013, 0017).

The relations are many-to-many:

- `cr:inSeries`: the series of an event. A joint conference that is branded and run as one event belongs to the
  series of each partner.
- `cr:heldAt`: the larger event an event is part of or hosted by: a workshop at its main conference, the partner
  conferences of a joint conference that presents as a collection, a conference at a federated event. The series of
  an event is independent of the series of its host.
- `cr:jointWith`, `cr:colocatedWith`: separate events held together (joint organisation or programme), or at the same
  place and time with programmes of their own. Both are symmetric.

The sources record joint conferences in each of these ways, and confref keeps the way of the source. The same joint
conference can appear as one event in two series and as two events joint with each other; the links show how they
are connected.

schema.org and AEON define a series as a kind of event. confref keeps the two levels apart, so its classes are its
own, with schema.org's as superclasses. The terms of AEON (the Academic Event Ontology,
`http://purl.obolibrary.org/obo/AEON_…`, also used by ConfIDent) are recorded as close matches.

#### cr:Series
```
cr:Series
    a owl:Class ;
    rdfs:label "series"@en ;
    rdfs:comment "A sequence of recurring academic events under one name (conference, workshop or symposium series), identified by https://id.confref.org/series/<id>."@en ;
    rdfs:subClassOf schema:EventSeries ;
    skos:closeMatch obo:AEON_0000002 .
```
#### cr:Event
```
cr:Event
    a owl:Class ;
    rdfs:label "event"@en ;
    rdfs:comment "One academic meeting (conference, workshop, symposium, joint or federated event) at one time, in one place or online, identified by https://id.confref.org/event/<id>. Not a series, not a proceedings volume."@en ;
    rdfs:subClassOf schema:Event ;
    owl:disjointWith cr:Series ;
    skos:closeMatch obo:AEON_0000001 .
```
#### cr:inSeries
```
cr:inSeries
    a owl:ObjectProperty ;
    rdfs:label "in series"@en ;
    rdfs:comment "The series an event belongs to. An event can belong to several series: a joint conference that is branded and run as one event belongs to the series of each partner."@en ;
    rdfs:domain cr:Event ;
    rdfs:range cr:Series ;
    rdfs:subPropertyOf schema:superEvent ;
    skos:closeMatch obo:AEON_0000084 .
```
#### cr:heldAt
```
cr:heldAt
    a owl:ObjectProperty ;
    rdfs:label "held at"@en ;
    rdfs:comment "The larger event an event is part of or hosted by: a workshop at its main conference, a partner conference of a joint conference that presents as a collection of conferences, a conference at a federated event. The series of an event is independent of the series of its host."@en ;
    rdfs:domain cr:Event ;
    rdfs:range cr:Event ;
    rdfs:subPropertyOf schema:superEvent ;
    skos:closeMatch obo:AEON_0000178 .
```
#### cr:jointWith
```
cr:jointWith
    a owl:ObjectProperty, owl:SymmetricProperty ;
    rdfs:label "joint with"@en ;
    rdfs:comment "Separate events that are held together, with joint organisation or a joint programme (as a source states it; a joint conference that is one event is one event in several series instead)."@en ;
    rdfs:domain cr:Event ;
    rdfs:range cr:Event ;
    skos:closeMatch obo:AEON_0000083 .
```
#### cr:colocatedWith
```
cr:colocatedWith
    a owl:ObjectProperty, owl:SymmetricProperty ;
    rdfs:label "co-located with"@en ;
    rdfs:comment "Separate events at the same place and time, each with a programme of its own."@en ;
    rdfs:domain cr:Event ;
    rdfs:range cr:Event ;
    skos:closeMatch obo:AEON_0000082 .
```
### Facts of an event

The edition number, the status, the attendance mode and the type of an event (confref-data decision 0016). The
edition number is per series: `cr:edition` when the event belongs to one series, otherwise one `cr:Edition` per
series.

    <https://id.confref.org/event/e10a0bm>
        cr:inSeries <https://id.confref.org/series/s10000y>, <https://id.confref.org/series/s1000b8> ;
        cr:hasEdition <https://id.confref.org/event/e10a0bm/edition/s10000y>,
                      <https://id.confref.org/event/e10a0bm/edition/s1000b8> .

    <https://id.confref.org/event/e10a0bm/edition/s10000y>
        a cr:Edition ;
        cr:editionOf <https://id.confref.org/series/s10000y> ;
        cr:editionNumber 29 .

#### cr:edition
```
cr:edition
    a owl:DatatypeProperty ;
    rdfs:label "edition"@en ;
    rdfs:comment "The edition number of an event in its series, when it belongs to one series. An event in several series has a cr:Edition per series instead."@en ;
    rdfs:domain cr:Event ;
    rdfs:range xsd:integer ;
    skos:closeMatch obo:AEON_0000140 .
```
#### cr:Edition
```
cr:Edition
    a owl:Class ;
    rdfs:label "edition"@en ;
    rdfs:comment "The place of an event in one of its series: the series (cr:editionOf) and the edition number (cr:editionNumber)."@en .
```
#### cr:hasEdition
```
cr:hasEdition
    a owl:ObjectProperty ;
    rdfs:label "has edition"@en ;
    rdfs:comment "An edition of an event in one of its series."@en ;
    rdfs:domain cr:Event ;
    rdfs:range cr:Edition .
```
#### cr:editionOf
```
cr:editionOf
    a owl:ObjectProperty ;
    rdfs:label "edition of"@en ;
    rdfs:comment "The series of an edition."@en ;
    rdfs:domain cr:Edition ;
    rdfs:range cr:Series .
```
#### cr:editionNumber
```
cr:editionNumber
    a owl:DatatypeProperty ;
    rdfs:label "edition number"@en ;
    rdfs:comment "The number of an edition in its series."@en ;
    rdfs:domain cr:Edition ;
    rdfs:range xsd:integer .
```
#### cr:eventType
```
cr:eventType
    a owl:ObjectProperty ;
    rdfs:label "event type"@en ;
    rdfs:comment "The type of an event, as a class of AEON: academic conference (AEON_0000103), workshop (AEON_0000121), symposium (AEON_0000113), congress (AEON_0000123), colloquium (AEON_0000101), forum (AEON_0000105), seminar (AEON_0000109), tutorial (AEON_0000119), hackathon (AEON_0000107). The types used by ConfIDent and DataCite. A series has no type of its own."@en ;
    rdfs:domain cr:Event .
```
#### schema:eventStatus
```
schema:eventStatus
    cr:label "status"@en ;
    cr:comment "Whether the event takes or took place as scheduled: schema:EventScheduled, EventPostponed, EventCancelled, EventRescheduled, EventMovedOnline. Cancelled and postponed events keep their identifiers."@en .
```
#### schema:eventAttendanceMode
```
schema:eventAttendanceMode
    cr:label "attendance mode"@en ;
    cr:comment "On site (schema:OfflineEventAttendanceMode), online (OnlineEventAttendanceMode) or hybrid (MixedEventAttendanceMode)."@en .
```

#### schema:superEvent
```
schema:superEvent
    cr:label "part of"@en ;
    cr:comment "Not used by confref directly: its subproperties cr:inSeries and cr:heldAt say which relation is meant."@en .
```
#### skos:closeMatch
```
skos:closeMatch
    cr:label "close match"@en ;
    cr:comment "On our own terms: the term of another vocabulary (AEON) that means nearly the same. The terms are not interchangeable in every application."@en .
```

### Identity and history

**Identity.** The sources state that their records are the same as others (`owl:sameAs`, identifier properties);
confref keeps these statements as given. What confref itself states to be the same series or event is `cr:sameAs`: in
the linksets and in the identifier set `ids` (a series or event of confref and the records of the sources it brings
together). `cr:sameAs` is a subproperty of `owl:sameAs`.

**History of our identifiers.** The identifiers stay stable from version to version of `ids`. When the records show
that two identifiers stand for the same series or event, one is merged into the other (`cr:mergedInto`, the older one
is kept); when one identifier stood for several, it is split (`cr:splitInto`); an identifier that no longer stands
for a series or event is retired (`cr:retiredDate`). Each change is stated once, with the date of the version that
made it. An identifier is never used again.

#### cr:sameAs
```
cr:sameAs
    a owl:ObjectProperty ;
    rdfs:label "same as (confref)"@en ;
    rdfs:comment "The same series or event, as stated by confref (linksets, identifier set). Statements of sources use owl:sameAs."@en ;
    rdfs:subPropertyOf owl:sameAs .
```
#### cr:mergedInto
```
cr:mergedInto
    a owl:ObjectProperty ;
    rdfs:label "merged into"@en ;
    rdfs:comment "The identifier that replaces this one: both stood for the same series or event; the older one is kept."@en ;
    rdfs:subPropertyOf dcterms:isReplacedBy .
```
#### cr:mergeDate
```
cr:mergeDate
    a owl:DatatypeProperty ;
    rdfs:label "merge date"@en ;
    rdfs:comment "The date of the version of the identifier set that merged this identifier."@en ;
    rdfs:range xsd:date .
```
#### cr:splitInto
```
cr:splitInto
    a owl:ObjectProperty ;
    rdfs:label "split into"@en ;
    rdfs:comment "The identifiers that replace this one: it stood for several series or events."@en .
```
#### cr:splitDate
```
cr:splitDate
    a owl:DatatypeProperty ;
    rdfs:label "split date"@en ;
    rdfs:comment "The date of the version of the identifier set that split this identifier."@en ;
    rdfs:range xsd:date .
```
#### cr:retiredDate
```
cr:retiredDate
    a owl:DatatypeProperty ;
    rdfs:label "retired date"@en ;
    rdfs:comment "The date of the version of the identifier set from which this identifier no longer stands for a series or event. It is not reused."@en ;
    rdfs:range xsd:date .
```
#### owl:sameAs
```
owl:sameAs
    cr:label "same as"@en ;
    cr:comment "As stated by a source: its record is the same as this resource. confref keeps these statements as given; its own identity statements are cr:sameAs."@en .
```

### Statistics of datasets

#### cr:currentSubjects
```
cr:currentSubjects
    a owl:DatatypeProperty ;
    rdfs:label "current subjects"@en ;
    rdfs:comment "In the metadata of a version of the identifier set: the number of identifiers that stand for a series or event (not merged, split or retired)."@en ;
    rdfs:range xsd:integer .
```

### Open

- The link between proceedings and events (decision 0013: many-to-many), and the class of proceedings.
- The facts of a series or event on its landing page (names, acronyms, dates, places, organisers) and the reused terms
  for them.
