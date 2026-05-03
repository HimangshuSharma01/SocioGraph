import json
#load # clean and # find the mutual

# load 
def load(file):
    with open(file,"r") as f:
        y = json.load(f)
    return y
i = input("Enter the file name : ")
x = load(i)
#clean checklist - look for inactive users(by no liked pages and no friends)
#                   remove the duplicate friends
#                   check for empty name 
#                   The pages list contains duplicate page IDs

def clean(file):
    file["users"] = [user for user in file["users"] if user["name"].strip()] # this will remove the empty name strings from json
    for user in file["users"]:
        user["friends"] = list(set(user["friends"]))
    file["users"] = [user for user in file["users"] if user["liked_pages"] or user["friends"]]
    u = {}
    for page in file["pages"]:
        u[page["id"]]=page
        file["pages"]=list(u.values())
    return file

y = clean(x)
output_name=i.replace(".json","")+"_cleaned.json"
json.dump(y,open(output_name,"w"),indent=0)


# mutuals - find frnds , find direct frnds , then mutuals

def find_mutuals(uid,data):
    user_friends={}
    u_to_name = {}
    for user in data["users"]:
        user_friends[user["id"]]=user["friends"] #we need not need to check for duplicate friends bcz we already cleaned up
        u_to_name[user["id"]]=user["name"]   
    if uid not in user_friends:
        return []
    direct_friends = user_friends[uid]
    suggestions={}
    for friends in direct_friends:
        for mutuals in user_friends[friends]:
            if mutuals != uid and mutuals not in direct_friends:
                suggestions[mutuals]=suggestions.get(mutuals,0)+1 #count

    sorted_suggestions=sorted(suggestions.items(), key = lambda x : x[1],  reverse=True)
    return[u_to_name[sid] for sid,_ in sorted_suggestions]  

h = int(input("Enter your ID to find your mutuals : "))
s = find_mutuals(h,y)
print(f"Fecthing mutuals for User{h}.....")
print(f" "*300)
print(f"The mutuals are fetched....")
print(f" "*300)
print(f"The mutuals for the User{h} is/are : {s}")