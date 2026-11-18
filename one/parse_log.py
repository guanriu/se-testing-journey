# 假设我们拿到了一行日志
raw_log = "  2026-10-27 10:30:00 INFO  [UserService] Login successful  "

# 1. 去除首尾多余的空格(strip)
# 注意如果不加strip，首尾的空格会被当成内容切分，导致结果错乱
clean_log = raw_log.strip()
# 2. 用 split() 按空格把字符串切成一个列表 (list)
# split() 默认会把连续的空格当成一个分隔符
log_parts = clean_log.split()

# 3.打印看看切成什么样子了
print("切分后的列表：\n",log_parts)

# 4.通过索引（下标）提取我们需要的数据
# 列表的索引从0开始数
if len(log_parts) >= 5:
    date = log_parts[0]
    time = log_parts[1]
    level = log_parts[2]
    module = log_parts[3]
    message = " ".join(log_parts[4:]) #把后面的内容用空格重新拼接起来
    print(f"【提取结果】日期:{date}, 时间:{time}, 级别:{level}, 模块:{module}, 消息:{message}")
else:
    print("日志格式不符合预期，无法解析！")
