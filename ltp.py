from ltp import LTP

ltp = LTP()

result = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks = ["cws","ner"])
print(result.ner)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]