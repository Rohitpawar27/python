# states=[
#     {"state_id":1,"state_name":"maharashtra","cities":[
#         {"city_id":1,"city_name":"mumbai"},
#         {"city_id":2,"city_name":"pune"}
#     ]},
#     {"state_id":2,"state_name":"gujrat","cities":[
#         {"city_id":3,"city_name":"ahmdabad"},
#          {"city_id":4,"city_name":"surat"}
#     ]}
#  ]
# for s in states:
#     print(str(s["state_id"])+" "+s["state_name"])
#     for c in s["cities"]:
#         print("\t"+str(c["city_id"])+" "+c["city_name"])
#         print("----------------------------")

# ------------------------------------------------------------------


# states=[
#     {"state_id":1,"state_name":"maharashtra","cities":[
#         {"city_id":1,"city_name":"mumbai"},
#         {"city_id":2,"city_name":"pune"}],"location":[
#         {"location_id":1,"location_name":"pimpri"},
#         {"location_id":2,"location_name":"Hadapsar"}]
#         },
#     {"state_id":2,"state_name":"gujrat","cities":[
#         {"city_id":3,"city_name":"ahmdabad"},
#         {"city_id":4,"city_name":"surat"}],"location":[
#         {"location_id":3,"location_name":"juna_bazar"},
#         {"location_id":4,"location_name":"new_bazar"}]
#     }
# ]
# for s in states:
#     print(str(s["state_id"])+" "+s["state_name"])
#     for c in s["cities"]:
#         print("\t"+str(c["city_id"])+" "+c["city_name"])
#         for l in s["location"]:
#             print("\t"+str(l["location_id"])+" "+l["location_name"])
#         print("----------------------------")



