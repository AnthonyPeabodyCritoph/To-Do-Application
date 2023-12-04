class File:

    def initialiseList():
        import os
        import json
        scriptPath = os.path.dirname(os.path.abspath(__file__))
        listDataPath = os.path.join (scriptPath, 'list.txt')       
        if os.path.exists(listDataPath):
            listData = open('list.txt', 'r')
            listRaw = listData.read()
            try:
                list = json.loads(listRaw)
            except json.decoder.JSONDecodeError:
                list = {}
            return list
        else:
            list = {}
            return list

    def saveList(list):
        import json
        listData = open('list.txt', 'w')
        listData.write(json.dumps(list))
        listData.close()