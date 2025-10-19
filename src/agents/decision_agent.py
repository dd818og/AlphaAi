import json
from jsonschema import validate
# Decision Agent - stub
def decide(signal):
    # simple rule: buy if score > 0.6
    if signal.get('score',0) > 0.6:
        proposal = {
            "symbol": signal['symbol'],
            "side": "BUY",
            "size": 100,
            "confidence": signal.get('confidence',0.5),
            "rationale_id": "r-001"
        }
        return proposal
    return None
if __name__=='__main__':
    s = {"symbol":"AAPL","score":0.7,"confidence":0.8}
    print(decide(s))
