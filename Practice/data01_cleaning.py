try:
    count = 0
    with open("data/error.log","r",encoding='utf-8') as f:
        for line in f:
            if "ERROR" in line:
               print(line.strip())
               count += 1
    print(f"\n错误日志总条数：{count}")
except FileNotFoundError:
    print("日志文件找不到")