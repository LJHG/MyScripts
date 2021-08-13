import os

for i in range(406):
    os.system("python ./infer.py -d ../../../smalldatasets/smalldataset{}-{} -l ./logs-v2-crf-smalldatasets/logs-v2-crf-{}-{} -m ./models/squeezesegV2-crf".format(i*10,i*10+20,i*10,i*10+20))




