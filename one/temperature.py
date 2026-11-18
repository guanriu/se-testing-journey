def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    try:
        user_input = input("请输入摄氏度温度（例如 25）：")
        c = float(user_input)
        f = celsius_to_fahrenheit(c)
        print(f"{c} 摄氏度 = {f:.1f} 华氏度")
    except ValueError:
        print("输入无效！请输入数字。")