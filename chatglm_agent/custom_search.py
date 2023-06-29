import requests

# RapidAPIKey = "5116ad5575msh1f7418d794eb2c1p1b0554jsn874ee243811d"
RapidAPIKey = "d250f5d98amshc6c294b2b0e6dc7p1248e2jsn2160c6cf8c09"

class DeepSearch:
    def search(query: str = ""):
        query = query.strip()

        if query == "":
            return ""

        if RapidAPIKey == "":
            return "请配置你的 RapidAPIKey"

        # # url = "https://bing-web-search1.p.rapidapi.com/search"
        # url = "https://bing-web-search4.p.rapidapi.com/bing-search"

        # querystring = {"q": query,
        #         "mkt":"zh-cn","textDecorations":"false","setLang":"CN","safeSearch":"Off","textFormat":"Raw"}

        # headers = {
        #     "Accept": "application/json",
        #     "X-BingApis-SDK": "true",
        #     "X-RapidAPI-Key": RapidAPIKey,
        #     "X-RapidAPI-Host": "bing-web-search1.p.rapidapi.com"
        # }
        # response = requests.get(url, headers=headers, params=querystring)
        url = "https://bing-web-search1.p.rapidapi.com/search"
        # url = "https://bing-web-search4.p.rapidapi.com/bing-search"
        print(f'query===={query}')
        payload = {
            "keyword": query,
            "page": 1,
            "lang": "en",
            "region": "us"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RapidAPIKey,
            "X-RapidAPI-Host": "bing-web-search4.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
        print(f'response==={response.json()}')
        # data_list = response.json()['value']
        data_list = response.json()['search_results']
        if len(data_list) == 0:
            return ""
        else:
            result_arr = []
            result_str = ""
            count_index = 0
            for i in range(6):
                item = data_list[i]
                title = item["name"]
                description = item["description"]
                item_str = f"{title}: {description}"
                result_arr = result_arr + [item_str]

            result_str = "\n".join(result_arr)
            return result_str

