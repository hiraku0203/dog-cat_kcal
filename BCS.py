BCS = str()
def animal_bcs(BCS) :

    # 犬か猫か判定
    q1 = int(input("犬なら1、猫なら2を入力: "))

    # 犬🐶
    if q1 == 1 :
        # 肋骨が触れるかどうかで第一段階判断
        rib = int(input("肋骨は触れるか。触れる場合は1を、触れないのなら2を入力: "))

        if rib == 1 :
            # 犬の外観から判断
            look = int(input("肋骨は外観からわかるほどに浮き出ているか。浮き出ているなら1、見えないようなら2を入力: "))

            # 肋骨浮き出るくらい痩せてる
            if look == 1 :
                spine = int(input("脊椎と骨盤も外観からわかり､触っても脂肪がわからないほどに痩せているかどうか。Yesなら1を、Noなら2を入力: "))
                
                if spine == 1 :
                    BCS = "非常にやせ細っています。健康状態や理想体重などの詳しい状態は獣医師に相談して下さい"
                    return BCS
                    
                elif spine == 2 :
                    BCS = "痩せています。理想体重などを獣医師と相談"
                    return BCS

            # そうでもないとき
            elif look == 2 :
                const = int(input("犬を上から見てくびれに注目してください。くびれがはっきりと確認できるのなら1を、すこしある又はあまり見えない場合は2を、全く確認できないなら3を入力: "))
                
                # くびれで判断
                if const == 1 :
                    abdomen = int(input("そのくびれはどの程度か。肋骨あたりからくびれができていて痩せていると感じるのなら1を。肋骨の後ろ、腰のあたりがくびれている場合は2を入力: "))
                    
                    if abdomen == 1 :
                        BCS = "やや瘦せています。理想体重などを獣医師と相談。"
                        return BCS
                    
                    elif abdomen == 2 :
                        BCS = "理想的な体重。おやつのあげすぎなどに注意"
                        return BCS
                
                elif const == 2 :
                    abdomen = int(input("犬を横から見る。そのとき胸からおなかのほうにかけて吊り上がっていっているか。吊り上がっているなら1を、吊り上がっておらず平坦なら2を入力: "))
                    
                    if abdomen == 1 :
                        BCS = "やや肥満気味。適切な運動や食事管理を。おやつのあげすぎには注意"
                        return BCS
                    
                    elif abdomen == 2 :
                        BCS = "肥満気味。適切な運動と食事管理を。おやつはあげたぶんだけ主食をへらす"
                        return BCS

                elif const == 3 :
                    body = int(input("犬を横から見る。そのときむねからおなかのほうにかけて平坦なら1を、脂肪が垂れ下がるくらいなら2を: "))
               
                    if body == 1 :
                        BCS = "肥満気味。適切な運動と食事管理を。おやつはあげたぶんだけ主食をへらす"
                        return BCS

                    elif body == 2 :
                        BCS = "かなりの肥満。適切な運動と食事管理を。本格的なダイエットが必要な場合は獣医師に相談"
                        return BCS

        elif rib == 2 :
            body = int(input("犬を横から見る。そのときむねからおなかのほうにかけて平坦なら1を、脂肪が垂れ下がるくらいなら2を: "))
           
            if body == 1 :
                        BCS = "肥満気味。適切な運動と食事管理を。おやつはあげたぶんだけ主食をへらす"
                        return BCS

            elif body == 2 :
                        BCS = "かなりの肥満。適切な運動と食事管理を。本格的なダイエットが必要な場合は獣医師に相談"
                        return BCS


    # ねこ(=^・・^=)
    elif q1 == 2 :

        # 肋骨を触って判断
        rib_touch = int(input("肋骨は簡単に触れるか。Yes=1,No=2: "))
        
        if rib_touch == 1 :
            
            # 外観で
            rib_look = int(input("肋骨は外から見てわかるか。Yes=1,No=2: "))
        
            if rib_look == 1 :
        
                # くびれで
                consta = int(input("肋骨の後ろ、腰のあたりのくびれは深いか。Yes=1,No=2: "))
        
                if consta == 1 :
        
                    body = int(input("横から見て腹部はかなり吊り上がっているか。Yes=1,No=2: "))
        
                    # 結果
                    if body == 1 :
                        BCS = "かなり痩せている。必要なら獣医師に相談"
                        return BCS
                   
                    elif body  == 2 :
                        BCS = "痩せている。"
                        return BCS
        
                elif consta == 2 :
                    BCS = "やや瘦せている。"
                    return BCS

            # くびれの深さで
            elif rib_look == 2 :
                consta = int(input("腰はわずかにでもくびれているか。Yes=1,No=2: "))
        
                if consta == 1 :
                    body = int(input("横から見て腹部の吊り上がりはどの程度か。深いなら1、浅いなら2: "))

                    # 結果
                    if body == 1 :
                        BCS = "やや痩せている。"
                        return BCS

                    elif body == 2 :
                        BCS = "理想体重。"
                        return BCS
                    
                # おなかの丸さで
                elif consta == 2 :
                    body = int(input("横から見ておなかの丸みはどの程度か。やや丸いなら1、まん丸なら2: "))

                    # 結果
                    if body == 1 :
                        BCS = "やや太っている。"
                        return BCS

                    elif body == 2 :
                        body2 = int(input("脇腹のひだは歩くとどれくらい揺れるか。揺れている程度なら1、盛んに揺れるなら2: "))
                        if body2 == 1 :
                            BCS = "太っている。"
                            return BCS

                        elif body2 == 2 :
                            BCS = "かなり太っている。"
                            return BCS


        # 肋骨が触れなかった場合
        elif rib_touch == 2:
            body2 = int(input("脇腹のひだは歩くとどれくらい揺れるか。揺れている程度なら1、盛んに揺れるなら2: "))
            
            if body2 == 1 :
                BCS = "太っている。"
                return BCS

            elif body2 == 2 :
                BCS = "かなり太っている。"
                return BCS


        
            
bcs = animal_bcs(BCS)

print(bcs)
