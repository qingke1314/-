from goto import with_goto
from random import *
from time import *

key0 = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
k0 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
zi = list(zip(key0, k0))
summ = 0
shunzitap = 0
tonghuatap = 0
pattern0 = ['#', '*', '&', '$']
three10 = ["*0 &0 $0", "#0 &0 $0", "#0 *0 $0", "#0 *0 &0"]
shunzi1 = ['23456', '34567', '45678', '56789', '67890', '7890J', '890JQ', '90JQK', '0JQKA']
shunzi2 = ['234', '345', '456', '567', '678', '789', '890', '90J', '0JQ', 'JQK', 'QKA']
zhadan = ["#2 *2 &2 $2", "#3 *3 &3 $3", "#4 *4 &4 $4", "#5 *5 &5 $5", "#6 *6 &6 $6", "#7 *7 &7 $7",
          "#8 *8 &8 $8", "#9 *9 &9 $9", "#0 *0 &0 $0", "#J *J &J $J", "#Q *Q &Q $Q", "#K *K &K $K", "#A *A &A $A"]
ju = [-1, -2, -3, -4]
bu = [-1, -4, -7, -10, -13]  # 用于比较两个同花/顺子大小
iu = [8, 7, 6, 5, 4, 3, 2, 1, 0]  # 顺子索引
qu = [3, 2, 1, 0]
su = [12, 11, 10, 9, 8, 7, 6, 5, 4]
aa = [[], [], [], []]
n3 = 0
n2 = 0
tonghuas = []  # 同花仓库
shunzis = []  # 顺子仓库
santiaos = []  # 三条仓库
pairss = []  # 对子仓库
get1 = []  # 前墩仓库
get2 = []  # 中墩仓库
get3 = []  # 后墩仓库
sin = [['#2', '*2', '&2', '$2'],
       ['#3', '*3', '&3', '$3'],
       ['#4', '*4', '&4', '$4'],
       ['#5', '*5', '&5', '$5'],
       ['#6', '*6', '&6', '$6'],
       ['#7', '*7', '&7', '$7'],
       ['#8', '*8', '&8', '$8'],
       ['#9', '*9', '&9', '$9'],
       ['#0', '*0', '&0', '$0'],
       ['#J', '*J', '&J', '$J'],
       ['#Q', '*Q', '&Q', '$Q'],
       ['#K', '*K', '&K', '$K'],
       ['#A', '*A', '&A', '$A']]

All = [[0, 0, 0, 0],  # 2
       [0, 0, 0, 0],  # 3
       [0, 0, 0, 0],  # 4
       [0, 0, 0, 0],  # 5
       [0, 0, 0, 0],  # 6
       [0, 0, 0, 0],  # 7
       [0, 0, 0, 0],  # 8
       [0, 0, 0, 0],  # 9
       [0, 0, 0, 0],  # 10
       [0, 0, 0, 0],  # J
       [0, 0, 0, 0],  # Q
       [0, 0, 0, 0],  # K
       [0, 0, 0, 0]]  # A
#     # * & $
cos = list(map(list, zip(*sin)))  # 转置
Bll = list(map(list, zip(*All)))


class AllCard:
    def __init__(self, cards):
        self.cards = cards
        self.end = 0
        self.step = 0
        self.remacards = ""  # 剩余牌
        self.cardss = []
        self.cardsss = []
        self.keylist = []
        self.keylistt = []
        self.keycount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.patternlist = []
        self.patternlistt = []
        self.patterncount = [0, 0, 0, 0]
        self.first = []
        self.middle = []
        self.final = []
    def change0(self):  # 对牌转值
        self.cardss = self.cards.split(" ")
        global sin, cos, All, Bll
        All = [[0, 0, 0, 0],  # 2
               [0, 0, 0, 0],  # 3
               [0, 0, 0, 0],  # 4
               [0, 0, 0, 0],  # 5
               [0, 0, 0, 0],  # 6
               [0, 0, 0, 0],  # 7
               [0, 0, 0, 0],  # 8
               [0, 0, 0, 0],  # 9
               [0, 0, 0, 0],  # 10
               [0, 0, 0, 0],  # J
               [0, 0, 0, 0],  # Q
               [0, 0, 0, 0],  # K
               [0, 0, 0, 0]]  # A
        #     # * & $
        Bll = list(map(list, zip(*All)))
        self.patternlist = []
        self.keylist = []
        self.patternlistt = []
        self.keylistt = []
        for i in range(13):
            for j in range(4):
                if sin[i][j] in self.cardss:
                    All[i][j] = 1
                else:
                    All[i][j] = 0
                if cos[j][i] in self.cardss:
                    Bll[j][i] = 1
                else:
                    Bll[j][i] = 0
        self.cardss = []  # 牌值排列
        self.cardsss = []  # 花型分组
        for i in range(13):
            self.keycount[i] = 0
        for i in range(4):
            self.patterncount[i] = 0
        for i in range(13):
            for j in range(4):
                if All[i][j] == 1:
                    self.keycount[i] += 1
                    self.patterncount[j] += 1
                    self.cardss.append(sin[i][j])
        for j in range(4):
            for i in range(13):
                if Bll[j][i] == 1:
                    self.cardsss.append(cos[j][i])
        for nu in self.cardss:
            pa = list(nu)
            self.patternlist.append(pa.pop(0))
            self.keylist.append(pa.pop())
        for nu in self.cardsss:
            pa = list(nu)
            self.patternlistt.append(pa.pop(0))
            self.keylistt.append(pa.pop())
    def change(self):
        global get1, get2, get3
        if self.end == 0:
            self.change0()
            self.end = 1
            return
        else:  # 对值转牌
            self.first = self.first.replace('0', 'x')
            self.first = self.first.replace('x', '10')
            self.middle = self.middle.replace('0', 'x')
            self.middle = self.middle.replace('x', '10')
            self.final = self.final.replace('0', 'x')
            self.final = self.final.replace('x', '10')
            self.end = 0
    def dododo(self):  # 按序摆牌
        global get1, get2, get3
        for i in range(3):
            get1.append(self.patternlist[i])
            get1.append(self.keylist[i])
            if i < 2:
                get1.append(" ")
        for i in range(3, 8):
            get2.append(self.patternlist[i])
            get2.append(self.keylist[i])
            if i < 7:
                get2.append(" ")
        for i in range(8, 13):
            get3.append(self.patternlist[i])
            get3.append(self.keylist[i])
            if i < 12:
                get3.append(" ")
        get3 = ''.join(get3)
        get2 = ''.join(get2)
        get1 = ''.join(get1)
    def SpecialCards1_2(self):  # 至尊清龙/一条龙
        # print("进入:至尊清龙/一条龙")
        global get1, get2, get3, All
        s1 = 1
        s2 = 1
        for a in self.keycount:
            if a != 1:
                s1 = 0
                break
        for i in range(4):
            if self.patterncount[i] == 13:
                s2 = 0
                break
        if s1 == 1:
            self.dododo()
            if s2 == 1:
                zhon = 0
                ho = 0
                for i in range(4):
                    zhong = All[3][i] + All[4][i] + All[5][i] + All[6][i] + All[7][i]
                    hou = All[8][i] + All[9][i] + All[10][i] + All[11][i] + All[12][i]
                    if zhong == 5:
                        zhon = 1
                    if hou == 5:
                        ho = 1
                if ho == 1:
                    pass
                else:
                    if zhon == 1:
                        huan = get3
                        get3 = get2
                        get2 = huan
                    else:
                        pass
            self.step = 3
    def SpecialCards3(self):  # 十二皇族
        # print("进入:十二皇族")
        global get1, get2, get3
        if (self.keycount[-1] + self.keycount[-2] +
            self.keycount[-3] + self.keycount[-4]) >= 12:
            for g in ju:
                if self.keycount[g] == 4:
                    ind = self.keylist.index(key0[g])
                    an = self.keylist[ind:ind + 4]
                    anp = self.patternlist[ind:ind + 4]
                    del self.keylist[ind:ind + 4]
                    del self.patternlist[ind:ind + 4]
                    self.keylist.extend(an)
                    self.patternlist.extend(anp)
                    break
            self.dododo()
            self.step = 3
    @with_goto
    def tonghuashun(self):  # 找同花顺
        # print("进入：找同花顺")
        global get1, get2, get3, aa, qu
        q = 0
        ba = 0
        aa = [[], [], [], []]
        sn = [[], []]
        self.change0()
        for i in range(13):  # 按花型分组
            if self.patternlist[i] == "#":
                aa[0].append(self.keylist[i])
            elif self.patternlist[i] == "*":
                aa[1].append(self.keylist[i])
            elif self.patternlist[i] == "&":
                aa[2].append(self.keylist[i])
            elif self.patternlist[i] == "$":
                aa[3].append(self.keylist[i])
        label.begin
        for i in qu:
            aaa = ''.join(aa[i])
            n = len(aaa)
            if n >= 5:
                shunzi = shunzi1
                shunzi.reverse()
                for gp in shunzi:
                    q = aaa.find(gp)
                    if q != -1:
                        for j in range(5):
                            sn[ba].append(pattern0[i])
                            sn[ba].append(aaa[q + j])
                            sn[ba].append(" ")
                            aa[i].remove(aaa[q + j])
                        sn[ba] = ''.join(sn[ba])
                        sn[ba] = sn[ba].strip()
                        ba += 1
                        goto.begin
        goto.end

        label.end
        sos = ""
        for j in range(4):
            n = len(aa[j])
            if n > 0:
                for l in range(n):
                    sos += pattern0[j] + aa[j][l] + " "
        self.remacards = sos.strip(" ")
        if ba == 1:
            get3 = sn.pop(0)
            self.step = 1
        elif ba == 2:
            get3 = sn.pop(0)
            get2 = sn.pop()
            get1 = self.remacards
            self.remacards = ""
            self.step = 3
            for x in range(13):
                if get2[-1] == zi[x][0]:
                    for y in range(13):
                        if get3[-1] == zi[y][0]:
                            if zi[x][1] > zi[y][1]:
                                turn = get3
                                get3 = get2
                                get2 = turn
    @with_goto
    def Bomb(self):  # 找炸弹
        # print("进入:找炸弹")
        r = 0
        sa = []
        self.cards = self.remacards
        self.change0()
        # 剩余的牌按牌值排列
        self.remacards = ""
        n = len(self.keylist)
        for i in range(n):
            self.remacards += self.patternlist[i] + self.keylist[i]
            if i < n - 1:
                self.remacards += " "
        global get1, get2, get3, su, qu, zhadan
        label.begin
        for i in su + qu:
            if self.keycount[i] == 4:  # 找到炸弹
                sa.append(zhadan[i])
                self.remacards = self.remacards.replace(zhadan[i], "")
                self.remacards = self.remacards.replace("  ", " ")
                self.remacards = self.remacards.strip(" ")
                self.keycount[i] = 0

        r += 1
        if r < 3:
            goto.begin
        else:
            goto.end
        label.end

        n = len(sa)
        if self.step == 0:
            if n == 0:
                pass
            elif n == 1:
                get3 = sa[0]
                self.step = 1
            elif n == 2:
                get3 = sa[0]
                get2 = sa[1]
                self.step = 2
            else:
                get3 = sa[0]
                get2 = sa[1]
                get1 = sa[2][:8]
                get3 += " " + sa[2][9:]
                get2 += " " + self.remacards
                self.remacards = []
                self.step = 3
        elif self.step == 1:
            if n == 0:
                pass
            elif n == 1:
                get2 = sa[0]
                self.step = 2
            else:
                get2 = sa[0]
                get1 = sa[1][:8]
                get2 += " " + sa[1][9:]
                self.step = 3
        return
    def santiao(self):  # 找三条
        # print("#找三条")
        global All, sin, su, qu, n3, three10, santiaos
        santiaos = []
        self.cards = self.remacards
        self.change0()
        for we in su + qu:
            six = ""
            if self.keycount[we] == 3:
                for i in range(4):
                    if All[we][i] == 1:
                        six += sin[we][i] + " "
                six = six.strip()
                santiaos.append(six)
            self.remacards = self.remacards.replace(six, "")
            self.remacards = self.remacards.replace("  ", " ")
            self.remacards = self.remacards.strip(" ")
        n3 = len(santiaos)
    def pairs(self):  # 找对子
        # print("找对子!!!")
        global All, sin, su, qu, n2, pairss
        pairss = []
        self.cards = self.remacards
        self.change0()
        for we in su + qu:
            six = ""
            if self.keycount[we] == 2:
                for i in range(4):
                    if All[we][i] == 1:
                        six += sin[we][i] + " "
                six = six.strip()
                pairss.append(six)
            self.remacards = self.remacards.replace(six, "")
            self.remacards = self.remacards.replace("  ", " ")
            self.remacards = self.remacards.strip(" ")
        n2 = len(pairss)
    def gourd(self):  # 找葫芦
        # print("找葫芦！！！")
        global n3, n2, santiaos, pairss, get1, get2, get3
        self.santiao()
        self.pairs()
        get3 = ''.join(get3)
        get2 = ''.join(get2)
        get1 = ''.join(get1)
        if self.step == 0:
            if n3 == 0:
                pass
            elif n3 == 1:
                if n2 == 0:
                    pass
                elif n2 >= 1:
                    get3 = santiaos.pop() + " " + pairss.pop()
                    self.step = 1
            elif n3 == 2:
                if n2 == 0:
                    pass
                elif n2 == 1:
                    get3 = santiaos.pop(0) + " " + pairss.pop()
                    self.step = 1
                elif n2 >= 2:
                    get3 = santiaos.pop(0) + " " + pairss.pop()
                    get2 = santiaos.pop() + " " + pairss.pop()
                    if n2 == 2:
                        get1 = self.remacards
                    else:
                        get1 = pairss.pop() + " " + self.remacards
                    self.remacards = ""
                    self.step = 3
            elif n3 == 3:
                if n2 == 0:
                    zai = santiaos.pop().split()
                    get3 = santiaos.pop(0)
                    get3 += " " + zai.pop()
                    get3 += " " + zai.pop()
                    self.remacards += " " + zai.pop()
                    self.step = 1
                elif n2 == 1:
                    get3 = santiaos.pop(0) + " " + pairss.pop()
                    get2 = santiaos.pop(0) + " " + self.remacards
                    get1 = santiaos.pop()
                    self.step = 3
                else:
                    get3 = santiaos.pop(0) + " " + pairss.pop(0)
                    get2 = santiaos.pop(0) + " " + pairss.pop()
                    get1 = santiaos.pop()
                    self.step = 3
            else:
                zai = santiaos.pop().split()
                get3 = santiaos.pop(0)
                get3 += " " + zai.pop()
                get3 += " " + zai.pop()
                get2 = santiaos.pop(0)
                get2 += " " + zai.pop() + " " + self.remacards
                get1 = santiaos.pop()
                self.step = 3
        elif self.step == 1:
            if n3 == 0:
                pass
            elif n3 == 1:
                if n2 == 0:
                    pass
                elif n2 == 1:
                    get2 = santiaos.pop() + " " + pairss.pop()
                    if len(get3) == 14:
                        get1 = self.remacards
                    else:
                        get3 += " " + self.remacards[:2]
                        get1 = self.remacards[3:]
                    self.step = 3
                else:
                    get2 = santiaos.pop() + " " + pairss.pop()
                    if len(get3) == 14:
                        get1 = pairss.pop() + " " + self.remacards
                    else:
                        get3 += " " + self.remacards[:2]
                        get1 = pairss.pop() + self.remacards[2:]
                    self.step = 3
            else:
                if n2 == 0:
                    zai = santiaos.pop().split()
                    get2 = santiaos.pop()
                    get2 += " " + zai.pop(0)
                    get2 += " " + zai.pop(0)
                    if len(get3) == 14:
                        get1 = zai.pop() + " " + self.remacards
                    else:
                        get3 += " " + zai.pop()
                        get1 = self.remacards
                    self.step = 3
                else:
                    get2 = santiaos.pop(0) + " " + pairss.pop()
                    get1 = santiaos.pop()
                    if len(get3) < 14:
                        get3 += " " + self.remacards
                    self.step = 3
        else:
            if n3 == 0:
                if n2 == 0:
                    if len(get3) < 14:
                        get3 += " " + self.remacards[:2]
                        get2 += self.remacards[2:5]
                        get1 = self.remacards[6:]
                        self.step = 3
                    else:
                        get2 += " " + self.remacards[:2]
                        get1 = self.remacards[3:]
                        self.step = 3
                elif n2 == 1:
                    if len(get3) < 14:
                        get3 += " " + self.remacards[:2]
                        get2 += self.remacards[2:5]
                        get1 = pairss.pop() + " " + self.remacards[6:]
                        self.step = 3
                    else:
                        get2 += " " + self.remacards[:2]
                        get1 = pairss.pop() + " " + self.remacards[3:]
                        self.step = 3
                else:
                    if len(get3) < 14:
                        zai = pairss.pop().split()
                        get3 += " " + zai.pop()
                        get2 += " " + zai.pop()
                        get1 = pairss.pop() + " " + self.remacards
                        self.step = 3
                    else:
                        zai = pairss.pop().split()
                        get2 += " " + zai.pop()
                        get1 = pairss.pop() + " " + zai.pop()
                        self.step = 3
            else:
                if n2 == 1:
                    zai = pairss.pop().split()
                    get2 += " " + zai.pop()
                    get3 += " " + zai.pop()
                    get1 = santiaos.pop()
                    self.step = 3
                else:
                    if len(get3) == 14:
                        get2 += " " + self.remacards
                        get1 = santiaos.pop()
                    else:
                        get3 += " " + self.remacards[:2]
                        get2 += self.remacards[2:]
                        get1 = santiaos.pop()
                        self.step = 3
        get3 = ''.join(get3)
        get2 = ''.join(get2)
        get1 = ''.join(get1)
        n3 = len(santiaos)
        n2 = len(pairss)
        # 最后剩余牌的回收
        ad = []
        if n3 > 0:
            for i in range(n3):
                ad.append(" ")
                ad.append(santiaos.pop())
            ad = ''.join(ad)
            self.remacards += ad
        ad = []
        if n2 > 0:
            for i in range(n2):
                ad.append(" ")
                ad.append(pairss.pop())
            ad = ''.join(ad)
            self.remacards += ad
    def tonghua(self):  # 找同花
        # print("找同花！！！")
        global k0, key0, get1, get2, get3, aa, bu, tonghuas, tonghuatap, pattern0
        aa = [[], [], [], []]
        self.cards = self.remacards
        self.change0()
        m = len(self.patternlist)
        for i in range(m):  # 按花型分组
            if self.patternlist[i] == "#":
                aa[0].append(self.keylist[i])
            elif self.patternlist[i] == "*":
                aa[1].append(self.keylist[i])
            elif self.patternlist[i] == "&":
                aa[2].append(self.keylist[i])
            elif self.patternlist[i] == "$":
                aa[3].append(self.keylist[i])
        sss = []
        for j in range(4):
            n = len(aa[j])
            sss = []
            if n in range(5, 10):
                sss = []
                for x in range(5):
                    sss.append(aa[j].pop())
                    sss.append(pattern0[j])
                    sss.append(" ")
                sss.pop()
                sss.reverse()
                tonghuas.append(''.join(sss))
            elif n in range(10, 12):
                sss = []
                for x in range(5):
                    sss.append(aa[j].pop())
                    sss.append(pattern0[j])
                    sss.append(" ")
                sss.pop()
                sss.reverse()
                tonghuas.append(''.join(sss))
                sss = []
                for x in range(5):
                    sss.append(aa[j].pop())
                    sss.append(pattern0[j])
                    sss.append(" ")
                sss.pop()
                sss.reverse()
                tonghuas.append(''.join(sss))

        # 回收剩余牌
        huis = []
        for k in range(4):
            h = len(aa[k])
            if h > 0:
                for o in range(h):
                    huis.append(aa[k].pop())
                    huis.append(pattern0[k])
                    huis.append(" ")
        huis.pop()
        huis.reverse()
        huis = ''.join(huis)
        self.remacards = huis
        n = len(tonghuas)
        if n == 0:
            pass
        elif n == 1:
            if self.step == 0:
                get3 = tonghuas.pop()
                tonghuatap = 1
                self.step = 1
            elif self.step == 1:
                get2 = tonghuas.pop()
                if len(get3) == 14:
                    get1 = self.remacards
                    self.step = 3
                else:
                    self.step = 2
            else:
                get3 += " " + tonghuas[0][:2]
                get2 += tonghuas[0][2:5]
                get1 = tonghuas[0][6:]
                self.step = 3
        else:
            # 同花大小比较
            mind = ""
            deng = 0
            for f in bu:
                key1 = 0
                key2 = 0
                for i in range(13):
                    if tonghuas[0][f] == key0[i]:
                        key1 = k0[i]
                for i in range(13):
                    if tonghuas[1][f] == key0[i]:
                        key2 = k0[i]
                if key1 == key2:
                    deng = 0
                elif key1 < key2:
                    deng = 1  # 交换
                else:
                    deng = -1  # 不交换
                if deng == 1:
                    # 交换
                    mind = tonghuas[0]
                    tonghuas[0] = tonghuas[1]
                    tonghuas[1] = mind
                    break
                elif deng == 0:
                    continue
                elif deng == -1:
                    break
            get3 = tonghuas[0]
            get2 = tonghuas[1]
            get1 = self.remacards
            self.step = 3
    def shunzi(self):
        # print("找顺子！！！")
        global All, sin, get1, get2, get3, iu, key0, k0, bu, shunzis, shunzitap
        self.cards = self.remacards
        self.change0()
        tes = 0
        bn = 0
        while (1):
            for ro in range(5, 11):  # 找顺子
                for i in iu:
                    mii = min(self.keycount[i], self.keycount[i + 1], self.keycount[i + 2],
                              self.keycount[i + 3], self.keycount[i + 4])
                    suu = (self.keycount[i] + self.keycount[i + 1] + self.keycount[i + 2] +
                           self.keycount[i + 3] + self.keycount[i + 4])
                    if mii > 0 and suu == ro:
                        dc = ""
                        for j in range(i, i + 5):
                            for k in range(4):
                                if All[j][k] == 1:
                                    dc += sin[j][k] + " "
                                    self.cardss.remove(sin[j][k])
                                    break
                        dc = dc.strip()
                        shunzis.append(dc)
                        self.remacards = ' '.join(self.cardss)
                        self.cards = self.remacards
                        self.change0()
                        tes = 1
                        break
                    else:
                        tes = 0
                if tes == 1:
                    tes = 0
                    break
            bn += 1
            if bn >= 2:
                break
        n = len(shunzis)
        if self.step == 0:
            if n == 1:
                get3 = shunzis.pop()
                shunzitap = 1
                self.step = 1
            elif n == 2:
                mind = ""
                deng = 0
                f = -1
                key1 = 0
                key2 = 0
                for i in range(13):
                    if shunzis[0][f] == key0[i]:
                        key1 = k0[i]
                for i in range(13):
                    if shunzis[1][f] == key0[i]:
                        key2 = k0[i]
                if key1 < key2:
                    deng = 1
                else:
                    deng = 0
                if deng == 1:
                    # 交换
                    mind = shunzis[0]
                    shunzis[0] = shunzis[1]
                    shunzis[1] = mind
                get3 = shunzis.pop(0)
                get2 = shunzis.pop()
                get1 = self.remacards
                self.step = 3
        elif self.step == 1:
            if n == 0:
                pass
            elif n == 1:
                if len(get3) == 14:
                    get2 = shunzis.pop()
                    get1 = self.remacards
                    self.step = 3
                else:
                    get2 = shunzis.pop()

                    self.step = 2
        elif self.step == 2:
            if n == 0:
                pass
            elif n == 1:
                get3 += " " + shunzis[0][:2]
                get2 += shunzis[0][2:5]
                get1 = shunzis[0][6:]
                self.step = 3
    def finalcard(self):
        # print("最后牌！！！")
        global santiaos, pairss, get1, get2, get3, n3, n2
        self.cards = self.remacards
        self.change0()
        self.remacards = ' '.join(self.cardss)
        self.santiao()
        self.pairs()
        n = len(santiaos)
        m = len(pairss)
        if self.step == 0:
            if n == 0:
                if m == 0:
                    pass
                elif m == 1:
                    get3 = pairss.pop() + " " + self.remacards[:8]
                    get1 = self.remacards[9:23]
                    get2 = self.remacards[24:]
                elif m == 2:
                    get3 = pairss.pop(0)
                    get3 += " " + pairss.pop() + " " + self.remacards[:2]
                    get1 = self.remacards[3:11]
                    get2 = self.remacards[12:]
                elif m == 3:
                    get3 = pairss.pop(0) + " " + pairss.pop(0)
                    get2 = pairss.pop()
                    get3 += " " + self.remacards[:2]
                    get2 += " " + self.remacards[3:11]
                    get1 = self.remacards[12:]
                elif m == 4:
                    get2 = pairss.pop(0)
                    get1 = pairss.pop(0)
                    get3 = pairss.pop(0) + " " + pairss.pop()
                    get3 += " " + self.remacards[:2]
                    get2 += " " + self.remacards[3:11]
                    get1 += " " + self.remacards[12:]
                elif m == 5:
                    get1 = pairss.pop(0)
                    get3 = pairss.pop(0) + " " + pairss.pop(0)
                    get2 = pairss.pop(0) + " " + pairss.pop()
                    get3 += " " + self.remacards[:2]
                    get2 += " " + self.remacards[3:5]
                    get1 += " " + self.remacards[6:]
                else:
                    get1 = pairss.pop(0)
                    get3 = pairss.pop(0) + " " + pairss.pop(0)
                    get2 = pairss.pop(0) + " " + pairss.pop(0)
                    get3 += " " + pairss[0][:2]
                    get2 += " " + pairss[0][3:]
                    get1 += " " + self.remacards
            elif n == 1:
                zai = self.remacards.split()
                get3 = santiaos.pop()
                get3 += " " + self.remacards[:5]
                get2 = self.remacards[6:17] + " " + zai.pop()
                get1 = self.remacards[18:26]
            else:
                get3 = santiaos.pop(0)
                get2 = santiaos.pop()
                get3 += " " + self.remacards[:5]
                get2 += " " + self.remacards[6:11]
                get1 = self.remacards[12:]
        elif self.step == 1:
            if n == 0:
                if m == 0:
                    zai = self.remacards.split()
                    if len(get3) == 14:
                        get2 = self.remacards[:11] + " " + zai.pop()
                        get1 = self.remacards[12:20]
                    else:
                        get3 += " " + self.remacards[:2]
                        get2 = self.remacards[3:14] + " " + zai.pop()
                        get1 = self.remacards[15:23]
                elif m == 1:
                    if len(get3) == 14:
                        get2 = pairss.pop()
                        get2 += " " + self.remacards[:8]
                        get1 = self.remacards[9:]
                    else:
                        get3 += " " + self.remacards[:2]
                        get2 = pairss.pop()
                        get2 += " " + self.remacards[3:11]
                        get1 = self.remacards[12:]
                elif m == 2:
                    get1 = pairss.pop()
                    get2 = pairss.pop()
                    if len(get3) == 14:
                        get2 += " " + self.remacards[:8]
                        get1 += " " + self.remacards[9:]
                    else:
                        get3 += " " + self.remacards[:2]
                        get2 += " " + self.remacards[3:11]
                        get1 += " " + self.remacards[12:]
                elif m == 3:
                    if len(get3) == 14:
                        get1 = pairss.pop(0) + " " + self.remacards[3:]
                        get2 = pairss.pop(0) + " " + pairss.pop()
                        get2 += " " + self.remacards[:2]
                    else:
                        get3 += " " + self.remacards[:2]
                        get1 = pairss.pop(0) + " " + self.remacards[6:]
                        get2 = pairss.pop(0) + " " + pairss.pop()
                        get2 += " " + self.remacards[3:5]
                else:
                    zai = pairss.pop().split()
                    if len(get3) == 14:
                        get1 = pairss.pop(0) + " " + zai.pop()
                        get2 = pairss.pop(0) + " " + pairss.pop() + " " + zai.pop()
                    else:
                        get3 += " " + zai.pop()
                        get1 = pairss.pop(0) + " " + self.remacards
                        get2 = pairss.pop(0) + " " + pairss.pop() + " " + zai.pop()
            elif n == 1:
                if m == 0:
                    if len(get3) == 14:
                        get2 = santiaos.pop() + " " + self.remacards[:5]
                        get1 = self.remacards[6:]
                    else:
                        get3 += " " + self.remacards[:2]
                        get2 = santiaos.pop() + " " + self.remacards[3:8]
                        get1 = self.remacards[9:]
                elif m == 1:
                    if tonghuatap == 0 and shunzitap == 0:
                        get2 = santiaos.pop() + " " + pairss.pop()
                        if len(get3) == 14:
                            get1 = self.remacards
                        else:
                            get3 += " " + self.remacards[:2]
                            get1 = self.remacards[3:]
                        self.step = 3
                    elif tonghuatap == 1 or shunzitap == 1:
                        get2 = get3
                        get3 = santiaos.pop() + " " + pairss.pop()
                        get1 = self.remacards
                        self.step = 3
            elif n == 2:
                zai = santiaos.pop().split()
                if tonghuatap == 0 and shunzitap == 0:
                    get2 = santiaos.pop() + " " + zai.pop() + " " + zai.pop()
                    if len(get3) == 14:
                        get1 = self.remacards + " " + zai.pop()
                    else:
                        get3 += " " + zai.pop()
                        get1 = self.remacards
                    self.step = 3
                elif tonghuatap == 1 or shunzitap == 1:
                    get2 = get3
                    get3 = santiaos.pop() + " " + zai.pop() + " " + zai.pop()
                    get1 = self.remacards + " " + zai.pop()
                    self.step = 3
        else:
            if n == 0:
                if m == 0:
                    zai = self.remacards.split()
                    if len(get2) < 14 and len(get3) < 14:
                        get3 += " " + zai.pop(0)
                        get2 += " " + zai.pop(0)
                        get1 = ' '.join(zai)
                    if len(get2) < 14 and len(get3) == 14:
                        get2 += " " + zai.pop(0)
                        get1 = ' '.join(zai)
                    if len(get2) == 14 and len(get3) < 14:
                        get3 += " " + zai.pop(0)
                        get1 = ' '.join(zai)
                elif m == 1:
                    zai = self.remacards.split()
                    get1 = pairss.pop() + " " + zai.pop()
                    if len(get2) < 14 and len(get3) < 14:
                        get3 += " " + zai.pop(0)
                        get2 += " " + zai.pop()
                    if len(get2) < 14 and len(get3) == 14:
                        get2 += " " + zai.pop()
                    if len(get2) == 14 and len(get3) < 14:
                        get3 += " " + zai.pop()
                elif m == 2:
                    zai = pairss.pop().split()
                    if len(get2) < 14 and len(get3) < 14:
                        get3 += " " + zai.pop()
                        get2 += " " + zai.pop()
                        get1 = pairss.pop() + " " + self.remacards
                    if len(get2) < 14 and len(get3) == 14:
                        get2 += " " + zai.pop()
                        get1 = pairss.pop() + " " + zai.pop()
                    if len(get2) == 14 and len(get3) < 14:
                        get3 += " " + zai.pop()
                        get1 = pairss.pop() + " " + zai.pop()
            elif n == 1:
                get1 = santiaos.pop()
                zai = self.remacards.split()
                if len(get2) < 14 and len(get3) < 14:
                    get3 += " " + zai.pop()
                    get2 += " " + zai.pop()
                if len(get2) < 14 and len(get3) == 14:
                    get2 += " " + zai.pop()
                if len(get2) == 14 and len(get3) < 14:
                    get3 += " " + zai.pop()
        self.remacards = ""
        self.step = 3
    def GetFinalCards(self):
        global get1, get2, get3, n3, n2, tonghuas, shunzis, santiaos, pairss
        aa = [[], [], [], []]
        n3 = 0
        n2 = 0
        tonghuas = []  # 同花仓库
        shunzis = []  # 顺子仓库
        santiaos = []  # 三条仓库
        pairss = []  # 对子仓库
        get1 = []  # 前墩仓库
        get2 = []  # 中墩仓库
        get3 = []  # 后墩仓库
        self.change()
        if self.step != 3:
            self.SpecialCards1_2()
        if self.step != 3:
            self.SpecialCards3()
        if self.step != 3:
            self.tonghuashun()
        if self.step != 3:
            self.Bomb()
        if self.step != 3:
            self.gourd()
        if self.step != 3:
            self.tonghua()
        if self.step != 3:
            self.shunzi()
        if self.step != 3:
            self.finalcard()
        self.first = ''.join(get1)
        self.middle = ''.join(get2)
        self.final = ''.join(get3)
        self.change()
def main():
    '''
    tan=['#2','*2','&2','$2',
         '#3','*3','&3','$3',
         '#4','*4','&4','$4',
         '#5','*5','&5','$5',
         '#6','*6','&6','$6',
         '#7','*7','&7','$7',
         '#8','*8','&8','$8',
         '#9','*9','&9','$9',
         '#10','*10','&10','$10',
         '#J','*J','&J','$J',
         '#Q','*Q','&Q','$Q',
         '#K','*K','&K','$K',
         '#A','*A','&A','$A']
         cardslist=sample(tan,13)
         '''
    cardslist = ['*A', '#K', '*Q', '*J', '*10', '*9', '*8', '*7', '*6', '*4', '*5', '*3', '*2']
    card = ' '.join(cardslist)
    card = card.replace("1", "")
    cards = AllCard(card)
    cards.GetFinalCards()
    print(cards.first)
    print(cards.middle)
    print(cards.final)
    return 0


if __name__ == '__main__':
    main()
