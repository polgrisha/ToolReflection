from GoogleNews import GoogleNews
from typing import Dict, List
class NewsAPI:

    @staticmethod
    def get_recent_news(query: str) -> List[str]:
        googlenews = GoogleNews()
        googlenews.get_news(query)
        return googlenews.get_texts()[:10]

if __name__ == '__main__':
    q = "Apple"
    print(f"Get news about {q}?")
    print(f"Top news titles about {q} are  {NewsAPI.get_recent_news(q)}")