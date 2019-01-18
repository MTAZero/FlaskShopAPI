from model.db import database

def getAllItem():
    print("Get All item")
    ans = []
    try:
        ans = list(database.items.find({}))
    except Exception as e:
        print(str(e))

    return ans