import time
import random


print('Эта история начинает с подземелья, выберите свой путь.', end='\n')

while True:
    hero = input('Чтобы выбрать война - нажмите "в", чтобы выбрать мага - "м", разбойника - "р": ')
    if hero != 'в' and hero != 'м' and hero != 'р':
        print('Введите значение в, м или р')
    else:
        break

if hero == 'в':
    skill={
        'strong': random.randint(7,11),
        'intel': random.randint(2,6),
        'dexterity': random.randint(4,8),
        'flair': random.randint(0,8),
        'health': 20
    }
elif hero == 'м':
    skill = {
        'strong': random.randint(2, 6),
        'intel': random.randint(7, 11),
        'dexterity': random.randint(4, 8),
        'flair': random.randint(0, 8),
        'health': 12
    }
else:
    skill = {
        'strong': random.randint(4, 10),
        'intel': random.randint(4, 10),
        'dexterity': random.randint(4, 10),
        'flair': random.randint(0, 8),
        'health': 16
    }

print('Вы спускаетесь по тёмным каридорам подземелья, факел в вашей руке отбрасывает причудливые тени на камменные стены.\n '
      '"Эх, сейчас бы найти укромное местечно и отдохнуть", - думаете вы')
time.sleep(2)
print('Тоннель перед вами расширяется и вы выходите на небольшую площадку.')
time.sleep(2)
print('Перед вами открывается три прохода, два из которых тускло подвечены тлеющими факелами, закреплёнными рядом с входом.')
time.sleep(2)
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
                  'попытки не выззвали больших разрушений. Остаётся только вернуться назад.')
            chose1 = int(input('Виберите, куда идти дальше:\n'
                               '1 - левый тоннель\n'
                               '2 - центральный тоннель '))
        else:
            print('Вы начали неуклюже двигать камни, убрав один из них, вы чувствуете как завал пришёл в движение.\n'
                  'В последний момент вам удаётся отпрыгнуть назад, прежде чем огромный камень упал на то место, \n'
                  'где вы были секунду назад')
            print('Отпрыгнув назад вы неудачно ставите ногу и чувствуете, как при упоре на неё, она отзывается тупой болью')
            print('Вы теряете 2 здоровья')
            skill['health']-=2
            chose1 = int(input('Виберите, куда идти дальше:\n'
                               '1 - левый тоннель\n'
                               '2 - центральный тоннель '))
    else:
        print('Вы возвращаетесь обратно')
        chose1= int(input('Виберите, куда идти дальше:\n'
                               '1 - левый тоннель\n'
                               '2 - центральный тоннель '))

if chose1 == 1:
    time.sleep(2)
    print('Вы проходите в тоннель и спустя метров 20 начинаете слышать спереди голоса.\n '
'Это искатели сокровищь, которые пришли, как и вы, за добычей.\n '
'Как только они вас замечают, начинают атаковать. Они не хотят делить добычу с посторонними.')
    print('Проверка силы')
    time.sleep(2)
    enemi_strong = random.randint(3, 6)
    dam=skill['strong']-enemi_strong
    if dam>0:
        skill['health']= skill['health']-dam
        print(f'Бандиты нанесли вам {dam} урона, у вас оставлось {skill["health"]} здоровья')
    if skill['health'] <=0:
        print('Ваше преключение окончено, вы умерли')
    if dam<=0:
        print('Противники не наносят вам урона, вы мастерски разделываетесь с ними')
    time.sleep(2)
    print('Вы вытираете кровь последнего соперника со своего клинка и радуетесь, что в этот раз удача была на вашей стороне.\n '
          'В следующей раз повезти может меньше.')
    time.sleep(2)
    print('Вы продолжаете свой путь по тоннелю...')
elif chose1 == 2:
    print('Вы проходите в центральный тоннель. Через 10 метров вы замечаете на стенах иероглифы')
    if skill['intel']>=7:
        if hero == 'м':
            time.sleep(2)
            print('Благодаря годам, проведённых в библиотеке университета, вы узнаёте символы, это древний язык одного из народов,\n'
                  'которые исчезли десятилетия назад. На стене написано "Будьте внимательны, остерегайтесь Фавна, он не тот, \n '
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
    print('Колено начинает ныть и вы теряете 1 единицу здоровья')
    skill['health'] -= 1
print('Тоннель начинает уходить вниз под большим углом')
print('Пока вы шагаете по тоннелю, в голове у вас проносятся мысль о то, какая же награда вас ждёт, когда вы выберетесь на поверхность')
print('Местный глава совета пообещал вам немалую сумму за уничтожение твари, которая охотится на шахтёров, которые\n'
      'добывают руду неподалёку')
print('Осмотр места последнего нападения дал вам понять несколько вещей: Во-первых, тварь с неимоверной жестокостью \n'
      'рассправляется со своими жертвами, это не похоже на охоту ради пропитания. Во-вторых, неподалёку от места преступления\n'
      'вы нашли нору, изучив которую, вы поняли, что тварь вылазит из под земли')
print('Именно поэтому, первое место, куда вы отправили на охоту за чудовищем, стало подземелье неподалёку. Скорее всего, \n'
      'тварь, напавшая на работяг, живёт в сети этих пищер, которые тянутся на сотни метров в разные стороны и использует\n'
      ' ответвления пещеры, которые находятся не глубоко под землёй, для внезапного нападения.')
print('Погрузившись в размышения, вы и не заметили, как тоннель закончился старинной дверью')
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
value = random.randint(1,5)
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
#1-Храбрость
#2-Мужество
#3- Стойкость
#4 - Отвага
#5 - Благородство
if skill['intel']>=6:
    print('Вам знаком язык текста, написанного на стене. Чтобы понять о чём именно говорится, ваших знаний недостаточно, \n'
          'но из котекста вы понимаете, что речь идёт о каком-то качестве героя. Какими качествами обладают герои?')
x=random.sample(word, k=len(word))
string=''.join(x)
tuple(string)
print(f'Собрав все буквы в руки, вы получили следующее:{string}')
print('Теперь вам нужно из полученных букв составить слово')
while True:
    word_ans=input('Введите слово: ')
    if word_ans ==word:
        print('Дверь открывается и вы проходите внутрь')
        break
    else:
        print('Вы вставляете буквы в пазы, но они выпадают. Это слово не подходит, нужно подумать ещё...')


