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

    def process(self, d, collection, authors):
        print(f"\033[1;32m{self.uuid} '\033[33m{self.title}\033[0;37m'")

        for a, auth in self.authors:
            if auth.startswith("virtual"):
                print(f"\033[35mSkipping\033[37m '{a}'")
                continue

            author = names.tidy(a)

            if a != author: print(f"\033[32mConverted\033[37m' {a}' to '{author}'")

            if author in authors:
                author_uuid = authors[author]
                if not d.add_author_to_item(author_uuid, self.uuid): return False

                print(f"\033[36mAdded\033[37m '{author}'  with id {author_uuid}")
            else:
                author_uuid = d.create_author_entity(collection, author)
                if author_uuid is None: return False
                if not d.add_author_to_item(author_uuid, self.uuid): return False
                authors[author] = author_uuid

                print(f"\033[33mCreated\033[37m '{author}' with id {author_uuid}")

        if (places := d.get_item(self.uuid)) is None: return False

        type_places, auth_places = places

        if not d.patch_item(self.uuid, type_places, auth_places): return False

        return True

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
