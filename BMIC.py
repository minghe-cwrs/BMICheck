while True:
        w = float(input("输入体重[千克/公斤]\n[local]~#"))
        h = float(input("\n输入身高[米]\n(带小数点)\n[local]~#："))
        bmi = w/(h**2)
        print("\n您的BMI为：" + str(bmi) + "\n")

        if bmi < 18.5:
                print("您的体重偏轻！")
                print("多吃点吧！！")
        elif 18.5 <= bmi < 24:
                print("您的体重在正常范围内")
                print("该吃吃该喝喝 让自己快乐就好!")
        elif 24 <= bmi < 27:
                print("您似乎属于微胖？")
                print("多多锻炼 有益身心！不需要太担心")
        elif 27 <= bmi < 30:
                print("您有点小胖啦")
                print("多出门走走，去探索世界吧！")
        elif 30 <= bmi < 35:
                print("呀，您重得")
                print("是时候呼叫营养师了！")
        elif bmi >= 35:
                print("您这...")
                print("赶紧打电话咨询营养师吧！")
        
        input("\n程序到此结束，按任意键继续！\n(程序会不停循环 直到您关掉为止)")