import json
with open('data/test_data.json',"r",encoding='utf-8') as f:
    data_list = json.load(f)

print(f"读到的数据类型是{type(data_list)}")
print(f"一共有几条数据{len(data_list)}")
print(f'第一条的数据标题是{data_list[0]['title']}')