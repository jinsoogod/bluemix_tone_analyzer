import matplotlib.pyplot as plt
import json
from os.path import join, dirname
from matplotlib import font_manager, rc
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username='b01eadca-1a8f-4dd1-839c-6dfe0a6f0869',
    password='ZHRaS6YhsLlm',
    version='2017-07-17')

print("\ntone() example 4:\n")
with open(join(dirname(__file__),
               'C:/Users/jklim/Downloads/tone.json')) as tone_json:
    tone = tone_analyzer.tone(json.load(tone_json), 'emotion',
                              content_type='application/json', )

print(json.dumps(tone, indent=2))
print("----------------------------------------------------------------------")

document_tone = tone["document_tone"]["tone_categories"][0]["tones"]

tone_name = []
tone_score = []

for a in document_tone:
    tone_name.append(a['tone_name'])
    tone_score.append(a['score'])

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

fig = plt.figure()
ax = plt.subplot(111)
ypos = range(1,len(tone_score)+1)
plt.barh(ypos, tone_score, align='center', height=0.5)

plt.yticks(ypos, tone_name)

plt.xlabel('Document_tone')

plt.show()