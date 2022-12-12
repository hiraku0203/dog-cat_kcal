import math


weight = float(input("体重を入力:"))

# RER:安静時エネルギー要求量計算
def RER(weight) :
    f = weight**3
    first_sqrt = math.sqrt(f)
    # print(first_sqrt)
    second_sqrt = math.sqrt(first_sqrt)
    # print(second_sqrt)
    rer = int(second_sqrt * 70)
    return rer


# DER:1日あたりのエネルギー要求量
def DER(rer):
    while True :
        q1 = int(input("犬なら1、猫なら2を入力:"))
        # 計算したいのが犬ならば
        if q1 == 1 :
            while True:
                dog_q1 = int(input("成犬なら1、生後12ヶ月以内なら2、高齢犬または肥満傾向なら3を入力:"))

                # 成犬ならば
                if dog_q1 ==  1 :
                    dog_q2 = int(input("去勢済なら1、していないなら2を入力:"))
                    if dog_q2 == 1 :
                        der = int(rer * 1.6)
                        return der

                    elif dog_q2 == 2 :
                        der = int(rer * 1.8)
                        return der

                    else :
                        print("1または2を入力")
                        continue

                # 子犬ならば
                elif dog_q1 == 2 :
                    while True :
                        born = int(input("生後何ヵ月?12以内で入力:"))
                        if born < 4 :
                            der = int(rer * 3.0)
                            return der
                        elif born >= 4 and born <= 9 :
                            der = int(rer * 2.5)
                            return der
                        elif born >= 10 and born <= 12 :
                            der = int(rer * 2.0)
                            return der
                        else :
                            print("12以内で入力")
                            continue

                # 高齢犬または肥満傾向ならば
                elif dog_q1 == 3 :
                        der = int(rer * 1.4)
                        return der
                        
                # 入力エラーならば
                else :
                    print("1、2、3のどれかを入力")
                    continue
        
        # 猫の場合
        elif q1 == 2 :  
            while True:
                cat_q1 = int(input("成猫なら1、生後12ヶ月以内なら2、高齢猫なら3、肥満傾向なら4を入力:"))

                # 成猫の場合
                if cat_q1 ==  1 :
                    cat_q2 = int(input("去勢済なら1、していないなら2を入力:"))

                    if cat_q2 == 1 :
                        der = int(rer * 1.2)
                        return der

                    elif cat_q2 == 2 :
                        der = int(rer * 1.4)
                        return der

                    else :
                        print("1または2を入力")
                        continue

                # 子猫の場合
                elif cat_q1 == 2 :
                    while True :
                        born = int(input("生後何ヵ月?12以内で入力:"))
                        if born < 4 :
                            der = int(rer * 3.0)
                            return der
                        elif born >= 4 and born <= 6 :
                            der = int(rer * 2.5)
                            return der
                        elif born >= 7 and born <= 12 :
                            der = int(rer * 2.0)
                            return der
                        else :
                            print("12以内で入力")
                            continue

                # 高齢の場合
                elif cat_q1 == 3 :
                    der = int(rer * 1.1)
                    return der

                # デブ猫なら
                elif cat_q1 == 4 :
                    der = int(rer * 1.0)
                    return der

                # 入力エラーの場合
                else :
                    print("1、2、3のどれかを入力")
                    continue

        # 入力エラーの場合
        else :
            print("1または2で入力")
            continue

# 一日の必要なカロリーを計算
def FOOD(der) :
    g_kcal = int(input("与えているフードの100gあたりのkcalを入力してください:"))
    one_kcal = float(g_kcal / 100)
    food = int(der / one_kcal)
    return food

rer = RER(weight)
der = DER(rer)
food = FOOD(der)

print("約" + str(food) + "g")

