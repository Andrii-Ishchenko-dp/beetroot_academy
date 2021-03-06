import time
import random
from dungeon import *

try:
    print('Эта история начинается с подземелья, выберите свой путь.', end='\n')

    while True:
        hero = input('Чтобы выбрать война - нажмите "в", чтобы выбрать мага - "м", разбойника - "р": ')
        if hero != 'в' and hero != 'м' and hero != 'р':
            print('Введите значение в, м или р')
        else:
            break
    if hero == 'в':
        skill={
            'strong': random.randint(6,10),
            'intel': random.randint(2,6),
            'dexterity': random.randint(2,6),
            'attention': random.randint(0,10),
            'flair': random.randint(0,6),
        }
        efficiency = skill['strong'] + skill['intel'] + skill['dexterity'] + skill['flair']
    elif hero == 'м':
        skill = {
            'strong': random.randint(2, 6),
            'intel': random.randint(7, 11),
            'dexterity': random.randint(4, 8),
            'attention': random.randint(0, 10),
            'flair': random.randint(0, 6),
        }
        efficiency = skill['strong'] + skill['intel'] + skill['dexterity'] + skill['flair']
    else:
        skill = {
            'strong': random.randint(4, 8),
            'intel': random.randint(4, 8),
            'dexterity': random.randint(4, 8),
            'flair': random.randint(0, 6),
            'attention': random.randint(0, 10),
        }
        efficiency = skill['strong'] + skill['intel'] + skill['dexterity'] + skill['flair']
    print(f"Ваша сила - {skill['strong']},\n"
          f"Интеллект - {skill['intel']},\n"
          f"Ловкость - {skill['dexterity']},\n"
          f"Удача - {skill['flair']}")
    time.sleep(3)
    print('Вы спускаетесь по тёмным каридорам подземелья, факел в вашей руке отбрасывает причудливые тени на камменные стены.\n'
          '"Эх, сейчас бы найти укромное местечно и отдохнуть", - думаете вы')
    time.sleep(3)
    print('Тоннель перед вами расширяется и вы выходите на небольшую площадку.')
    time.sleep(2)
    print('Перед вами открывается три прохода, два из которых тускло подвечены тлеющими факелами, закреплёнными рядом с входом.')
    time.sleep(3)
    if skill['flair']>5:
        print('Вы ощущаете лёгкий сквозняк из центрального тоннеля')

    print('Слева-направо: 1 - тоннель без факела, 2, 3 -тоннели с факелами. Внешне они никак не отличаются друг от друга.')

    chose1= int(input('Виберите, куда идти дальше: '))

    if chose1 == 3:
        print('Вы выбираете самый правый тоннель. Пройдя метров 10 вы видете, что тоннель обрушен. Тяжёлые глыбы перекрывают вам проход\n'
              'Вы можете попробовать оазобрать обвал или вернуться назад. Что вы выберите?\n'
              '1 - попробовать разобрать завал\n'
              '2 - вернуться обратно')
        chose1_1= int(input('Ваш выбор: '))
        if chose1_1 == 1:
            if hero == 'м':
                print('Не смотря на вашу недюжую силу, все попытки разобрать завал оказались неуспешными. Вам повезло, что ваши\n'
                      'попытки не вызвали больших разрушений. Остаётся только вернуться назад.')
                chose1 = int(input('Виберите, куда идти дальше:\n'
                                   '1 - левый тоннель\n'
                                   '2 - центральный тоннель\n'
                                   'Ваш выбор: '))
            else:
                print('Вы начали неуклюже двигать камни, убрав один из них, вы чувствуете как завал пришёл в движение.\n'
                      'В последний момент вам удаётся отпрыгнуть назад, прежде чем огромный камень упал на то место, \n'
                      'где вы были секунду назад')
                print('Отпрыгнув назад вы неудачно ставите ногу и чувствуете, как при упоре на неё, она отзывается тупой болью')
                print('Вы теряете 2 единицы ловкости')
                skill['dexterity']-=2
                chose1 = int(input('Виберите, куда идти дальше:\n'
                                   '1 - левый тоннель\n'
                                   '2 - центральный тоннель\n'
                                   'Ваш выбор: '))
        else:
            print('Вы возвращаетесь обратно')
            chose1= int(input('Виберите, куда идти дальше:\n'
                                   '1 - левый тоннель\n'
                                   '2 - центральный тоннель\n'
                                   'Ваш выбор: '))

    if chose1 == 1:
        time.sleep(2)
        print('Вы проходите в тоннель и спустя метров 20 начинаете слышать спереди голоса.')
        time.sleep(2)
        print('Это искатели сокровищь, которые пришли, как и вы, за добычей.')
        time.sleep(2)
        print('Как только они вас замечают, начинают атаковать. Они не хотят делить добычу с посторонними.')
        time.sleep(2)
        print('Вы вступаете в бой')
        time.sleep(2)
        enemi_strong = random.randint(12, 20)
        dam= efficiency - enemi_strong
        if dam>=0:
            print(f'Вы оказываетесь сильнее и выходите победителем в этом сражении')
        if dam<0:
            print('В какой-то момент вы понимаете, что зря вступили в бой, но уже поздно. Вы чувствуете, как после очередного\n'
                  'удачного нападения соперника, холодная сталь проходит через ваше тело. Вы падаете замертво.')
            raise TypeError

        time.sleep(2)
        print('Вытирая кровь последнего соперника, со своего клинка вы радуетесь, что в этот раз удача была на вашей стороне.\n'
              'В следующей раз повезти может меньше.')
        time.sleep(2)
        print('Вы продолжаете свой путь по тоннелю...')
    elif chose1 == 2:
        print('Вы проходите в центральный тоннель. Через 10 метров вы замечаете на стенах иероглифы')
        if skill['intel']>=7:
            if hero == 'м':
                time.sleep(2)
                print('Благодаря годам, проведённых в библиотеке университета, вы узнаёте символы, это древний язык одного из народов,\n'
                      'которые исчезли десятилетия назад. На стене написано "Будьте внимательны, остерегайтесь Кейна, он не тот, \n '
                      'за кого себя выдаёт"')
                time.sleep(2)
                print(
                    'Тоннель начинает ухоидить влево, спустя какое-то время, вы понимаете, что он соединяется с левым тоннелем')
            else:

                print('Как-то вы проникли в дом одного из учёных университета в поисках драгоценных камней,\n'
                      ' над которыми те любили ставить опыты, но камней вы не нашли, но ваше внимание привлекла книжка на полке.')
                time.sleep(2)
                print('Переплёт книги был истрёпаный, по общему состаянию можно было предположить, что книга очень древняя и,\n '
                      'возможно, ценная.')
                time.sleep(2)
                print('Вы решили прихватить её с собой. Книга называлась "Языки исчезнувших народов".\n'
                      ' На досуге вы просматривали необычные иероглифы на страницах и вам запомнился один из них.')
                print('Именно он сейчас начинал строку символов на стене. Иероглиф означал "Будьте внимательны"')
                time.sleep(2)
                print('Тоннель начинает ухоидить влево, спустя какое-то время, вы понимаете, что он соединяется с левым тоннелем')
        else:
            print('К сожалению, ваших знаний недостаточно для того, чтобы понять, что означают символы. С чувством, что вы \n'
                  'упустили что-то важное, вы продолжаете идти вперёд...')
            time.sleep(2)
            print('Тоннель начинает ухоидить влево, спустя какое-то время, вы понимаете, что он соединяется с левым тоннелем')
    print('Продвигаясь по тоннелю, вы замечаете, что стены и потолок начинают вас сдавливать.\n'
          'Приступ клоустрофобии или проход действительно становится меньше?')
    time.sleep(2)
    print('Про себя вы думаете "Хорошо что на мне не тяжёлые латы, иначе бы застрял"')
    if skill['flair']<=3:
        print('Не заметив камень вы спотыкаетесь и больно ударяетесь о выступающий край стены тоннеля')
        time.sleep(2)
        print('Колено начинает ныть и вы теряете 1 единицу ловкости')
        skill['dexterity'] -= 1
    print('Тоннель начинает уходить вниз под большим углом')
    time.sleep(3)
    print('Пока вы шагаете по тоннелю, в голове у вас проносятся мысль о то, какая же награда вас ждёт, когда вы выберетесь на поверхность')
    time.sleep(3)
    print('Местный глава совета пообещал вам немалую сумму за уничтожение твари, которая охотится на шахтёров, которые\n'
          'добывают руду неподалёку')
    time.sleep(3)
    print('Осмотр места последнего нападения дал вам понять несколько вещей: Во-первых, тварь с неимоверной жестокостью \n'
          'рассправляется со своими жертвами, это не похоже на охоту ради пропитания. Во-вторых, вы не находите следов животных\n'
          'что указывает на то, что или же чудовчище или умеет здорово заметать следы, или оставляет их, но отличить от человеческих\n'
          'их не получается.')
    time.sleep(3)
    print('Именно поэтому, первое место, куда вы отправили на охоту за чудовищем, стало подземелье неподалёку. Скорее всего,\n'
          'тварь, напавшая на работяг, живёт в сети этих пищер, которые тянутся на сотни метров в разные стороны и использует\n'
          'ответвления пещеры, которые находятся не глубоко под землёй, для внезапного нападения.')
    time.sleep(3)
    print('Погрузившись в размышения, вы и не заметили, как тоннель закончился старинной дверью')
    time.sleep(2)
    print('При попытке открыть её, вы потерпели неудачу')
    if skill['strong']>=10:
        print('Оценив, свои силы, вы подумали, что можете попробовать проломить дверь с небольшого разгона')
        print('Это наделает шума, но преграды на пути у вас больше не будет')
        chose2 = input('Попробовать пробить дверь плечём - 1\n'
                       'Ничего не делать - 2\n'
                       'Ваш выбор: ')
        if chose2 == 1:
            print('Вы берёте разгон и со всей силы тараните плечём дверь')
            print('Дверь издаёт глухой звук при ударе, но не поддаётся')
    print('Осмотрев дверь, вы замещаете надпись на стене справа, в ней не хватает последнего слова, которое рассыпалось по \n'
          'буквам и лежит у вас под ногами.')
    value = random.randint(1,6)
    if value ==1:
        word = 'Храбрость'
    elif value ==2:
        word = 'Мужество'
    elif value == 3:
        word = 'Стойкость'
    elif value == 4:
        word = 'Отвага'
    elif value == 5:
        word = 'Благородство'
    elif value == 6:
        word = 'Бесстрашие'
    #1 - Храбрость
    #2 - Мужество
    #3- Стойкость
    #4 - Отвага
    #5 - Благородство
    #6 - Бесстрашие
    if skill['intel']>=6:
        print('Вам знаком язык текста, написанного на стене. Чтобы понять о чём именно говорится, ваших знаний недостаточно, \n'
              'но из котекста вы понимаете, что речь идёт о каком-то качестве героя. Какими качествами обладают герои?')
    x=random.sample(word, k=len(word))
    string=''.join(x)
    set(string)
    print(f'Собрав все буквы в руки, вы получили следующее:{string}')
    time.sleep(2)
    print('Теперь вам нужно из полученных букв составить слово')
    while True:
        word_ans=input('Введите слово: ')
        if word_ans ==word:
            print('Дверь открывается и вы проходите внутрь')
            time.sleep(3)
            break
        else:
            print('Вы вставляете буквы в пазы, вы слышите, как за стенами начинают крутиться шестерёнки и уже в следующее\n'
                  'мгновение пол под вами раздвигается и вы падаете в бездну')
            raise TypeError
    number_of_rooms = random.randint(3,5)
    dungeons = [1, 2, 4, 5, 6, 3]

    for i in range(1, number_of_rooms + 1):
        random.shuffle(dungeons)
        dung_chouse = dungeons.pop()
        if dung_chouse == 1:
            dungeon1(skill, efficiency, hero)
        elif dung_chouse == 2:
            dungeon2(skill, efficiency, hero)
        elif dung_chouse == 3:
            dungeon3(skill, efficiency, hero)
        elif dung_chouse == 4:
            dungeon4(skill, efficiency, hero)
        elif dung_chouse == 5:
            dungeon5(skill, efficiency, hero)
        elif dung_chouse == 6:
            dungeon6(skill, efficiency, hero)
        elif dung_chouse == 7:
            dungeon7(skill, efficiency, hero)
        elif dung_chouse == 8:
            dungeon8(skill, efficiency, hero)
        elif dung_chouse == 9:
            dungeon9(skill, efficiency, hero)
        elif dung_chouse == 10:
            dungeon10(skill, efficiency, hero)
        time.sleep(3)
    final_room1(skill, efficiency, hero)
except TypeError as err_msg:
    print('Ваше преключение закончилось')
