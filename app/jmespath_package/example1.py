import jmespath

obj = {
    "people":[
        {
          "name":"A",
          "age":30
        },{
          "name":"B",
          "age":70
        },{
          "name":"C",
          "age":50
        },
    ]
}

search_pattern = 'max_by(people,&age).name'
search_result = jmespath.search(search_pattern, obj)
print("search_result==", search_result)