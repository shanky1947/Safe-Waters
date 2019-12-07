people='''
{
  "annotations": {
    "Grab0.jpg": [
      {
        "label": "knee deep"
      }
    ],
    "Grab1.jpg": [
      {
        "label": "feet-dont-touch deep"
      }
    ],

   }
}
'''


import json
data=json.loads(people)
file1 = open(r"D:\ML\Safe Waters\labels_json.txt","w+")
for i in range(0,2):
    #print(data['annotations']['Grab'+str(i)+'.jpg'][0]['label'])
    l=["Grab",str(i),"-",data['annotations']['Grab'+str(i)+'.jpg'][0]['label'],"\n"]
    file1.writelines(l)
