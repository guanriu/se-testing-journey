# 定义输入和输出的文件路径
input_file = "data/app.log"
output_file = "data/error.log"

print("开始处理日志...")

# 1. 打开文件并读取
# with open(...) as f 是 Python 中处理文件的黄金标准，它会在用完后自动帮你关闭文件
try:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines() # 读取所有行，存成一个列表
        
    error_count = 0
    error_lines = [] # 准备一个空列表，用来装找出来的 ERROR 日志
    
    # 2. 遍历每一行
    for line in lines:
        # 如果 "ERROR" 这个单词存在于这一行里
        if "ERROR" in line:
            error_count += 1
            error_lines.append(line) # 把它装进我们的列表里

    # 3. 把抓出来的错误日志写入新文件
    with open(output_file, "w", encoding="utf-8") as f:
        # writelines 会把列表里的所有字符串一次性写进文件
        f.writelines(error_lines) 
        
    print(f"处理完成！一共发现 {error_count} 条 ERROR 日志。")
    print(f"已保存到 {output_file}，请去查看。")

except FileNotFoundError:
    print(f"报错啦：找不到文件 {input_file}，请检查路径！")