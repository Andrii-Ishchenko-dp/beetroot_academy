import random
import time

def dungeon1(skill, efficiency, hero):
    print('Вы открываете дверь в комнату, осторожно продвигаетесь вглубь. Освещая факелом пространство вокруг, вы стараетесь\n'
          'понять размеры помещения. ')
    time.sleep(2)
    print('Воздух пропитан запахом смерти и разложившейся плоти.\n'
          '"Не к добру это" - пронеслась мысль в голове')
    time.sleep(2)
    print('Выйдя на середину комнаты, при этом не встретя никакого сопративления, вы начинаете думать, что комната пустая')
    time.sleep(4)
    print('И именно в этот момент вы слышите тяжёлое дыхание впереди')
    time.sleep(2)
    print('Существо напало внезамно, вы в последний момент увернулись от его острых, как бритва, когтей')
    monster_power1 = 50
    if skill['intel'] > 5:
        print(f"Вы оцениваете силу монстра, она равна {monster_power1}, ваша боевая эффективность равна {efficiency}")
    while True:
        chouse1_d1 = int(input('Что будете делать?\n'
                           'Нападать - 1\n'
                           'Сбежать - 2 \n'
                           'Ваш выбор: '))
        if chouse1_d1 == 1:
            time.sleep(2)
            print('Вы нападаете на монстра')
            if efficiency >= monster_power1:
                if hero == 'в':
                    time.sleep(2)
                    print('Вы наносите сокрушительный удар, который убивает монстра. Вытирая кровь с клинка вы радуетесь победе')
                    time.sleep(2)
                    print('Обыскав комнату тщательнее вы находите у углу меч. Вытащив из ножен, вы удивляетесь качеству\n'
                          'стали. "Мечи такого качества достойны королей" - думаете вы и меняете свой меч на "королевский"')
                    time.sleep(2)
                    return skill['strong'] + 1
                if hero == 'м':
                    print('Вы пускаете огненный шар, который оставляет после монстра только горству пепла.\n'
                          'Сбив огонь с руковов, вы радуетесь победе')
                    time.sleep(2)
                    print('Обыскав комнату тщательнее вы находите волшебный посох. Поднимая его, вы чувствуете\n'
                          'магическую энергию, которая исходит от него. Подумав, вы решаете взять его с собой.')
                    time.sleep(2)
                    return skill['strong'] + 1
                if hero == 'р':
                    print('Увернувшись от атаки чудовища, вы замечаете уязвимое место. \n'
                          'Воспользовавшись моментом вы наносите смертельный удар чудовищу. Вытирая кровь с кинжалов,\n'
                          'вы радуетесь победе')
                    time.sleep(2)
                    print('Обыскав комнату тщательнее вы находите старый труп. В руках у мертвеца зажаты кинжалы. Хорошо\n'
                          'осветив их факелами, вы понимаете, что на лезвиях написаны какие-то руны. Вы решаете взять их с собой.')
                    time.sleep(2)
                    return skill['strong'] + 1
            else:
                print('Ваша атака не достигает цели')
                time.sleep(2)
                while True:
                    print('Монстр делает молниеносный выпад')
                    time.sleep(2)
                    if skill['dexterity'] > 4:
                        print('У вас получается увернуться от атаки')
                        time.sleep(2)
                        skill['dexterity'] -=1
                        lucky_Strike = random.randint(0,10)
                        if lucky_Strike > skill['flair']:
                            print('Вы проводите контратаку и убиваете монстра')
                            time.sleep(2)
                            if hero == 'в':
                                print(
                                    'Обыскав комнату тщательнее вы находите у углу меч. Вытащив из ножен, вы удивляетесь качеству\n'
                                    'стали. "Мечи такого качества достойны королей" - думаете вы и меняете свой меч на "королевский"')

                                return skill['strong'] + 1
                            if hero == 'м':
                                print(
                                    'Обыскав комнату тщательнее вы находите волшебный посох. Поднимая его, вы чувствуете\n'
                                    'магическую энергию, которая исходит от него. Подумав, вы решаете взять его с собой.')
                                return skill['strong'] + 1
                            if hero == 'р':
                                print(
                                    'Обыскав комнату тщательнее вы находите старый труп. В руках у мертвеца зажаты кинжалы. Хорошо\n'
                                    'осветив их факелами, вы понимаете, что на лезвиях написаны какие-то руны. Вы решаете взять их с собой.')
                                return skill['strong'] + 1
                    else:
                        print('Вы даже не успеваете заметить, как чудовище хвостом пронзает вас. Вы падаете замертво.')
                        return TypeError

        else:
            print('Оценив шансы на победу против чудовища вы решаете сбежать, может, в следующей комнате повезёт больше')
            time.sleep(2)
            if skill['dexterity']<=4:
                print('Вам не хватает всего пару секунд, чтобы добежать до заветной двери. Чудовище хвостом пронзает вас.\n'
                      'Вы падаете замертво.')
                return TypeError
            else:
                print('Вы выбигаете из комнаты и плотно закрываете за собой дверь. Ещё бы чуть- чуть и монстр бы вас схватил')
                return None

    # Идея в том, чтобы создать много разных сбалансированных подземелий и подставлять их в случайном порядке.
    # Задача путешествия в том, чтобы убить одного конкретного монстра, но по пути к нему могут попадаться другие

def dungeon2(skill, efficiency, hero):
    return None
