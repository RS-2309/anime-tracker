import json
import requests

class Api:
    @staticmethod
    def search(anime):
        url = "https://graphql.anilist.co"

        query = """
            query ($search: String, $limit: Int) {
                Page (perPage: $limit) {
                    media (search: $search, type: ANIME) {
                        id
                        format
                        episodes
                        seasonYear

                        title {
                            romaji
                            english
                        }
                        
                        coverImage {
                            extraLarge
                            large
                        }
                        
                    }
                }
            }
        """

        variables = {
            "search": anime,
            "limit": 10
        }

        response = requests.post(url, json={"query": query, "variables": variables})

        data = response.json()

        anime_list = data["data"]["Page"]["media"]

        i = 0

        while True:
            if i == len(anime_list):
                break
            if anime_list[i]["title"]["english"] is None:
               anime_list.pop(i)
               continue

            i += 1

        return anime_list

    
    @staticmethod
    def getAnime(id):
        url = "https://graphql.anilist.co"

        query = """
            query ($id: Int) {
                Media (id: $id, type: ANIME) {
                    description
                    genres
                    averageScore
                    format
                    episodes
                    seasonYear
                    
                    studios {
                        nodes {
                            name
                        }
                    }

                    title {
                        romaji
                        english
                    }
                    
                    coverImage {
                        extraLarge
                        large
                    }
                    
                }
            }
        """

        variables = {
            "id": id,
        }

        response = requests.post(url, json={"query": query, "variables": variables})

        data = response.json()

        anime = data['data']['Media']

        studioNames = []

        for dictionary in anime['studios']['nodes']:
            studioNames.append(dictionary['name'])

        return anime, studioNames

    @staticmethod
    def get_data(id):
        url = "https://graphql.anilist.co"

        query = """
            query ($id: Int) {
                Media (id: $id, type: ANIME) {

                    title {
                        english
                    }
                
                    genres
                    averageScore
                    format
                    episodes

                    season
                    seasonYear

                    status
                    duration
                    source

                    isAdult

                    startDate {
                        year
                    }

                    endDate {
                        year
                    }
                    
                    studios {
                        nodes {
                            name
                        }
                    }
                    
                }
            }
        """

        variables = {
            "id": id,
        }

        response = requests.post(url, json={"query": query, "variables": variables})

        mid_1 = response.json()

        mid_2 = mid_1['data']['Media']

        data = [
            id,
            mid_2["title"]["english"],
            json.dumps(mid_2["genres"]),
            mid_2["averageScore"],
            mid_2["format"],
            mid_2["episodes"],
            mid_2["season"],
            mid_2["seasonYear"],
            mid_2["status"],
            mid_2["duration"],
            mid_2["source"],
            mid_2["isAdult"],
            mid_2["startDate"]["year"] if mid_2["startDate"] else None,
            mid_2["endDate"]["year"] if mid_2["endDate"] else None,
            json.dumps([studio["name"] for studio in mid_2["studios"]["nodes"]])
        ]

        #studioNames = []

        #for dictionary in anime['studios']['nodes']:
            #studioNames.append(dictionary['name'])

        return data#, studioNames