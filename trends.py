from pytrends.request import TrendReq

BAD_KEYWORDS = ["weather", "sports", "lottery", "death"]

def score(topic):
    score = 0
    if len(topic.split()) <= 6:
        score += 1
    if any(w in topic.lower() for w in ["ai", "tech", "new", "internet"]):
        score += 2
    if not any(b in topic.lower() for b in BAD_KEYWORDS):
        score += 1
    return score

def get_best_trending_topic():
    py = TrendReq(hl="en-US", tz=360)
    trends = py.trending_searches(pn="united_states").head(10)
    ranked = [(t[0], score(t[0])) for t in trends.values]
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked[0][0]
