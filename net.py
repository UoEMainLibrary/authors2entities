from api import DSpaceAPI

#import requests, pprint, json

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"


d = DSpaceAPI(HOST, PORT)

if d.options() is None: exit(1)
if d.login(USER, PASS) is None: exit(2)

for comm_name, comm_uuid in d.get_all_communities():
    print(f"\n{comm_name} - {comm_uuid}")

    for coll_name, coll_uuid in d.get_collections(comm_uuid):
        print(f"    {coll_name} - {coll_uuid}")

        d.get_items(coll_uuid)



#if (comm_uuid := d.find_community(COMMUNITY)) is None: exit(3)
#if (coll_uuid := d.find_collection(comm_uuid, COLLECTION)) is None: exit(4)


#if (person_uuid := d.create_eperson("Surname", "B")) is None: exit(5)

#d.find_eperson("B-Surname@somewhere.ac.uk")

#d.delete_community(comm_uuid)
    
#comm_uuid = d.find_community(COMMUNITY) or d.create_community()
#coll_uuid = d.find_collection(comm_uuid, COLLECTION) or d.create_collection(comm_uuid)


# RAW DATA from get_items():

"""
{
  "id" : null,
  "scope" : "b66c063b-093e-487a-a35e-3b82ce00468e",
  "query" : null,
  "appliedFilters" : null,
  "sort" : {
    "by" : "dc.date.accessioned",
    "order" : "DESC"
  },
  "configuration" : null,
  "type" : "discover",
  "_links" : {
    "self" : {
      "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e"
    }
  },
  "_embedded" : {
    "searchResult" : {
      "_embedded" : {
        "objects" : [ {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "537b2400-9bac-4d40-921b-6c92b6bda14b",
              "uuid" : "537b2400-9bac-4d40-921b-6c92b6bda14b",
              "name" : "Bio-physical models for the management of micropathogens in Scottish aquaculture: A preliminary view to farming further offshore",
              "handle" : "20.500.12594/11548",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Moriarty, M.",
                  "language" : "",
                  "authority" : "64064182-cd8d-436c-9d8a-4d9dfe5b8dd7",
                  "confidence" : 600,
                  "place" : 0
                }, {
                  "value" : "Tulett, D.",
                  "language" : "",
                  "authority" : "345dfef9-25a3-4274-9ccb-dba9aecd019f",
                  "confidence" : 600,
                  "place" : 1
                }, {
                  "value" : "Rabe, Berit",
                  "language" : "",
                  "authority" : "c42a3b34-02aa-4a7f-9976-de5b759e2d3c",
                  "confidence" : 600,
                  "place" : 2
                }, {
                  "value" : "Murray, Alexander",
                  "language" : "",
                  "authority" : "26c44ac2-defe-4303-8085-f5e63c8b430a",
                  "confidence" : 600,
                  "place" : 3
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-09-07T08:10:45Z",
                  "language" : "",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-09-07T08:10:45Z",
                  "language" : "",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2021",
                  "language" : "",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.description.abstract" : [ {
                  "value" : "Transmission of pathogens increases with population density associated with larger populations within farms and higher number of farms within an area. These pathogens can also spill over (or back) into wild populations. Owing to transmission between, and from, farms many diseases are best managed at an area level. Current area management practice in Scotland was developed 20 years ago, but as aquaculture evolves, farm size and environmental exposure will change. To assess if potential aquaculture management changes require spatial disease management changes, three scenarios for particle spread to help inform on pathogen transmission are evaluated: (1) current farm distribution; (2) medium term development (farms in exposed coastal areas); and (3) long term development (offshore farms). Climatological output from a hydrodynamic model is used to drive movements of passive particles representing infectious pathogens released from these farms. The potential distribution of particles allows assessment on possible transmission of infection, around farm locations, subject to various modelling assumptions and limitations. Dispersal distances increased with time in all scenarios. For medium term development the average dispersal distance (3.0+/-1.3 km) was marginally larger than dispersal from existing sites (2.7+/-1.6 km) after 12 hours, whereas for the longer term development this was 4.8+/-2.9 km. These results indicate that short to medium term aquaculture expansion is consistent with existing disease management areas, at least from these models. However, offshore aquaculture may result in transmission distances for pathogens that exceed existing limits, therefore will likely require re-assessment of management areas, subject to consideration of all relevant epidemiological factors.",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.citation" : [ {
                  "value" : "Moriarty, M.; Tulett, D.; Rabe, B. & Murray, A.G. 2021. Bio-physical models for the management of micropathogens in Scottish aquaculture: A preliminary view to farming further offshore. Marine Ecology Progress Series. DOI: https://doi.org/10.3354/meps13875",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "10.3354/meps13875",
                  "language" : "",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11548",
                  "language" : "",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Marine Ecology Progress Series",
                  "language" : "",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Bio-physical models for the management of micropathogens in Scottish aquaculture: A preliminary view to farming further offshore",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-09-07T08:15:40.391+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/537b2400-9bac-4d40-921b-6c92b6bda14b"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "3389847e-9ee7-40f2-8c5d-a6bdda31618c",
              "uuid" : "3389847e-9ee7-40f2-8c5d-a6bdda31618c",
              "name" : "A simple modelling tool for assessing interaction with host and local infestation of sea lice from salmonid farms on wild salmonids based on processes operating at multiple scales in space and time",
              "handle" : "20.500.12594/11285",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Murray, A.G.",
                  "language" : "en",
                  "authority" : "ca5ce47d-4576-4299-a830-6828c4635c4d",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Shephard, S.",
                  "language" : "en",
                  "authority" : "04129c50-725d-4fe9-b24d-0a3832ee4315",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Asplin, L.",
                  "language" : "en",
                  "authority" : "539fcd85-917b-41b1-bc43-10b00e92f76b",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Adams, T.",
                  "language" : "en",
                  "authority" : "22e6dad6-0cdc-4dff-94fb-f2141f58c926",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Adlandsvik, B.",
                  "language" : "en",
                  "authority" : "ff507adf-4cd9-4aca-82af-285b97bc62d0",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Gallego, A.",
                  "language" : "en",
                  "authority" : "aeeac64a-25c2-449b-b152-4c5aaaaf71b7",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Harnett, M.",
                  "language" : "en",
                  "authority" : "b84bf764-c9c7-44c6-9108-988737f541be",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Johnsen, I.A.",
                  "language" : "en",
                  "authority" : "1a2b29b0-d9cc-4a59-802d-e507973a0af4",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "Nash, S.",
                  "language" : "en",
                  "authority" : "45be1c8c-6cd6-45ef-9995-d1544398165f",
                  "confidence" : -1,
                  "place" : 8
                }, {
                  "value" : "Pert, C.",
                  "language" : "en",
                  "authority" : "c7c6fb6b-9ae2-4ee4-a20e-1392f2bc5dbb",
                  "confidence" : -1,
                  "place" : 9
                }, {
                  "value" : "Rabe, B.",
                  "language" : "en",
                  "authority" : "102d7753-c5c3-4f6a-9043-9d609237306a",
                  "confidence" : -1,
                  "place" : 10
                }, {
                  "value" : "Gargan, P.",
                  "language" : "en",
                  "authority" : "1f52306c-162b-4f48-ae40-74802e43dcca",
                  "confidence" : -1,
                  "place" : 11
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:53Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:53Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.ecolmodel.2021.109459",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11285",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Ecological Modelling",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "A simple modelling tool for assessing interaction with host and local infestation of sea lice from salmonid farms on wild salmonids based on processes operating at multiple scales in space and time",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Sea lice are marine ectoparasitic crustacea which limit the potential for sustainable salmon aquaculture due to risks of impacts on iconic wild salmon and sea trout. Control of the parasite on farms costs an estimated 9% of farm revenue. Sea lice develop through planktonic nauplii to copepodid stages which attach to, and mature on, salmonid hosts until females become ovigerous (egg laying) Impacts of lice on wild fish depend on their exposure to planktonic larval lice transported from salmon farms, which consists of (A) production of larval lice from ovigerous female lice on salmon farms, (B) local concentrations of planktonic larval lice infectious copepodids in adjacent waters, (C) rates of infestation of wild fish given these concentrations, and (D) impact on fish given this level of interaction. A model of this local exposure around salmon farms was developed. Production rates for nauplii as a function of the numbers of adult lice on salmon farms and maturation to copepodids (A) is well studied, as are impacts of infestation (D), with >0.75 lice per gram of host fish considered to present a high risk of mortality. Using existing assessments of infectious copepodid production (A) we develop a model of copepodid concentration (B) based on a simple kernel of copepodid distribution around farms; within this kernel the copepodids are assumed either to disperse evenly or to be transported in a concentrated plume, allowing comparison of the range of different concentration distributions. These distributions combine with a model of infestation (C) based on small-scale movements of copepodids in the immediate vicinity of a swimming fish. Fish swimming at intermediate velocities are most susceptible to infestation, as slow fish exhaust lice in their immediate vicinity while fast fish move on before lice copepodids can approach. These models are combined to create an assessment of the risk that concentrations can result in infestation of fish at levels considered to cause mortalities (D). The results can be used in combination with empirical assessments as a tool to link potential impacts on wild salmonids to aquaculture biomass and on-farm lice management in different environments in support of strategic aquaculture planning. Our modelling demonstrates the, often neglected, importance of fine-scale processes in sea lice infestation of salmonids.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Murray, A. G., Shephard, S., Asplin, L., Adams, T., Adlandsvik, B., Gallego, A., Harnett, M., Johnsen, I. A., Nash, S., Pert, C., Rabe, B. & Gargan, P. (2021). A simple modelling tool for assessing interaction with host and local infestation of sea lice from salmonid farms on wild salmonids based on processes operating at multiple scales in space and time. Ecological Modelling. doi:https://doi.org/10.1016/j.ecolmodel.2021.109459",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "Online first",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1161",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:00:41.840+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/3389847e-9ee7-40f2-8c5d-a6bdda31618c"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "b8208f63-cd37-4a4a-a915-96b0d9a0a2f8",
              "uuid" : "b8208f63-cd37-4a4a-a915-96b0d9a0a2f8",
              "name" : "The Critically Endangered Flapper Skate (Dipturus intermedius): Recommendations from the first Flapper Skate Working Group Meeting",
              "handle" : "20.500.12594/11284",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Garbett, A.",
                  "language" : "en",
                  "authority" : "300021db-8c05-43c1-9e32-f68c8b1bf94f",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Phillips, N.",
                  "language" : "en",
                  "authority" : "40b16289-0450-4e52-aba8-be7b7189e065",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Houghton, J.",
                  "language" : "en",
                  "authority" : "d4691a21-50a6-489d-9aa1-b370f00b7e8a",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Prodöhl, P.",
                  "language" : "en",
                  "authority" : "590105b0-d2d0-416b-9169-2c4cd6df05ed",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Thorburn, J.",
                  "language" : "en",
                  "authority" : "41e89959-6d77-4ce1-86b4-94f6f06452e4",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Loca, S.",
                  "language" : "en",
                  "authority" : "afdab785-6af8-4854-9b13-6904eeb49fe1",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Eagling, L.",
                  "language" : "en",
                  "authority" : "8a416a37-d9c3-454a-afc8-8bd7b6ae5718",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Hannon, G.",
                  "language" : "en",
                  "authority" : "b8ed0e74-2784-491d-b2cd-ed321150ef73",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "Wise, D.",
                  "language" : "en",
                  "authority" : "bcc899db-9d9f-4f7b-93aa-94cae9f1d8e1",
                  "confidence" : -1,
                  "place" : 8
                }, {
                  "value" : "Pothanikat, L.",
                  "language" : "en",
                  "authority" : "b31472b3-0e7a-4c43-ab36-0800de178fc5",
                  "confidence" : -1,
                  "place" : 9
                }, {
                  "value" : "Gordon, C.",
                  "language" : "en",
                  "authority" : "e9af862d-f285-4736-839c-65b705ab7ea8",
                  "confidence" : -1,
                  "place" : 10
                }, {
                  "value" : "Clarke, M.",
                  "language" : "en",
                  "authority" : "c5b96968-8d44-420a-b2c6-7a75edfd07ff",
                  "confidence" : -1,
                  "place" : 11
                }, {
                  "value" : "Williams, P.",
                  "language" : "en",
                  "authority" : "690b3f3a-b529-463e-8c56-13401761a7d7",
                  "confidence" : -1,
                  "place" : 12
                }, {
                  "value" : "Hunter, R.",
                  "language" : "en",
                  "authority" : "4247d2eb-7027-41a0-b892-2c54797a5d5a",
                  "confidence" : -1,
                  "place" : 13
                }, {
                  "value" : "McShane, R.",
                  "language" : "en",
                  "authority" : "6d815403-6518-41a2-bc35-a60bd220efb2",
                  "confidence" : -1,
                  "place" : 14
                }, {
                  "value" : "Brader, A.",
                  "language" : "en",
                  "authority" : "c3dd1fde-49fd-4397-88fe-dd7384e4805b",
                  "confidence" : -1,
                  "place" : 15
                }, {
                  "value" : "Dodd, J.",
                  "language" : "en",
                  "authority" : "e4f0a593-d08e-4e84-b9e9-3f2307814d96",
                  "confidence" : -1,
                  "place" : 16
                }, {
                  "value" : "McGonigle, C.",
                  "language" : "en",
                  "authority" : "3133fc68-f498-4275-8470-f65614ef20fd",
                  "confidence" : -1,
                  "place" : 17
                }, {
                  "value" : "McIlvenny, H.",
                  "language" : "en",
                  "authority" : "96869e12-2307-4ed4-9863-a940686a6413",
                  "confidence" : -1,
                  "place" : 18
                }, {
                  "value" : "Daly, O.",
                  "language" : "en",
                  "authority" : "67c7c773-c29a-4a19-ba86-fe1a6885b453",
                  "confidence" : -1,
                  "place" : 19
                }, {
                  "value" : "Surgenor, R.",
                  "language" : "en",
                  "authority" : "36bd2cce-2fb0-48b2-bf7a-7f7e44647d01",
                  "confidence" : -1,
                  "place" : 20
                }, {
                  "value" : "Varian, S.",
                  "language" : "en",
                  "authority" : "254bc593-1a7d-495f-a410-1342f466a037",
                  "confidence" : -1,
                  "place" : 21
                }, {
                  "value" : "Verhoog, P.",
                  "language" : "en",
                  "authority" : "96ce589a-1b83-49f0-874d-17cb30adc469",
                  "confidence" : -1,
                  "place" : 22
                }, {
                  "value" : "van Zonneveld, G.",
                  "language" : "en",
                  "authority" : "3124546c-e3a9-478b-9243-de2b2afc2829",
                  "confidence" : -1,
                  "place" : 23
                }, {
                  "value" : "Burke, L.",
                  "language" : "en",
                  "authority" : "cd586860-87a9-428a-84b1-25a2eba247e6",
                  "confidence" : -1,
                  "place" : 24
                }, {
                  "value" : "Davies, I.",
                  "language" : "en",
                  "authority" : "2993bff5-702a-4929-9002-78a4a3bd44c3",
                  "confidence" : -1,
                  "place" : 25
                }, {
                  "value" : "Souster, T.",
                  "language" : "en",
                  "authority" : "5135caf7-49ee-4f5d-947c-2d705fb57d84",
                  "confidence" : -1,
                  "place" : 26
                }, {
                  "value" : "Mayo, P.",
                  "language" : "en",
                  "authority" : "134911a1-c110-42eb-931b-50eef2ff91e1",
                  "confidence" : -1,
                  "place" : 27
                }, {
                  "value" : "Schwanck, T.",
                  "language" : "en",
                  "authority" : "4f769f9d-8720-4208-82b5-20237f3df6ac",
                  "confidence" : -1,
                  "place" : 28
                }, {
                  "value" : "Jones, C.",
                  "language" : "en",
                  "authority" : "1570a0a1-e241-474c-93af-f136ab5c05ab",
                  "confidence" : -1,
                  "place" : 29
                }, {
                  "value" : "Collins, P.",
                  "language" : "en",
                  "authority" : "0f87c114-215c-440a-8cbf-905865f3bab1",
                  "confidence" : -1,
                  "place" : 30
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:53Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:53Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.marpol.2020.104367",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11284",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Marine Policy",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "The Critically Endangered Flapper Skate (Dipturus intermedius): Recommendations from the first Flapper Skate Working Group Meeting",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "The flapper skate, Dipturus intermedius (Parnell, 1837), is the largest of all European skate and rays (Superorder: Batoidea). It is found in coastal waters of the European continental shelf and slopes in the North-East (NE) Atlantic. With the 2006 IUCN Red List of Threatened Species classification of ‘common skate’ as Critically Endangered, and the recognition in 2010 that this name masked two species (flapper skate and blue skate D. batis (Linnaeus, 1758)), and to better support conservation on this regional scale, the Flapper Skate Working Group (SWG) was formed. The SWG is a consortium of government, NGOs, sport-fishing associates and academics, including participants from the UK, Ireland and the Netherlands. The purpose of the SWG is to consolidate relevant research, advocacy and policy expertize for the purpose of flapper skate conservation. The first SWG workshop took place in Belfast, November 2019, with discussions focussed on conservation in the NE Atlantic. Following two days of talks, workshops and discussions, we present the SWG’s key recommendations for future collaborative conservation.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Garbett, A., Phillips, N., Houghton, J., Prodöhl, P., Thorburn, J., Loca, S., Eagling, L., Hannon, G., Wise, D., Pothanikat, L., Gordon, C., Clarke, M., Williams, P., Hunter, R., McShane, R., Brader, A., Dodd, J., McGonigle, C., McIlvenny, H., Daly, O., Surgenor, R., Varian, S., Verhoog, P., van Zonneveld, G., Burke, L., Davies, I., Souster, T., Mayo, P., Schwanck, T., Jones, C. & Collins, P. (2021). The Critically Endangered Flapper Skate (Dipturus intermedius): Recommendations from the first Flapper Skate Working Group Meeting. Marine Policy, 124, 104367. doi:https://doi.org/10.1016/j.marpol.2020.104367",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "104367",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "124",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1160",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:21.326+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/b8208f63-cd37-4a4a-a915-96b0d9a0a2f8"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "8231d483-ed96-4563-93cd-2d6f64d569ac",
              "uuid" : "8231d483-ed96-4563-93cd-2d6f64d569ac",
              "name" : "Fishing within offshore wind farms in the North Sea: Stakeholder perspectives for multi-use from Scotland and Germany",
              "handle" : "20.500.12594/11282",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Schupp, M.F.",
                  "language" : "en",
                  "authority" : "b31bc590-9807-414b-98c2-39bc46f4a535",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Kafas, A.",
                  "language" : "en",
                  "authority" : "659773b2-abd5-4614-b43a-f51f1492237c",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Buck, B.H.",
                  "language" : "en",
                  "authority" : "0fd2bd32-6f4c-4f1a-9e06-f780e33f5e84",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Krause, G.",
                  "language" : "en",
                  "authority" : "91ac5954-10b6-473c-b275-d49ca18661bb",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Onyango, V.",
                  "language" : "en",
                  "authority" : "6776590d-d64b-4eac-826e-7f3e19606f2d",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Stelzenmüller, V.",
                  "language" : "en",
                  "authority" : "48958594-62dc-43e5-b645-85e6dca89a2d",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Davies, I.M.",
                  "language" : "en",
                  "authority" : "6738b6bd-0f5d-49f3-87dd-5f9f0e46659a",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Scott, B.E.",
                  "language" : "en",
                  "authority" : "e1df0789-cbce-49bd-861a-dfaa1a1d674c",
                  "confidence" : -1,
                  "place" : 7
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:52Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:52Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.jenvman.2020.111762",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11282",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Journal of Environmental Management",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Fishing within offshore wind farms in the North Sea: Stakeholder perspectives for multi-use from Scotland and Germany",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Offshore wind power generation requires large areas of sea to accommodate its activities, with increasing claims for exclusive access. As a result, pressure is placed on other established maritime uses, such as commercial fisheries. The latter sector has often been taking a back seat in the thrust to move energy production offshore, thus leading to disagreements and conflicts among the different stakeholder groups. In recognition of the latter, there has been a growing international interest in exploring the combination of multiple maritime activities in the same area (multi-use; MU), including the re-instatement of fishing activities within, or in close proximity to, offshore wind farms (OWFs). We summarise local stakeholder perspectives from two sub-national case studies (East coast of Scotland and Germany's North Sea EEZ) to scope the feasibility of combining multiple uses of the sea, such as offshore wind farms and commercial fisheries. We combined a desk-based review with 15 semi-structured qualitative interviews with key knowledge holders from both industries, regulators, and academia to aggregate key results. Drivers, barriers and resulting effects (positive and negative) for potential multi-use of fisheries and OWFs are listed and ranked (57 factors in total). Factors are of economic, social, policy, legal, and technical nature. To date, in both case study areas, the offshore wind industry has shown little interest in multi-use solutions, unless clear added value is demonstrated and no risks to their operations are involved. In contrast, the commercial fishing sector is proactive towards multi-use projects and acts as a driving force for MU developments. We provide a range of management recommendations, based on stakeholder input, to support progress towards robust decision making in relation to multi-use solutions, including required policy and regulatory framework improvements, good practice guidance, empirical studies, capacity building of stakeholders and improvements of the consultation process. Our findings represent a comprehensive depiction of the current state and key stakeholder aspirations for multi-use solutions combining fisheries and OWFs. We believe that the pathways towards robust decision making in relation to multi-use solutions suggested here are transferable to other international locations.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Schupp, M. F., Kafas, A., Buck, B. H., Krause, G., Onyango, V., Stelzenmüller, V., Davies, I. M. & Scott, B. E. (2021). Fishing within offshore wind farms in the North Sea: Stakeholder perspectives for multi-use from Scotland and Germany. Journal of Environmental Management, 279, 111762. doi:https://doi.org/10.1016/j.jenvman.2020.111762",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "111762",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "279",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1158",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:07.348+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/8231d483-ed96-4563-93cd-2d6f64d569ac"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "ba5ce010-eb4e-4b1d-bfba-396c40325852",
              "uuid" : "ba5ce010-eb4e-4b1d-bfba-396c40325852",
              "name" : "A preliminary assessment of indirect COVID-19 impacts on aquaculture species health and welfare in Scotland",
              "handle" : "20.500.12594/11283",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Murray, A.G.",
                  "language" : "en",
                  "authority" : "ca5ce47d-4576-4299-a830-6828c4635c4d",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Ives, S.C.",
                  "language" : "en",
                  "authority" : "5cdfc6b5-46cf-46e8-83c0-71f7f950dc46",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Smith, R.J.",
                  "language" : "en",
                  "authority" : "a451024b-780a-49e5-8c3a-b83776483875",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Moriarty, M.",
                  "language" : "en",
                  "authority" : "64064182-cd8d-436c-9d8a-4d9dfe5b8dd7",
                  "confidence" : -1,
                  "place" : 3
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:52Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:52Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.vas.2021.100167",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11283",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Veterinary and Animal Science",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "A preliminary assessment of indirect COVID-19 impacts on aquaculture species health and welfare in Scotland",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "COVID-19 led to sudden changes in human activities, mainly due to restrictive measures required to supress the virus. These disruptions potentially risk animal health and welfare within production cycles. We assess the preliminary evidence for impacts on animal health and welfare in Scottish aquaculture, a key economic activity in remoter areas of the country. We summarise the industry structure, explore pathways of vulnerability to aquatic animal disease that may be accentuated by impacts of COVID-19, illustrate the temporal pattern of concern from numbers of stories in the trade press, and use basic routine data collection on the key welfare indicators of salmon mortality and parasitic sea lice counts. The indicators were published on schedule and provide no evidence of gross impact on health and welfare, at least for salmon, during the period of intensive lockdown restrictions in Scotland. Longer term effects cannot be ruled out, as mortality rates peak in autumn.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Murray, A. G., Ives, S. C., Smith, R. J. & Moriarty, M. (2021). A preliminary assessment of indirect COVID-19 impacts on aquaculture species health and welfare in Scotland Veterinary and Animal Science, 11, 100167. doi:https://doi.org/10.1016/j.vas.2021.100167",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "100167",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "11",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1159",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:21.859+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/ba5ce010-eb4e-4b1d-bfba-396c40325852"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "fb984cd6-ef31-44e8-aa45-e3e79bfc3745",
              "uuid" : "fb984cd6-ef31-44e8-aa45-e3e79bfc3745",
              "name" : "Life in a drop: Sampling environmental DNA for marine fishery management and ecosystem monitoring",
              "handle" : "20.500.12594/11281",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Gilbey, J.",
                  "language" : "en",
                  "authority" : "a5ecfd92-af40-49a8-a8d4-57303b8869a3",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Carvalho, G.",
                  "language" : "en",
                  "authority" : "f02ef09b-d1fc-4291-867c-f2bad0d924fb",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Castilho, R.",
                  "language" : "en",
                  "authority" : "16562e66-aec7-4ada-8455-e6f7ecd0480a",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Coscia, I.",
                  "language" : "en",
                  "authority" : "16f80db7-4895-4d92-ab56-554e9d38f570",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Coulson, M.W.",
                  "language" : "en",
                  "authority" : "52c5ca00-f191-4ecf-b898-5a29e887b9b2",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Dahle, G.",
                  "language" : "en",
                  "authority" : "ef85179a-f256-4bc7-b3c9-4ea5fbf361b2",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Derycke, S.",
                  "language" : "en",
                  "authority" : "5eecb7ec-b70c-4edc-ba27-74d9e350b55e",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Francisco, S.M.",
                  "language" : "en",
                  "authority" : "06d9e861-cfac-4a4f-b61d-2e690a354001",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "Helyar, S.J.",
                  "language" : "en",
                  "authority" : "97c735da-e2fb-43e1-90ff-80ff6a402742",
                  "confidence" : -1,
                  "place" : 8
                }, {
                  "value" : "Johansen, T.",
                  "language" : "en",
                  "authority" : "8b7e6e5f-9e26-4ccf-83c4-8098b2fdc2b8",
                  "confidence" : -1,
                  "place" : 9
                }, {
                  "value" : "Junge, C.",
                  "language" : "en",
                  "authority" : "da76bb3a-34e3-455a-b67c-efe12411efef",
                  "confidence" : -1,
                  "place" : 10
                }, {
                  "value" : "Layton, K.K.S.",
                  "language" : "en",
                  "authority" : "8b234bc0-9f01-46b8-b8cf-bab0448a72b2",
                  "confidence" : -1,
                  "place" : 11
                }, {
                  "value" : "Martinsohn, J.",
                  "language" : "en",
                  "authority" : "b71d3542-15ec-4996-a6ce-f94b05f0b167",
                  "confidence" : -1,
                  "place" : 12
                }, {
                  "value" : "Matejusova, I.",
                  "language" : "en",
                  "authority" : "383ce323-fe7e-470a-b5f1-c0a216e2b8d7",
                  "confidence" : -1,
                  "place" : 13
                }, {
                  "value" : "Robalo, J.I.",
                  "language" : "en",
                  "authority" : "460b2630-2dd4-46cd-85c7-e4f0ab5fb723",
                  "confidence" : -1,
                  "place" : 14
                }, {
                  "value" : "Rodríguez-Ezpeleta, N.",
                  "language" : "en",
                  "authority" : "aa56b459-76c9-41f3-be05-dfb0c7a91005",
                  "confidence" : -1,
                  "place" : 15
                }, {
                  "value" : "Silva, G.",
                  "language" : "en",
                  "authority" : "2d36e523-02c8-444b-8539-ddc6021b7cdb",
                  "confidence" : -1,
                  "place" : 16
                }, {
                  "value" : "Strammer, I.",
                  "language" : "en",
                  "authority" : "5e261598-ae1e-4f13-a81a-1e8b97de7bd2",
                  "confidence" : -1,
                  "place" : 17
                }, {
                  "value" : "Vasemägi, A.",
                  "language" : "en",
                  "authority" : "a172ca85-35e2-4b60-aa9f-1fec7c379140",
                  "confidence" : -1,
                  "place" : 18
                }, {
                  "value" : "Volckaert, F.A.M.",
                  "language" : "en",
                  "authority" : "9e979dc8-04e6-4613-9466-f78569e31727",
                  "confidence" : -1,
                  "place" : 19
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:51Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:51Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.marpol.2020.104331",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.issn" : [ {
                  "value" : "0308597X",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11281",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Marine Policy",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Life in a drop: Sampling environmental DNA for marine fishery management and ecosystem monitoring",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Science-based management of marine fisheries and effective ecosystem monitoring both require the analysis of large amounts of often complex and difficult to collect information. Legislation also increasingly requires the attainment of good environmental status, which again demands collection of data to enable efficient monitoring and management of biodiversity. Such data is traditionally obtained as a result of research surveys through the capture and/or visual identification of organisms. Recent years have seen significant advances in the utilisation of environmental DNA (eDNA) in the marine environment in order to develop alternative cost-effective ways to gather relevant data. Such approaches attempt to identify and/or quantify the species present at a location through the detection of extra-organismal DNA in the environment. These new eDNA based approaches have the potential to revolutionise data collection in the marine environment using non-invasive sampling methods and providing snapshots of biodiversity beyond the capacity of traditional sampling. Here we present a non-technical summary of different approaches in the field of eDNA, and emphasise the broad application of this approach, with value for the governance and management of marine aquatic ecosystems. The review focuses on identifying those tools which are now readily applicable and those which show promise but are currently in development and require further validations. The aim is to provide an understanding of techniques and concepts that can be used by managers without genetic or genomic expertise when consulting with specialists to perform joint evaluations of the utility of the approaches.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Gilbey, J., Carvalho, G., Castilho, R., Coscia, I., Coulson, M. W., Dahle, G., Derycke, S., Francisco, S. M., Helyar, S. J., Johansen, T., Junge, C., Layton, K. K. S., Martinsohn, J., Matejusova, I., Robalo, J. I., Rodríguez-Ezpeleta, N., Silva, G., Strammer, I., Vasemägi, A. & Volckaert, F. A. M. (2021). Life in a drop: Sampling environmental DNA for marine fishery management and ecosystem monitoring. Marine Policy, 124, 104331. doi:10.1016/j.marpol.2020.104331",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "104331",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "124",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1157",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:39.761+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/fb984cd6-ef31-44e8-aa45-e3e79bfc3745"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "6d6e1764-281e-4aae-90a7-6512e7057bff",
              "uuid" : "6d6e1764-281e-4aae-90a7-6512e7057bff",
              "name" : "Zooplankton biomass depletion event reveals the importance of small pelagic fish top-down control in the Western Mediterranean coastal waters",
              "handle" : "20.500.12594/11279",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Yebra, L.",
                  "language" : "en",
                  "authority" : "8ff234e1-9d95-415a-8495-65aded32a582",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Espejo, E.",
                  "language" : "en",
                  "authority" : "b377a28f-a7dc-417e-b2bc-9f19873d0fe1",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Putzeys, S.",
                  "language" : "en",
                  "authority" : "55dbd9e1-8508-411b-a91d-1d24fd6f0567",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Giráldez, A.",
                  "language" : "en",
                  "authority" : "afb8fb25-90ac-4316-9d0e-3e48961eb43e",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Gómez-Jakobsen, F.",
                  "language" : "en",
                  "authority" : "5a563f3b-ffff-41cf-a5c5-686ca2732394",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "León, P.",
                  "language" : "en",
                  "authority" : "204dd647-a0da-44d4-9e9f-6a7de6efdbf8",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Salles, S.",
                  "language" : "en",
                  "authority" : "82ee99eb-40fc-4eb9-8b70-897eb65befc0",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Torres, P.",
                  "language" : "en",
                  "authority" : "45c9a548-47f3-4b33-a68e-d6b4c16b81bd",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "Mercado, J.M.",
                  "language" : "en",
                  "authority" : "b4eba11d-7494-4797-9c69-bc56327365b9",
                  "confidence" : -1,
                  "place" : 8
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:50Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:50Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.3389/fmars.2020.608690",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11279",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Frontiers in Marine Science",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Zooplankton biomass depletion event reveals the importance of small pelagic fish top-down control in the Western Mediterranean coastal waters",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Journal Article",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "The influence of hydrochemistry and trophic conditions on the coastal zooplankton community’s biomass and metabolic activities was investigated along the Spanish Mediterranean coastal waters, from Algeciras Bay to Barcelona, from autumn 2011 to autumn 2012. Two hydrographic regions were differentiated: NW Alboran (ALB) and W Mediterranean (MED). Zooplankton metabolism was assessed from measurements of the electron transport system (ETS) and aminoacyl-tRNA synthetases (AARS) activities, as proxies for potential respiration and somatic growth, respectively. Zooplankton showed three to fivefold higher biomass in ALB than in MED during autumn 2011 and spring 2012. However, in autumn 2012, a drastic decrease in biomass standing stock was observed in ALB, with no significant differences between the two regions. This biomass depletion event was not associated with environmental variables, food availability or zooplankton metabolic rates, but coincided with a twofold peak of Sardina pilchardus landings in ALB. A reduced standing stock coupled with high zooplankton growth rates suggests mortality by predation as the main cause for the low zooplankton biomass typically observed in MED, and in ALB during autumn 2012.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Yebra, L., Espejo, E., Putzeys, S., Giráldez, A., Gómez-Jakobsen, F., León, P., Salles, S., Torres, P. & Mercado, J. M. (2020). Zooplankton biomass depletion event reveals the importance of small pelagic fish top-down control in the Western Mediterranean coastal waters. Frontiers in Marine Science, Online first. doi:https://doi.org/10.3389/fmars.2020.608690",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "Online first",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1155",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:01.046+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/6d6e1764-281e-4aae-90a7-6512e7057bff"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "bb7f20ea-6b29-4757-9247-759a458f313a",
              "uuid" : "bb7f20ea-6b29-4757-9247-759a458f313a",
              "name" : "Biomarker Fingerprint of Debris Flow Deposits as a Paleoproxy for IRD Sources in the Last Glacial North Atlantic",
              "handle" : "20.500.12594/11274",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Wary, M.",
                  "language" : "en",
                  "authority" : "097024e1-15e5-4205-95d0-0c7b32590938",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Kornilova, O.",
                  "language" : "en",
                  "authority" : "72e943a8-1c71-4ee5-bcd4-a9cf83d86254",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Russell, M.",
                  "language" : "en",
                  "authority" : "d149222a-1e7a-46dc-b849-8ec1b0b1162f",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Rosell-Melé, A.",
                  "language" : "en",
                  "authority" : "e69a0d3e-038e-46fb-9040-63860ebadaad",
                  "confidence" : -1,
                  "place" : 3
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:48Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:48Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1029/2020PA003850",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11274",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Paleoceanography and Paleoclimatology",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Biomarker Fingerprint of Debris Flow Deposits as a Paleoproxy for IRD Sources in the Last Glacial North Atlantic",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Investigating the spatiotemporal dynamics of iceberg discharges during the last glacial period constitutes a major challenge for paleoclimate research. In recent decades, many ice-rafted debris (IRD) provenance studies, mostly based on the comparison of the inorganic signature of IRD-rich layers and surrounding continental bedrock, have differentiated main subareas of individual ice sheets as iceberg sources and gauged their dynamic interplay. Diagnosis of specific source ice streams has nonetheless remained limited. Here we propose a new IRD provenance methodology to refine the identification of iceberg sources. It relies on the organic geochemical characterization of glacigenic debris flow (GDF) deposits to obtain the biomarker fingerprint of IRD sources. To test its potential, we analyze the composition of n-alkanes and chlorophyll-derived pigments in sediments deposited within six major North Atlantic GDF depocenters fed by ice streams draining the surrounding ice sheets. The biomarker fingerprint of GDF deposits appears to (1) be consistent with a common origin of IRD and GDF deposits through erosion of outcrops and transport by ice streams, (2) differ significantly from that of ambient hemipelagic sediments, (3) be specific and unique to each GDF depocenter, making it possible to distinguish the corresponding specific ice streams, (4) be imprinted in IRD-bearing marine sediments, and (5) have remained homogeneous enough through the last glacial to be used as a proxy for IRD sources. The biomarker fingerprint of GDF deposits thus shows strong potential to track the specific source ice streams that delivered IRD to the last glacial North Atlantic.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Wary, M., Kornilova, O., Russell, M. & Rosell-Melé, A. (2020). Biomarker Fingerprint of Debris Flow Deposits as a Paleoproxy for IRD Sources in the Last Glacial North Atlantic. Paleoceanography and Paleoclimatology, 35(4), e2020PA003850. doi:10.1029/2020PA003850",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.issue" : [ {
                  "value" : "4",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "e2020PA003850",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "35",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1150",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:22.219+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/bb7f20ea-6b29-4757-9247-759a458f313a"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "9275005b-6c2f-41f9-a28b-14900b06af6b",
              "uuid" : "9275005b-6c2f-41f9-a28b-14900b06af6b",
              "name" : "Exclusion of tidal influence on ambient sound measurements",
              "handle" : "20.500.12594/11271",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Van Geel, N.",
                  "language" : "en",
                  "authority" : "06ca69fa-5465-4fec-8015-fd5fc77cf9c1",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Merchant, N.D.",
                  "language" : "en",
                  "authority" : "6db7b226-69be-4206-bd61-af5a58183ecc",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Culloch, R.M.",
                  "language" : "en",
                  "authority" : "b753efc7-41b9-4aeb-b4dd-e428f329ff67",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Edwards, E.W.J.",
                  "language" : "en",
                  "authority" : "9709e56b-be49-47d0-9b20-fc36bd176c0f",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Davies, I.M.",
                  "language" : "en",
                  "authority" : "6738b6bd-0f5d-49f3-87dd-5f9f0e46659a",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "O'Hara Murray, R.",
                  "language" : "en",
                  "authority" : "550a9228-a9f9-4da7-ae22-5925f7b36eb3",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Brookes, K.L.",
                  "language" : "en",
                  "authority" : "2c18fe7c-28b2-4120-8e14-a79cbb24cd0f",
                  "confidence" : -1,
                  "place" : 6
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:47Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:47Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1121/10.0001704",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11271",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Journal of the Acoustical Society of America",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Exclusion of tidal influence on ambient sound measurements",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Growing concern about the impacts of anthropogenic noise on marine life has led to a global increase in the number of acoustic monitoring programmes aiming to quantify underwater soundscapes. However, low-frequency measurements in coastal sites may be affected by flow noise that is not actually present in the environment, but is caused by tidal flow turbulence around the hydrophone. At present, there is no standard way of removing this contaminating noise. This study presents an approach to exclude tidal influences (flow noise and other tidal-related acoustic self-noise) on ambient sound measurements, using data recorded at ten Scottish coastal sites between 2013 and 2017, and with a focus on the 63 and 125 Hz 1/3-octave bands. The annual ambient sound pressure levels (SPL) of the full and “tidal influence excluded” datasets of the three most tidally affected sites were compared against hypothetical noise thresholds. For the 63 Hz 1/3-octave band, results revealed: Site-specific patterns in the amount of data excluded (28.2%–89.2%), decreases in SPL (0.7–8.5 dB), and differences in the percentage of time that noise thresholds were exceeded. The described approach may serve as a standardised way of excluding tidal influence on soundscape descriptors.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Van Geel, N., Merchant, N. D., Culloch, R. M., Edwards, E. W. J., Davies, I. M., O'Hara Murray, R. & Brookes, K. L. (2020). Exclusion of tidal influence on ambient sound measurements. Journal of the Acoustical Society of America, 148(2), 701-712. doi:https://doi.org/10.1121/10.0001704",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.issue" : [ {
                  "value" : "2",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "701-712",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "148",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1147",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:12.090+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/9275005b-6c2f-41f9-a28b-14900b06af6b"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "1622a969-bd59-49f8-80b0-ee120627c703",
              "uuid" : "1622a969-bd59-49f8-80b0-ee120627c703",
              "name" : "A feeding guild indicator to assess environmental change impacts on marine ecosystem sturcture and funcioning",
              "handle" : "20.500.12594/11270",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Thompson, M.S.A.",
                  "language" : "en",
                  "authority" : "4a0fa609-6624-4807-b0f0-80dbed53e83b",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Pontalier, H.",
                  "language" : "en",
                  "authority" : "38b6e6c2-0e73-4d1c-9725-d3dc0d221b42",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Spence, M.A.",
                  "language" : "en",
                  "authority" : "1b25df3d-b4d5-4c06-9c42-c64803b4cc7f",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Pinnegar, J.K.",
                  "language" : "en",
                  "authority" : "a2d2e46d-a2d2-443d-bf1a-5e3d6bf97af0",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Greenstreet, S.",
                  "language" : "en",
                  "authority" : "cedb9e33-6180-4282-9cc6-92cfc1be7cd0",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Moriarty, M.",
                  "language" : "en",
                  "authority" : "64064182-cd8d-436c-9d8a-4d9dfe5b8dd7",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Hélaouët, P.",
                  "language" : "en",
                  "authority" : "6294db13-1579-4fe0-988d-593f7a399fc9",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Lynam, C.P.",
                  "language" : "en",
                  "authority" : "3ddc0710-c942-433f-a671-c3ed1a43a552",
                  "confidence" : -1,
                  "place" : 7
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:46Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:46Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1111/1365-2664.13662",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11270",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Journal of Applied Ecology",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "A feeding guild indicator to assess environmental change impacts on marine ecosystem sturcture and funcioning",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "(1) Integrating food web indicators into ecological status assessments is central to developing effective management measures. This is because they could reveal how an ecosystem is affected by, and responds to, environmental change that cannot be inferred from studying habitat, species or assemblages alone. However, the substantial investment required to consturct food webs from directly observed site-specific feeding interactions has hampered the development of such indicators. (2) Inventories of trophic interactions have been collated worldwide and across biomes. Information from these can be applied to infer food web structur and energy flow. Here, we compile a new marine dataset containing 8092 unique predator-prey interactions from 415,294 fish stomachs. We use this dataset to demonstrate how feeding guilds (i.e groupings based on diet and life stage) can be defined and then apply these to investigate changes in the distribution of fish biomass in the North Sea. (3) There was evidence for seven distinct feeding guilds in the tropic interaction data. Differences between guilds were related to the size of the predators which positively correlated with piscivory and habitat, with pelagic, benthic and shallow-coastal foraging apparent. (4) All seven guilds were present in the North Sea trawl data, with corresponding information for 99.7% of the biomass. Guild biomasses were largely consistent through time at the North Sea-level and spatially aggregated at the regional-level with spatiotemporal change relating to changes in resource availability, temperature, fishing, and the biomass of other guilds. This suggests that fish biomass was partitioned across broad feeding and environmental niches, and changes over time were governed partly by guild carrying capacities, but also by a combination of covariates with contrasting patterns of change between the north and south, for instance. Management of anthropogenic impacts of the North Sea ecosystem could therefore be adaptive and focused towards specific guilds and pressures in a given area. (5) Synthesis and applications: We propose a potential food web indicator that could be developed further to assess Good Environmental Status of the North East Atlantic shelf system. This approach could be readily extended to other marine ecosystems and biomes to establish its wider applicability.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Thompson, M. S. A., Pontalier, H., Spence, M. A., Pinnegar, J. K., Greenstreet, S., Moriarty, M., Hélaouët, P. & Lynam, C. P. (2020). A feeding guild indicator to assess environmental change impacts on marine ecosystem sturcture and funcioning. Journal of Applied Ecology, 57(9): 1769-1781.",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.issue" : [ {
                  "value" : "9",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "1769-1781",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "57",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1146",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:00:28.361+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/1622a969-bd59-49f8-80b0-ee120627c703"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "a5eae208-b754-40e9-9767-4a91c5e3a7a3",
              "uuid" : "a5eae208-b754-40e9-9767-4a91c5e3a7a3",
              "name" : "Integrating stakeholder knowledge through modular cooperative participatory processes for marine spatial planning outcomes (CORPORATES)",
              "handle" : "20.500.12594/11267",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Slater, A.-M.",
                  "language" : "en",
                  "authority" : "3c5d0d56-6a83-4de6-accd-42b47fc14bec",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Irvine, K.N.",
                  "language" : "en",
                  "authority" : "309b28e5-75a4-49e6-b319-59aa99fcfd45",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Byg, A.A.",
                  "language" : "en",
                  "authority" : "04feec66-7bc4-4aa1-b8cd-ee286bf02ee1",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Davies, I.M.",
                  "language" : "en",
                  "authority" : "6738b6bd-0f5d-49f3-87dd-5f9f0e46659a",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Gubbins, M.",
                  "language" : "en",
                  "authority" : "32409edf-5805-4afb-8d9a-e467bdb2c395",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Kafas, A.",
                  "language" : "en",
                  "authority" : "659773b2-abd5-4614-b43a-f51f1492237c",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Kenter, J.",
                  "language" : "en",
                  "authority" : "a0375216-899e-4725-9524-b5ae36d6433f",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "MacDonald, A.",
                  "language" : "en",
                  "authority" : "c575431d-edba-47c1-b940-8b3f8f7a2340",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "O'Hara Murray, R.",
                  "language" : "en",
                  "authority" : "550a9228-a9f9-4da7-ae22-5925f7b36eb3",
                  "confidence" : -1,
                  "place" : 8
                }, {
                  "value" : "Potts, T.",
                  "language" : "en",
                  "authority" : "ed5a2e74-a11a-4c35-bbe6-94fd66d0e13d",
                  "confidence" : -1,
                  "place" : 9
                }, {
                  "value" : "Tweddle, J.F.",
                  "language" : "en",
                  "authority" : "e65abbff-c1a8-4717-aca0-8ba42cc7192f",
                  "confidence" : -1,
                  "place" : 10
                }, {
                  "value" : "Wright, K.",
                  "language" : "en",
                  "authority" : "14ef908a-8b6e-434c-8193-11cb868c8229",
                  "confidence" : -1,
                  "place" : 11
                }, {
                  "value" : "Scott, B.E.",
                  "language" : "en",
                  "authority" : "e1df0789-cbce-49bd-861a-dfaa1a1d674c",
                  "confidence" : -1,
                  "place" : 12
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:45Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:45Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.ecoser.2020.101126",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.issn" : [ {
                  "value" : "2212-0416",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "http://www.sciencedirect.com/science/article/pii/S2212041620300681",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "https://hdl.handle.net/20.500.12594/11267",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 1
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Ecosystem Services",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Integrating stakeholder knowledge through modular cooperative participatory processes for marine spatial planning outcomes (CORPORATES)",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Management of the sea is increasingly complex, riddled with uncertainty and necessitates involvement from researchers across disciplines and stakeholders from multiple policy and practice sectors. This article discusses “The Cooperative Participatory Evaluation of Renewable Technologies on Ecosystem Services” (CORPORATES) research project, which developed an innovative and practical method of linking ecological processes, ecosystem services and benefits. The research was conducted in the context of licensing decisions for offshore wind farms in the North Sea (Scotland, UK). A set of linked, modular participatory processes were developed to foster cross-sector stakeholder engagement. It employed an exchange of ecological, legal, social, economic and cultural knowledge around marine ecosystem services. Workshop exercises included participatory mapping, benefit identification, and developing an understanding of linkages between ecosystem services, benefits, stakeholders’ activities and policy drivers through co-development of conceptual systems maps of the study area. The participatory exercises fostered meaningful dialogue across sectors and an ability to participate equally, despite initial differences in knowledge about ecosystem services. The development of conceptual systems maps facilitated productive discussion about trade-offs in relation to different policies. Reflective discussion identifies ways in which the developed processes could be integrated into future decision making. An assessment of the approach revealed that it operationalised a post normal science framework in terms of process oversight, multiple knowledge claims, and managing uncertainty. It developed a process that linked understanding of ecosystem functioning with the creation and implementation of policy thereby creating an ecosystem approach to marine spatial planning and licensing decisions, as required by law. This approach has extensive transferability to situations where stakeholder engagement is required to develop policy and provide feedback as part of a decision-making process. It is an engagement, outreach tool for communities and can help teach methods and processes for stakeholder engagement which enable new insights.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Slater, A.-M., Irvine, K. N., Byg, A. A., Davies, I. M., Gubbins, M., Kafas, A., Kenter, J., MacDonald, A., O'Hara Murray, R., Potts, T., Tweddle, J. F., Wright, K. & Scott, B. E. (2020). Integrating stakeholder knowledge through modular cooperative participatory processes for marine spatial planning outcomes (CORPORATES). Ecosystem Services, 44, 101126. doi:https://doi.org/10.1016/j.ecoser.2020.101126",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "101126",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "44",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1143",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:16.893+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/a5eae208-b754-40e9-9767-4a91c5e3a7a3"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "79b7290d-6291-4215-b1ef-c55dce296498",
              "uuid" : "79b7290d-6291-4215-b1ef-c55dce296498",
              "name" : "Different bottom trawl fisheries have a differential impact on the status of the North Sea seafloor habitats",
              "handle" : "20.500.12594/11266",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Rijnsdorp, A.D.",
                  "language" : "en",
                  "authority" : "c66e5f95-1fb8-4099-bde3-e9a72fb2c465",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Hiddink, J.G.",
                  "language" : "en",
                  "authority" : "ca2d17c1-0e9d-49d7-b291-1bc1b65b0173",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "van Denderen, P.D.",
                  "language" : "en",
                  "authority" : "29ee8863-06d9-40be-8953-c05403e03c79",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Hintzen, N.T.",
                  "language" : "en",
                  "authority" : "470c1845-f506-4813-a606-df5366ec7ec3",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Eigaard, O.R.",
                  "language" : "en",
                  "authority" : "521b2bf0-15cf-496a-8e99-f85914167f4c",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Valanko, S.",
                  "language" : "en",
                  "authority" : "840d3044-07ae-4317-a122-d3fa6d78b600",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Bastardie, F.",
                  "language" : "en",
                  "authority" : "0cfc2fc4-d347-4fa9-9c06-4e61e6b6f81a",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Bolam, S.G.",
                  "language" : "en",
                  "authority" : "7dce0234-b39d-44a6-99c3-eccff4b65465",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "Boulcott, P.",
                  "language" : "en",
                  "authority" : "e1c1a57b-1f98-42ff-9982-fd157bcccd56",
                  "confidence" : -1,
                  "place" : 8
                }, {
                  "value" : "Egekvist, J.",
                  "language" : "en",
                  "authority" : "7b00811a-55b2-4deb-ab7e-8c4928107351",
                  "confidence" : -1,
                  "place" : 9
                }, {
                  "value" : "Garcia, C.",
                  "language" : "en",
                  "authority" : "9eb46756-56ac-497d-a4a5-f9ccf03a091a",
                  "confidence" : -1,
                  "place" : 10
                }, {
                  "value" : "van Hoey, G.",
                  "language" : "en",
                  "authority" : "2ed137e3-49cd-43d9-9860-7066e4882a1c",
                  "confidence" : -1,
                  "place" : 11
                }, {
                  "value" : "Jonsson, P.",
                  "language" : "en",
                  "authority" : "e37987b3-b1af-44d4-992e-a30fa5613f26",
                  "confidence" : -1,
                  "place" : 12
                }, {
                  "value" : "Laffargue, P.",
                  "language" : "en",
                  "authority" : "4b78ab4a-6dfd-4964-a7e8-361564d38838",
                  "confidence" : -1,
                  "place" : 13
                }, {
                  "value" : "Nielsen, J.R.",
                  "language" : "en",
                  "authority" : "3bf5dbc2-4aab-4da5-b02c-ca6e4d83a81f",
                  "confidence" : -1,
                  "place" : 14
                }, {
                  "value" : "Piet, G.J.",
                  "language" : "en",
                  "authority" : "d6d70a37-1905-42b2-a528-41194fe47c83",
                  "confidence" : -1,
                  "place" : 15
                }, {
                  "value" : "Sköld, M.",
                  "language" : "en",
                  "authority" : "fa1ceeef-03f9-40fc-98e6-46aa4a959133",
                  "confidence" : -1,
                  "place" : 16
                }, {
                  "value" : "van Kooten, T.",
                  "language" : "en",
                  "authority" : "9d6d8690-3936-4fce-ab36-b8bb7a84819c",
                  "confidence" : -1,
                  "place" : 17
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:45Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:45Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1093/icesjms/fsaa050.",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11266",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "ICES Journal of Marine Science",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Different bottom trawl fisheries have a differential impact on the status of the North Sea seafloor habitats",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Fisheries using bottom trawls are the most widespread source of anthropogenic physical disturbance to seafloor habitats. To mitigate such disturbances, the development of fisheries-, conservation-, and ecosystem-based management strategies requires the assessment of the impact of bottom trawling on the state of benthic biota. We explore a quantitative and mechanistic framework to assess trawling impact. Pressure and impact indicators that provide a continuous pressure–response curve are estimated at a spatial resolution of 1 × 1 min latitude and longitude (∼2 km2) using three methods: L1 estimates the proportion of the community with a life span exceeding the time interval between trawling events; L2 estimates the decrease in median longevity in response to trawling; and population dynamic (PD) estimates the decrease in biomass in response to trawling and the recovery time. Although impact scores are correlated, PD has the best performance over a broad range of trawling intensities. Using the framework in a trawling impact assessment of ten métiers in the North Sea shows that muddy habitats are impacted the most and coarse habitats are impacted the least. Otter trawling for crustaceans has the highest impact, followed by otter trawling for demersal fish and beam trawling for flatfish and flyshooting. Beam trawling for brown shrimps, otter trawling for industrial fish, and dredging for molluscs have the lowest impact. Trawling is highly aggregated in core fishing grounds where the status of the seafloor is low but the catch per unit of effort (CPUE) per unit of impact is high, in contrast to peripheral grounds, where CPUE per unit of impact is low.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Rijnsdorp, A. D., Hiddink, J. G., van Denderen, P. D., Hintzen, N. T., Eigaard, O. R., Valanko, S., Bastardie, F., Bolam, S. G., Boulcott, P., Egekvist, J., Garcia, C., van Hoey, G., Jonsson, P., Laffargue, P., Nielsen, J. R., Piet, G. J., Sköld, M. & van Kooten, T. (2020). Different bottom trawl fisheries have a differential impact on the status of the North Sea seafloor habitats. ICES Journal of Marine Science, Online first. doi:https://doi.org/10.1093/icesjms/fsaa050.",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.issue" : [ {
                  "value" : "5",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "1772–1786",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "77",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1142",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:04.916+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/79b7290d-6291-4215-b1ef-c55dce296498"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "7bb139b8-dd0a-4f93-a133-a86e28a77de3",
              "uuid" : "7bb139b8-dd0a-4f93-a133-a86e28a77de3",
              "name" : "Near equal compressibility of liver oil and seawater minimises buoyancy changes in deep-sea sharks and chimaeras",
              "handle" : "20.500.12594/11264",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Priede, I.G.",
                  "language" : "en",
                  "authority" : "175b454c-5467-469d-b197-e79ce8b40a38",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Burgass, R.G.",
                  "language" : "en",
                  "authority" : "5db9ac9b-b386-4033-b549-ee8fb1c74849",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Mandalakis, M.",
                  "language" : "en",
                  "authority" : "e2bf0561-802d-4f36-8a1e-93bb9f83c225",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Spyros, A.",
                  "language" : "en",
                  "authority" : "02352cc4-6e26-4258-a28d-b132e340cd16",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Gikas, P.",
                  "language" : "en",
                  "authority" : "f0a29cf8-f8e9-43a2-afb8-8d4d53f15449",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Burns, F.",
                  "language" : "en",
                  "authority" : "196e1315-7231-4946-9fa1-24c0ac1bf97d",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Drewery, J.",
                  "language" : "en",
                  "authority" : "74ddb4e1-eb61-406f-8ac4-0e7d84e3510c",
                  "confidence" : -1,
                  "place" : 6
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:44Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:44Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1242/jeb.222943",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11264",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Journal of Experimental Biology",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Near equal compressibility of liver oil and seawater minimises buoyancy changes in deep-sea sharks and chimaeras",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Whereas upper ocean pelagic sharks are negatively buoyant and must swim continuously to generate lift from their fins, deep-sea sharks float or swim slowly buoyed up by large volumes of low-density oils in their livers. Investigation of the pressure, volume, temperature (PVT) relationships for liver oils of 10 species of deep-sea Chondrichthyes shows that the density difference between oil and seawater, Δρ, remains almost constant with pressure down to full ocean depth (11 km, 1100 bar), theoretically providing buoyancy far beyond the maximum depth of occurrence (3700 m) of sharks. However, Δρ does change significantly with temperature and we show that the combined effects of pressure and temperature can decrease buoyancy of oil by up to 10% between the surface and 3500 m depth across interfaces between warm southern and cold polar waters in the Rockall Trough in the NE Atlantic. This increases drag more than 10-fold compared with neutral buoyancy during horizontal slow swimming (0.1 m s−1), but the effect becomes negligible at high speeds. Chondrichthyes generally experience positive buoyancy change during ascent and negative buoyancy change during descent, but contrary effects can occur at interfaces between waters of different densities. During normal vertical migrations buoyancy changes are small, increasing slow-speed drag no more than 2- to 3-fold. Equations and tables of density, pressure and temperature are provided for squalene and liver oils of Chimaeriformes (Harriotta raleighana, Chimaera monstrosa, Hydrolagus affinis), Squaliformes (Centrophorus squamosus, Deania calcea, Centroscymnus coelolepis, Centroscyllium fabricii, Etmopterus spinax) and Carcharhiniformes (Apristurus laurussonii, Galeus murinus).",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Priede, I. G., Burgass, R. G., Mandalakis, M., Spyros, A., Gikas, P., Burns, F. & Drewery, J. (2020). Near equal compressibility of liver oil and seawater minimises buoyancy changes in deep-sea sharks and chimaeras Journal of Experimental Biology, 223. doi:https://doi.org/10.1242/jeb.222943",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "223",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1140",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:05.358+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/7bb139b8-dd0a-4f93-a133-a86e28a77de3"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "832545e9-b153-4adc-9d81-4e3e3ea2f99b",
              "uuid" : "832545e9-b153-4adc-9d81-4e3e3ea2f99b",
              "name" : "Size-at-maturity of Brown Crab, Cancer pagurus, in Scottish waters based on gonadal and morphometric traits",
              "handle" : "20.500.12594/11262",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Mesquita, C.",
                  "language" : "en",
                  "authority" : "36a95211-67cc-4aa6-a7a6-c275b4b954b4",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Dobby, H.",
                  "language" : "en",
                  "authority" : "103144b7-1af6-41b0-a3ac-64038a97897a",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Sweeting, S.",
                  "language" : "en",
                  "authority" : "e09147b5-52de-488c-84ae-26187fb05c25",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Jones, C.S.",
                  "language" : "en",
                  "authority" : "a233b24e-b9ce-4f74-8d53-a1f5d34fb480",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Pierce, G.J.",
                  "language" : "en",
                  "authority" : "e0867e0d-983c-4185-9e77-263663488c66",
                  "confidence" : -1,
                  "place" : 4
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:43Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:43Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.fishres.2020.105610",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11262",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Fisheries Research",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Size-at-maturity of Brown Crab, Cancer pagurus, in Scottish waters based on gonadal and morphometric traits",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Minimum landing sizes (MLS) are commonly used to manage crustaceans and are generally set above the size at first maturity to ensure that some protection is afforded to exploited stocks. Despite the economic importance of the brown crab fishery in Scotland, the species is considered data-poor and only limited information is available on size-at-maturity. This study provides, for the first time, estimates of the size-at-maturity of brown crab on the east and west coasts of Scotland using gonadal and morphometric criteria. Gonadal maturity was determined from female ovary and male testes, which were classified macroscopically into development stages and their relationship with body size modelled using a logistic regression. Body morphometric maturity was studied by analysing morphometric changes in growth in the male chelae and female abdomens using generalized additive models and regression models to estimate the size at which changes in allometric relationships occur. Estimates of size-at-maturity using gonad development were 101-106 mm carapace width (CW) for males and 127-128 mm for females. Size-at-maturity based on the morphometric characters were 120-148 mm CW for males and 131-142 mm for females. Results show that brown crab maturity is likely to occur at lower sizes than the current MLS in Scotland, implying that crabs may be able to reproduce at least once before being harvested. Regional variations in local populations should be considered when setting a MLS and this study suggests that the current MLS of 150 mm is appropriate for both areas considered.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Mesquita, C., Dobby, H., Sweeting, S., Jones, C. S. & Pierce, G. J. (2020). Size-at-maturity of Brown Crab, Cancer pagurus, in Scottish waters based on gonadal and morphometric traits. Fisheries Research, 229, 105610. doi:https://doi.org/10.1016/j.fishres.2020.105610",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "105610",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "229",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1138",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:07.594+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/832545e9-b153-4adc-9d81-4e3e3ea2f99b"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "775d82d8-f661-4248-9b9b-8905a3474399",
              "uuid" : "775d82d8-f661-4248-9b9b-8905a3474399",
              "name" : "Multi-residue enantioselective determination of emerging drug contaminants in seawater by solid phase extraction and liquid chromatographytandem mass spectrometry",
              "handle" : "20.500.12594/11261",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "McKenzie, K.",
                  "language" : "en",
                  "authority" : "460bb779-b0e6-44f6-92a0-e0f57b49b14f",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Moffat, C.F.",
                  "language" : "en",
                  "authority" : "a6ca8ae3-0183-45c4-8205-9ac33407c64b",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Petrie, B.",
                  "language" : "en",
                  "authority" : "a61abb8e-7066-41ac-9851-bc1bc6dfd604",
                  "confidence" : -1,
                  "place" : 2
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:43Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:43Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1039/d0ay00801j",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11261",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Analytical Methods",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Multi-residue enantioselective determination of emerging drug contaminants in seawater by solid phase extraction and liquid chromatographytandem mass spectrometry",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "This study proposes a new multi-residue enantioselective method for the determination of emerging drug contaminants in sea water by solid phase extraction (SPE) and liquid chromatography-tandem mass spectrometry (LC-MS/MS). To achieve satisfactory enantiomeric separation with a vancomycin stationary phase it was essential to limit sodium chloride in extracted samples to <1 μg per injection. This was achieved through a straightforward SPE method using a 50 mL water wash volume and analyte elution in acetonitrile. A Chiral-V enantioselective column (150 × 2.1 mm; 2.7 μm particle size) operated in polar ionic mode enabled simultaneous drug separations in 30 minutes. Analytes with enantioresolution ≥1 were the stimulants amphetamine and methamphetamine, the beta-agonist salbutamol, the beta-blockers propranolol, sotalol and acebutolol, the anti-depressants fluoxetine, venlafaxine, desmethylvenlafaxine and citalopram, and the antihistamine chlorpheniramine. Method quantitation limits were <10 ng L−1 and method trueness was 80–110% for most analytes. The method was applied to samples from the Forth and Clyde estuaries, Scotland. Chiral drugs were present at concentrations in the range 4–159 ng L−1 and several were in non-racemic form (enantiomeric fraction ≠ 0.50) demonstrating enantiomer enrichment. This emphasises the need for further enantiospecific drug exposure and effect studies in the marine environment.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "McKenzie, K., Moffat, C. F. & Petrie, B. (2020). Multi-residue enantioselective determination of emerging drug contaminants in seawater by solid phase extraction and liquid chromatographytandem mass spectrometry. Analytical Methods, 12, 2881-2892. doi:10.1039/d0ay00801j",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "2881-2892",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "12",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1137",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:03.942+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/775d82d8-f661-4248-9b9b-8905a3474399"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "bf27ff2c-df12-41c4-b87b-83bd29405b48",
              "uuid" : "bf27ff2c-df12-41c4-b87b-83bd29405b48",
              "name" : "Missing the full story: First estimates of carbon deposition rates for the European flat oyster, Ostrea edulis",
              "handle" : "20.500.12594/11257",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Lee, H.Z.L.",
                  "language" : "en",
                  "authority" : "14423b69-5b92-4adf-bdd1-ff649f00ca66",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Davies, I.",
                  "language" : "en",
                  "authority" : "2993bff5-702a-4929-9002-78a4a3bd44c3",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Baxter, J.",
                  "language" : "en",
                  "authority" : "8fc01382-9243-47cc-912e-9749074addb1",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Diele, K.",
                  "language" : "en",
                  "authority" : "b1246d7a-367a-4ea8-aa41-686a9bb188bc",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Sanderson, W.G.",
                  "language" : "en",
                  "authority" : "4779ff78-5f57-4de9-ba1b-3d597ae187c1",
                  "confidence" : -1,
                  "place" : 4
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:41Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:41Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1002/aqc.3402",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11257",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Aquatic Conservation: Marine and Freshwater Ecosystems",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Missing the full story: First estimates of carbon deposition rates for the European flat oyster, Ostrea edulis",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Globally, momentum to restore damaged habitats has been increasing. For example, the number of European shellfish restoration projects has quadrupled in the past 3 years. In line with the increasing focus on both restoration and climate change mitigation efforts, this study highlights how these two practices can complement each other. This experimental study quantifies the active and passive sediment deposition associated with the European flat oyster (Ostrea edulis) and the organic and inorganic carbon fractions of the deposits. Treatments included ‘dead’, ‘live’, and control to account for (i) passive deposition, (ii) biodeposition and passive deposition, and (iii) background deposition respectively. By utilizing these data, the expected carbon deposition associated with a restored flat oyster bed was investigated. The experiment was conducted ex situ, with natural seawater input. Covariate data on temperature, suspended particulate influx, salinity, and oxygen availability were recorded. Enhanced sedimentation (2.9 times) and organic carbon deposition (three times) were observed in the presence of living oysters, compared with the control. The shell structure of the oysters had no influence on passive sedimentation in this study. By developing a full understanding of the ecosystem services (functioning, supporting, regulating, and cultural) provided by a habitat, it becomes possible to quantify overall ecosystem function. This evidence is key in advising policymakers, restoration funders, and marine spatial planners on the connection between keystone species restoration, ecosystem service restoration, and conservation management. The enhancement of benthopelagic coupling by the European flat oyster, evidenced here for the first time, is contextualized from the perspective of quantification of ecosystem service provision for both restoration practices and blue carbon store management. The data produced in this study are discussed comparatively with work that has focused on other species from both Europe and the USA.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Lee, H. Z. L., Davies, I., Baxter, J., Diele, K. & Sanderson, W. G. (2020). Missing the full story: First estimates of carbon deposition rates for the European flat oyster, Ostrea edulis. Aquatic Conservation: Marine and Freshwater Ecosystems, 30(11), 2076-2086. doi:10.1002/aqc.3402",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.issue" : [ {
                  "value" : "11",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "2076-2086",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "30",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1133",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:23.389+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/bf27ff2c-df12-41c4-b87b-83bd29405b48"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "20b1e0b6-a197-4a09-aed1-21c01268a131",
              "uuid" : "20b1e0b6-a197-4a09-aed1-21c01268a131",
              "name" : "Are MPAs effective in removing fishing pressure from benthic species and habitats?",
              "handle" : "20.500.12594/11255",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Langton, R.",
                  "language" : "en",
                  "authority" : "626ab9e7-5b20-42ce-b1e1-43436cd73fb8",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Stirling, D.A.",
                  "language" : "en",
                  "authority" : "33448bb2-e659-46e8-9e28-367b67023136",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Boulcott, P.",
                  "language" : "en",
                  "authority" : "e1c1a57b-1f98-42ff-9982-fd157bcccd56",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Wright, P.J.",
                  "language" : "en",
                  "authority" : "4f5435d2-040f-404f-8ac4-2d25138b20f6",
                  "confidence" : -1,
                  "place" : 3
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:40Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:40Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.biocon.2020.108511",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11255",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Biological Conservation",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Are MPAs effective in removing fishing pressure from benthic species and habitats?",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "MPAs are expected to effect a demonstrable improvement to the conservation status of rare and important habitats and species. However, the reduction in anthopogenic pressure due to such management measures is rarely estimated. Although MPA networks may cover a large proportion of the seabed, designated areas that prohibit damaging fishing activity are in many instances much smaller. This case study compares fishing pressure inside and outside areas covered by Scottish MPAs and MPA management measures, further relating its distirbution to a metric of habitat topography; bottom ruggedness. Whilst 7% of the study region was found to be within MPA boundaries, only 2.5% of the region was subject to managment measures that restric benthic mobile fishing. Taking historical levels of fishing as a benchmark, management measues have been applied to less than 0.6% of the swept area of existing fishing activity in areas of high average seabed ruggedness. These finsings suggest that protection has been focussed in areas that already act as natural refugia for sensitive benthic species and lie away from the majority of fishing activity. While the measures do not reduce fishing pressure markedly, they do protect relatively pristing habitats from future impact. Nevertheless, management that targets pristing habitats may have unintended consequences, as it focuses protection towards areas with highger ruggedness, leaving areas of low ruggedness and associated species of ecological importance underrepresented.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Langton, R., Stirling, D. A., Boulcott, P. & Wright, P. J. (2020). Are MPAs effective in removing fishing pressure? Biological Conservation (Vol. 247, pp. 108511).",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "108511",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "247",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1131",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:00:33.327+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/20b1e0b6-a197-4a09-aed1-21c01268a131"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "d6f46a6c-bc49-4a50-8663-69e8193e2094",
              "uuid" : "d6f46a6c-bc49-4a50-8663-69e8193e2094",
              "name" : "Integration of transcriptome, gross morphology and histopathology in the gill of sea farmed Atlantic salmon (Salmo salar): lessons from multi-site sampling",
              "handle" : "20.500.12594/11254",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Krol, E.",
                  "language" : "en",
                  "authority" : "2e1aeb4c-061b-4131-8d8b-2cb10f71d196",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Noguera, P.",
                  "language" : "en",
                  "authority" : "14460d2b-3d1c-48d8-adcc-6ec87c1bb723",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Shaw, S.",
                  "language" : "en",
                  "authority" : "deba7145-1f51-435f-afb8-5a28238380ef",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Costelloe, E.",
                  "language" : "en",
                  "authority" : "91fef5cf-1c2c-47e8-bc12-1961ae6e6f70",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Gajardo, K.",
                  "language" : "en",
                  "authority" : "eee19f68-3b75-4220-bc9e-e46d26b9c758",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Valdenegro, V.",
                  "language" : "en",
                  "authority" : "78c35d23-49ab-4ed2-a36f-ac4569d7dc7b",
                  "confidence" : -1,
                  "place" : 5
                }, {
                  "value" : "Bickerdike, R.",
                  "language" : "en",
                  "authority" : "efd3e70a-bb86-4f88-99cf-9212423fd57e",
                  "confidence" : -1,
                  "place" : 6
                }, {
                  "value" : "Douglas, A.",
                  "language" : "en",
                  "authority" : "e378d3bf-fb59-4b67-8098-3dc54fcd7bac",
                  "confidence" : -1,
                  "place" : 7
                }, {
                  "value" : "Martin, S.A.M.",
                  "language" : "en",
                  "authority" : "6dfc6c6f-f0c6-4008-9107-d249dd013ee9",
                  "confidence" : -1,
                  "place" : 8
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:40Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:40Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.3389/fgene.2020.00610",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11254",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Frontiers in Genetics",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Integration of transcriptome, gross morphology and histopathology in the gill of sea farmed Atlantic salmon (Salmo salar): lessons from multi-site sampling",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "The gill of teleost fish is a multifunctional organ involved in many physiological processes such as gas exchange, osmotic and ionic regulation, acid-base balance and excretion of nitrogenous waste. Due to its extensive interface with the environment, the gill plays a key role as a primary mucosal defense tissue against pathogens, as manifested by the presence of the gill-associated lymphoid tissue (GIALT). In recent years, the prevalence of multifactorial gill pathologies has increased significantly, causing substantial losses in Atlantic salmon aquaculture. The transition from healthy to unhealthy gill phenotypes and the progression of multifactorial gill pathologies, such as proliferative gill disease (PGD), proliferative gill inflammation (PGI) and complex gill disorder (CGD), are commonly characterized by epithelial hyperplasia, lamellar fusion and inflammation. Routine monitoring for PGD relies on visual inspection and non-invasive scoring of the gill tissue (gross morphology), coupled with histopathological examination of gill sections. To explore the underlying molecular events that are associated with the progression of PGD, we sampled Atlantic salmon from three different marine production sites in Scotland and examined the gill tissue at three different levels of organization: gross morphology with the use of PGD scores (macroscopic examination), whole transcriptome (gene expression by RNA-seq) and histopathology (microscopic examination). Our results strongly suggested that the changes in PGD scores of the gill tissue were not associated with the changes in gene expression or histopathology. In contrast, integration of the gill RNA-seq data with the gill histopathology enabled us to identify common gene expression patterns associated with multifactorial gill disease, independently from the origin of samples. We demonstrated that the gene expression patterns associated with multifactorial gill disease were dominated by two processes: a range of immune responses driven by pro-inflammatory cytokines and the events associated with tissue damage and repair, driven by caspases and angiogenin.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Krol, E., Noguera, P., Shaw, S., Costelloe, E., Gajardo, K., Valdenegro, V., Bickerdike, R., Douglas, A. & Martin, S. A. M. (2020). Integration of transcriptome, gross morphology and histopathology in the gill of sea farmed Atlantic salmon (Salmo salar): lessons from multi-site sampling. Frontiers in Genetics, 11: 610.",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "610",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "11",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1130",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:30.369+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/d6f46a6c-bc49-4a50-8663-69e8193e2094"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "e6a198bf-e83f-47fd-9bdd-3aff41634cee",
              "uuid" : "e6a198bf-e83f-47fd-9bdd-3aff41634cee",
              "name" : "Validated shipping noise maps of the Northeast Atlantic",
              "handle" : "20.500.12594/11250",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Farcas, A.",
                  "language" : "en",
                  "authority" : "474f4d49-a44d-47bb-8cb1-56a4cc240250",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Powell, C.F.",
                  "language" : "en",
                  "authority" : "21a65077-0665-40fd-893c-14ac04b33f25",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Brookes, K.L.",
                  "language" : "en",
                  "authority" : "2c18fe7c-28b2-4120-8e14-a79cbb24cd0f",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Merchant, N.D.",
                  "language" : "en",
                  "authority" : "6db7b226-69be-4206-bd61-af5a58183ecc",
                  "confidence" : -1,
                  "place" : 3
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:38Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:38Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.1016/j.scitotenv.2020.139509",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11250",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Science of the Total Environment",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Validated shipping noise maps of the Northeast Atlantic",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Underwater noise pollution from shipping is globally pervasive and has a range of adverse impacts on species which depend on sound, including marine mammals, sea turtles, fish, and many invertebrates. International bodies including United Nations agencies, the Arctic Council, and the European Union are beginning to address the issue at the policy level, but better evidence is needed to map levels of underwater noise pollution and the potential benefits of management measures such as ship-quieting regulations. Crucially, corroboration of noise maps with field measurements is presently lacking, which undermines confidence in their application to policymaking. We construct a computational model of underwater noise levels in the Northeast Atlantic using Automatic Identification System (AIS) ship-tracking data, wind speed data, and other environmental parameters, and validate this model against field measurements at 4 sites in the North Sea. Overall, model predictions of the median sound level were within ±3 dB for 93% of the field measurements for one-third octave frequency bands in the range 125 Hz–5 kHz. Areas with median noise levels exceeding 120 dB re 1 μPa and 20 dB above modelled natural background sound were predicted to occur in the Dover Strait, the Norwegian trench, near to several major ports, and around offshore infrastructure sites in the North Sea. To our knowledge, this is the first study to quantitatively validate large-scale modelled noise maps with field measurements at multiple sites. Further validation will increase confidence in deeper waters and during winter months. Our results highlight areas where anthropogenic pressure from shipping noise is greatest and will inform the management of shipping noise in the Northeast Atlantic. The good agreement between measurements and model gives confidence that models of shipping noise can be used to inform future policy and management decisions to address shipping noise pollution.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Farcas, A., Powell, C. F., Brookes, K. L. & Merchant, N. D. (2020). Validated shipping noise maps of the Northeast Atlantic. Science of the Total Environment, 735, 139509. doi:https://doi.org/10.1016/j.scitotenv.2020.139509",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "139509",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "735",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1126",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:34.112+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/e6a198bf-e83f-47fd-9bdd-3aff41634cee"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        }, {
          "hitHighlights" : null,
          "type" : "discover",
          "_links" : {
            "indexableObject" : {
              "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a"
            }
          },
          "_embedded" : {
            "indexableObject" : {
              "id" : "db7a807d-e0a9-4353-b559-aa8a6a74058a",
              "uuid" : "db7a807d-e0a9-4353-b559-aa8a6a74058a",
              "name" : "Genome Sequencing of SAV3 Reveals Repeated Seeding Events of Viral Strains in Norwegian Aquaculture",
              "handle" : "20.500.12594/11251",
              "metadata" : {
                "dc.contributor.author" : [ {
                  "value" : "Gallagher, M.D.",
                  "language" : "en",
                  "authority" : "7b68fd4b-bc9b-4603-9150-55d5903ad6eb",
                  "confidence" : -1,
                  "place" : 0
                }, {
                  "value" : "Karlsen, M.",
                  "language" : "en",
                  "authority" : "e550b041-9966-4e7d-a493-2c2701220287",
                  "confidence" : -1,
                  "place" : 1
                }, {
                  "value" : "Petterson, E.",
                  "language" : "en",
                  "authority" : "77342323-c6e0-4b66-8eb3-eddd1c05b831",
                  "confidence" : -1,
                  "place" : 2
                }, {
                  "value" : "Haugland, Ø.",
                  "language" : "en",
                  "authority" : "2bd62b84-51c7-4eed-b656-baed0c746930",
                  "confidence" : -1,
                  "place" : 3
                }, {
                  "value" : "Matejusova, I.",
                  "language" : "en",
                  "authority" : "383ce323-fe7e-470a-b5f1-c0a216e2b8d7",
                  "confidence" : -1,
                  "place" : 4
                }, {
                  "value" : "Macqueen, D.J.",
                  "language" : "en",
                  "authority" : "d516a418-c8ae-4b50-9879-98c07e102332",
                  "confidence" : -1,
                  "place" : 5
                } ],
                "dc.coverage.temporal" : [ {
                  "value" : "2020/2021",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.accessioned" : [ {
                  "value" : "2021-05-05T11:17:38Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.available" : [ {
                  "value" : "2021-05-05T11:17:38Z",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.date.issued" : [ {
                  "value" : "2020",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.doi" : [ {
                  "value" : "https://doi.org/10.3389/fmicb.2020.00740",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.issn" : [ {
                  "value" : "1664-302X",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.identifier.uri" : [ {
                  "value" : "https://hdl.handle.net/20.500.12594/11251",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.relation.ispartof" : [ {
                  "value" : "Frontiers in Microbiology",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.title" : [ {
                  "value" : "Genome Sequencing of SAV3 Reveals Repeated Seeding Events of Viral Strains in Norwegian Aquaculture",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dc.type" : [ {
                  "value" : "Article - peer-reviewed",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.abstract" : [ {
                  "value" : "Understanding the dynamics of pathogen transfer in aquaculture systems is essential to manage and mitigate disease outbreaks. The goal of this study was to understand recent transmission dynamics of salmonid alphavirus (SAV) in Norway. SAV causes significant economic impacts on farmed salmonids in European aquaculture. SAV is classified into six subtypes, with Norway having ongoing epidemics of SAV subtypes 2 and 3. These two viral subtypes are present in largely distinct geographic regions of Norway, with SAV2 present in Trondelag, SAV3 in Rogaland, Sogn og Fjordane, and Hordaland, and Møre og Romsdal having outbreaks of both subtypes. To determine likely transmission routes of Norwegian SAV an established Nanopore amplicon sequencing approach was used in the current study. After confirming the accuracy of this approach for distinguishing subtype level co-infections of SAV2 and SAV3, a hypothetical possibility in regions of neighboring epidemics, twenty-four SAV3 genomes were sequenced to characterize the current genetic diversity of SAV3 in Norwegian aquaculture. Sequencing was performed on naturally infected heart tissues originating from a range of geographic locations sampled between 2016 and 2019. Phylogenetic analyses revealed that the currently active SAV3 strains sampled comprise several distinct lineages sharing an ancestor that existed ∼15 years ago (95% HPD, 12.51–17.7 years) and likely in Hordaland. At least five of these lineages have not shared a common ancestor for 7.85 years (95% HPD, 5.39–10.96 years) or more. Furthermore, the ancestor of the strains that were sampled outside of Hordaland (Sogn of Fjordane and Rogaland) existed less than 8 years ago, indicating a lack of long-term viral reservoirs in these counties. This evident lack of geographically distinct subclades is compatible with a source-sink transmission dynamic explaining the long-term movements of SAV around Norway. Such anthropogenic transport of the virus indicates that at least for sink counties, biosecurity strategies might be effective in mitigating the ongoing SAV epidemic. Finally, genomic analyses of SAV sequences were performed, offering novel insights into the prevalence of SAV genomes containing defective deletions. Overall, this study improves our understanding of the recent transmission dynamics and biology of the SAV epidemic affecting Norwegian aquaculture.",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.bibliographicCitation" : [ {
                  "value" : "Gallagher, M. D., Karlsen, M., Petterson, E., Haugland, Ø., Matejusova, I. & Macqueen, D. J. (2020). Genome Sequencing of SAV3 Reveals Repeated Seeding Events of Viral Strains in Norwegian Aquaculture. Frontiers in Microbiology, 11: 740. doi:10.3389/fmicb.2020.00740",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.sizeOrDuration" : [ {
                  "value" : "740",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "dcterms.volume" : [ {
                  "value" : "11",
                  "language" : null,
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ],
                "rsc.identifier" : [ {
                  "value" : "MARINE_1127",
                  "language" : "en",
                  "authority" : null,
                  "confidence" : -1,
                  "place" : 0
                } ]
              },
              "inArchive" : true,
              "discoverable" : true,
              "withdrawn" : false,
              "lastModified" : "2021-05-11T03:01:31.382+00:00",
              "entityType" : null,
              "type" : "item",
              "_links" : {
                "accessStatus" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/accessStatus"
                },
                "bundles" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/bundles"
                },
                "identifiers" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/identifiers"
                },
                "mappedCollections" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/mappedCollections"
                },
                "owningCollection" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/owningCollection"
                },
                "relationships" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/relationships"
                },
                "version" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/version"
                },
                "templateItemOf" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/templateItemOf"
                },
                "thumbnail" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a/thumbnail"
                },
                "self" : {
                  "href" : "http://localhost:8080/server/api/core/items/db7a807d-e0a9-4353-b559-aa8a6a74058a"
                }
              },
              "_embedded" : {
                "thumbnail" : null
              }
            }
          }
        } ]
      },
      "page" : {
        "number" : 0,
        "size" : 20,
        "totalPages" : 24,
        "totalElements" : 469
      },
      "_links" : {
        "next" : {
          "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&sort=dc.date.accessioned,DESC&page=1"
        },
        "last" : {
          "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&sort=dc.date.accessioned,DESC&page=23"
        },
        "self" : {
          "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&sort=dc.date.accessioned,DESC"
        }
      }
    },
    "facets" : [ {
      "name" : "author",
      "facetType" : "text",
      "facetLimit" : 5,
      "minValue" : "(inc. Hollingsworth, P.M.",
      "maxValue" : "王, 年 [Nian Wang]",
      "page" : {
        "number" : 0,
        "size" : 5
      },
      "_links" : {
        "next" : {
          "href" : "http://localhost:8080/server/api/discover/facets/author?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&page=1&size=5"
        },
        "self" : {
          "href" : "http://localhost:8080/server/api/discover/facets/author?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&size=5"
        }
      },
      "_embedded" : {
        "values" : [ {
          "label" : "Bresnan, E.",
          "count" : 31,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.author=Bresnan,%20E.,equals"
            }
          }
        }, {
          "label" : "Wright, P.J.",
          "count" : 26,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.author=Wright,%20P.J.,equals"
            }
          }
        }, {
          "label" : "Collet, B.",
          "count" : 24,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.author=Collet,%20B.,equals"
            }
          }
        }, {
          "label" : "Malcolm, I.A.",
          "count" : 24,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.author=Malcolm,%20I.A.,equals"
            }
          }
        }, {
          "label" : "Collins, C.",
          "count" : 20,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.author=Collins,%20C.,equals"
            }
          }
        } ]
      }
    }, {
      "name" : "subject",
      "facetType" : "hierarchical",
      "facetLimit" : 5,
      "_links" : {
        "self" : {
          "href" : "http://localhost:8080/server/api/discover/facets/subject?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e"
        }
      },
      "_embedded" : {
        "values" : [ ]
      }
    }, {
      "name" : "dateIssued",
      "facetType" : "date",
      "facetLimit" : 5,
      "minValue" : "1683",
      "maxValue" : "In press",
      "page" : {
        "number" : 0,
        "size" : 5
      },
      "_links" : {
        "self" : {
          "href" : "http://localhost:8080/server/api/discover/facets/dateIssued?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&size=5"
        }
      },
      "_embedded" : {
        "values" : [ {
          "label" : "2015 - 2019",
          "count" : 416,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.dateIssued=%5B2015%20TO%202019%5D,equals"
            }
          }
        }, {
          "label" : "2020 - 2021",
          "count" : 52,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.dateIssued=%5B2020%20TO%202021%5D,equals"
            }
          }
        } ]
      }
    }, {
      "name" : "has_content_in_original_bundle",
      "facetType" : "standard",
      "facetLimit" : 2,
      "page" : {
        "number" : 0,
        "size" : 2
      },
      "_links" : {
        "self" : {
          "href" : "http://localhost:8080/server/api/discover/facets/has_content_in_original_bundle?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&size=2"
        }
      },
      "_embedded" : {
        "values" : [ {
          "label" : "false",
          "count" : 468,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.has_content_in_original_bundle=false,equals"
            }
          }
        }, {
          "label" : "true",
          "count" : 1,
          "authorityKey" : null,
          "type" : "discover",
          "_links" : {
            "search" : {
              "href" : "http://localhost:8080/server/api/discover/search/objects?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e&f.has_content_in_original_bundle=true,equals"
            }
          }
        } ]
      }
    }, {
      "name" : "entityType",
      "facetType" : "text",
      "facetLimit" : 5,
      "_links" : {
        "self" : {
          "href" : "http://localhost:8080/server/api/discover/facets/entityType?dsoType=ITEM&scope=b66c063b-093e-487a-a35e-3b82ce00468e"
        }
      },
      "_embedded" : {
        "values" : [ ]
      }
    } ]
  }
}
"""
