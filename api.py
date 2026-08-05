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