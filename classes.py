from dataclasses import dataclass

import names

##############################################################################

@dataclass
class Item:
    uuid:    str
    title:   str
    authors: list[tuple[str, str]]

    @classmethod
    def from_json(cls, json):
        match json:
            case { "_embedded": {
                    "indexableObject": {
                        "id": uuid, "metadata": {
                            "dc.contributor.author": authors,
                            "dc.title": titles,
                        }
                      }
                    }
                  }:

                title = " ".join([ v["value"] for v in titles ])
                return cls(uuid, title, [ (author["value"], author["authority"]) for author in authors ])

    def __lt__(self, other): return self.title < other.title

    def process(self, d, collection):
        print(f"\033[1;32m{self.uuid} \033[33m{self.title}\033[0;37m ({len(self.authors)})")

        d.set_item_type_to_publication(self)

        for a, auth in self.authors:
            if auth.startswith("virtual"):
                print(f"\033[35mSkipping\033[37m '{a}'")
                continue

            author = names.tidy(a)

            if a != author: print(f"    \033[32mConverted\033[37m' {a}' to '{author}'")

            for c in "|;:":
                if c in author:
                    print(f"\033[1;44mMultiple authors: {author}\033[0;40m")
                    authors = [ s.strip() for s in author.split(c) ]
                    authors = [ s for s in authors if len(s) > 0 ]
                    break
            else:
                authors = [ author ]

            for author in authors:
                if not self.add_author_to_item(d, author, collection):
                    return False

        match d.get_item(self.uuid):
            case type_places, auth_places:
                return d.remove_old_author_metadata(self.uuid, auth_places)

    def add_author_to_item(self, d, author, collection):
        if (author_uuid := d.get_author_uuid(collection, author)) is not None:
            s = f"\033[36mAdded\033[37m"
        elif (author_uuid := d.create_author_entity(collection, author)) is not None:
            s = f"\033[33mCreated\033[37m"
        else:
            return False
                
        params = { "typeId": 1,
                   "relationshipLabel": "isAuthorOfPublication",
                   "focusItem": self.uuid,
                   "relatedItem": author_uuid }

        match d.get_embedded("core/relationships/search/byItemsAndType", **params):
            case { "relationships": rel }:
                if len(rel) > 0:
                    print(f"'{author}' has already been added")
                    return True
        
        if not d.add_author_to_item(author_uuid, self.uuid): return False

        print(f"{s} '{author}'  with id {author_uuid}")

        return True

##############################################################################

@dataclass
class Author:
    uuid:     str
    surname:  str
    forename: str

    @classmethod
    def from_json(cls, json):
        match json:
            case { "_embedded": {
                    "indexableObject": {
                        "id": uuid, "metadata": {
                            "person.familyName": surname,
                            "person.givenName": forename,
                        }
                      }
                    }
                  }:
                sn = " ".join([ v["value"] for v in surname ])
                fn = " ".join([ v["value"] for v in forename ])

                return cls(uuid, sn, fn)

    def __lt__(self, other): return self.title < other.title

    @property
    def fullname(self): return f"{self.surname}, {self.forename}"

##############################################################################

@dataclass
class Community:
    name: str
    uuid: str

    @classmethod
    def from_json(cls, json):
        match json:
            case { "name": name, "uuid": uuid }: return cls(name, uuid)

##############################################################################

@dataclass
class Collection:
    name: str
    uuid: str
    community: Community

    @classmethod
    def from_json(cls, json, comm):
        match json:
            case { "name": name, "uuid": uuid }: return cls(name, uuid, comm)

##############################################################################
