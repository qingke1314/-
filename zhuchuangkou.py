import wx
import requests
import wx.grid as wg
import re
import suanfa
import json
import time
from jiazaitupian import *
class TransparentText(wx.StaticText):
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TRANSPARENT_WINDOW, name='transparenttext'):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.on_size)
    def on_paint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)
    def on_size(self, event):
        self.Refresh()
        event.Skip()
class TransparentButton(wx.Button):
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize,
        style=wx.TRANSPARENT_WINDOW):
        wx.Button.__init__(self, parent, id, label, pos, size, style)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.on_size)
    def on_paint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)
    def on_size(self, event):
        self.Refresh()
        event.Skip()
    '''def on_paint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)
    def on_size(self, event):
        self.Refresh()
        event.Skip()'''
class MyFrame(wx.Frame):
    def __init__(self,parent,id,token,userid):
        wx.Frame.__init__(self,parent,id,'福建十三水',pos=(250,50),size=(1000,700),style = wx.DEFAULT_FRAME_STYLE)
        self.SetMaxSize((1000,700))
        self.limit=1
        self.token=token
        self.userid=userid
        self.tdtp=[]
        self.zdtp=[]
        self.ddtp=[]
        self.shuchu={}

        self.bjt0 = wx.Bitmap("90/zjm.png")
        self.bjt1 = wx.Bitmap("90/zjm.png")
        self.font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font=wx.Font(16,wx.SWISS,wx.NORMAL,wx.LIGHT)
        self.panel=wx.Panel(self)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.bt_game=wx.Button(self.panel, label='开始对战',size=(180,60),style=0)
        self.bt_game.SetBackgroundColour('DARK TURQUOISE')
        self.bt_game.SetForegroundColour('FIREBRICK')
        self.bt_game.SetFont(font=font)
        self.bt_game.Bind(wx.EVT_BUTTON,self.ingame)
        self.bt_rank=wx.Button(self.panel,label='查看排行榜',size=(180,60))
        self.bt_rank.Bind(wx.EVT_BUTTON,self.paihangbang)
        self.bt_rank.SetBackgroundColour('LIGHT STEEL BLUE')
        self.bt_rank.SetForegroundColour('FIREBRICK')
        self.bt_rank.SetFont(font=font)
        self.bt_history=wx.Button(self.panel,label='查看往期对战',size=(180,60),style=0)
        self.bt_history.Bind(wx.EVT_BUTTON,self.wangqiduizhan)
        self.bt_history.SetBackgroundColour('DARK TURQUOISE')
        self.bt_history.SetForegroundColour('FIREBRICK')
        self.bt_history.SetFont(font=font)
        self.bt_room=wx.Button(self.panel,label='查看某场对战',size=(180,60))
        self.bt_room.SetBackgroundColour('LIGHT STEEL BLUE')
        self.bt_room.SetForegroundColour('FIREBRICK')
        self.bt_room.SetFont(font=font)
        self.bt_room.Bind(wx.EVT_BUTTON,self.xiangxi)
        self.vvvvt()


        self.bt_return = wx.Button(self.panel, label='返回', pos=(10, 10), size=(80, 40))
        self.bt_return.SetBackgroundColour('white')
        self.bt_return.SetFont(self.font)
        self.bt_return.Bind(wx.EVT_BUTTON, self.returnpaihang)
        self.grid = wg.Grid(self.panel, -1)
        self.grid.CreateGrid(120, 3)
        self.grid.SetSize((750, 500))
        self.grid.SetPosition((120, 120))
        for i in range(3):
            self.grid.SetColSize(i, 215)
        for i in range(70):
            self.grid.SetRowSize(i, 30)
        self.grid.SetColLabelValue(0, "玩家id")
        self.grid.SetColLabelValue(1, "分数")
        self.grid.SetColLabelValue(2, "玩家昵称")
        self.grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTER)
        self.grid.Hide()
        self.bt_return.Hide()

        self.panel2 = wx.Panel(self.panel, size=(1000, 700))
        self.panel2.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        self.bt_returnroom = wx.Button(self.panel2, label='返回', pos=(10, 10), size=(80, 40))
        self.bt_returnroom.SetBackgroundColour('white')
        self.bt_returnroom.SetFont(self.font)
        self.bt_returnroom.Bind(wx.EVT_BUTTON, self.returnroom)
        self.text_room = wx.TextCtrl(self.panel2, style=wx.TE_LEFT, value=wx.EmptyString, pos=(410, 200),
                                     size=(250, 40))
        self.text_room.SetFont(self.font)
        self.static_room = TransparentText(self.panel2, label='请输入房间号', pos=(245, 200), size=(165, 40), style=0)
        self.static_room.SetFont(self.font)

        self.static_room.SetBackgroundColour('TURQUOISE')
        self.search1 = TransparentButton(self.panel2, label='搜索', pos=(660, 200), size=(80, 40))
        #self.search1.SetBackgroundColour('TURQUOISE')
        self.search1.SetFont(self.font)
        self.search1.Bind(wx.EVT_BUTTON, self.searchroom)
        self.grid2 = wg.Grid(self.panel2, -1)
        self.grid2.CreateGrid(4, 4)
        self.grid2.SetSize((683, 193))
        self.grid2.SetPosition((150, 280))
        self.grid2.SetColSize(3, 120)
        self.grid2.SetColSize(1, 320)
        for i in range(4):
            self.grid2.SetRowSize(i, 40)
            #self.grid2.SetCellBackgroundColour(3,i,'turquoise')
            self.grid2.SetCellBackgroundColour(0, i, 'turquoise')
            self.grid2.SetCellBackgroundColour(2, i, 'turquoise')
            #self.grid2.SetCellBackgroundColour(1, i, 'turquoise')
        self.grid2.SetColLabelValue(0, "玩家id")
        self.grid2.SetColLabelValue(1, "出牌情况")
        self.grid2.SetColLabelValue(2, "玩家昵称")
        self.grid2.SetColLabelValue(3, "分数")
        self.panel2.Hide()

        self.text_id = wx.TextCtrl(self.panel, style=wx.TE_LEFT, value=wx.EmptyString, pos=(410, 120), size=(250, 40))
        self.text_id.SetFont(self.font)
        self.static_id = wx.StaticText(self.panel, label='请输入玩家id', pos=(245, 120), size=(165, 40))
        self.static_id.SetFont(self.font)
        self.static_id.SetBackgroundColour('white')
        self.bt_returnwangqi = wx.Button(self.panel, label='返回', pos=(10, 10), size=(80, 40))
        self.bt_returnwangqi.SetBackgroundColour('white')
        self.bt_returnwangqi.SetFont(self.font)
        self.bt_returnwangqi.Bind(wx.EVT_BUTTON, self.return2)

        bitmap1 = wx.Image("90/zuo.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        bitmap2 = wx.Image("90/you.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.bt_zuo = wx.BitmapButton(self.panel, -1, bitmap1, pos=(250, 513), size=(100, 100))
        self.bt_zuo.Bind(wx.EVT_BUTTON, self.btzuo)
        self.bt_zuo.SetBackgroundColour('TURQUOISE')
        self.bt_you = wx.BitmapButton(self.panel, -1, bitmap2, pos=(635, 513), size=(100, 100))
        self.bt_you.Bind(wx.EVT_BUTTON, self.btyou)
        self.bt_you.SetBackgroundColour('TURQUOISE')
        self.search = TransparentButton(self.panel, label='搜索', pos=(660, 120), size=(80, 40))
        #self.search.SetBackgroundColour('TURQUOISE')
        self.search.SetFont(self.font)
        self.search.Bind(wx.EVT_BUTTON, self.searchwar)
        self.grid1 = wg.Grid(self.panel, -1)
        self.grid1.CreateGrid(10, 4)
        self.grid1.SetSize((683, 333))
        self.grid1.SetPosition((150, 180))
        self.grid1.SetColSize(3, 120)
        self.grid1.SetColSize(1, 320)
        self.grid1.SetColLabelValue(0, "房间号")
        self.grid1.SetColLabelValue(1, "出牌情况")
        self.grid1.SetColLabelValue(2, "分数")
        self.grid1.SetColLabelValue(3, "时间")
        for i in range(10):
            if not (i % 2):
                self.grid1.SetCellBackgroundColour(i, 0, 'TURQUOISE')
                self.grid1.SetCellBackgroundColour(i, 2, 'TURQUOISE')
                self.grid1.SetCellBackgroundColour(i, 1, 'TURQUOISE')
                self.grid1.SetCellBackgroundColour(i, 3, 'TURQUOISE')
        for i in range(10):
            self.grid1.SetRowSize(i, 30)
        self.static_id.Hide()
        self.text_id.Hide()
        self.grid1.Hide()
        self.bt_zuo.Hide()
        self.bt_you.Hide()
        self.search.Hide()
        self.bt_returnwangqi.Hide()

        self.panel3=wx.Panel(self.panel, size=(1000, 700))
        self.panel3.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        bitmap3=wx.Image("90/ksyx.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()


        self.bt_ksyx=wx.BitmapButton(self.panel3, -1, bitmap3, pos=(370, 483),style=0)

        self.bt_ksyx.SetBackgroundColour('turquoise')
        self.bt_ksyx.Bind(wx.EVT_BUTTON,self.qupai)
        self.bt_xunhuansai=wx.Button(self.panel3, label='循环赛', pos=(420, 570), size=(150, 80))
        self.bt_xunhuansai.SetFont(wx.Font(35, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.bt_xunhuansai.SetBackgroundColour('turquoise')
        self.bt_xunhuansai.Bind(wx.EVT_BUTTON,self.kaishixunhuan)
        self.bt_returnduizhan = wx.Button(self.panel3, label='返回', pos=(10, 10), size=(80, 40))
        self.bt_returnduizhan.SetBackgroundColour('white')
        self.bt_returnduizhan.SetFont(self.font)
        self.bt_returnduizhan.Bind(wx.EVT_BUTTON, self.returnduizhan)
        self.bt_chupai=TransparentButton(self.panel3,label='出牌',pos=(455,503),size=(100,60))
        self.bt_chupai.SetForegroundColour('LIGHT STEEL BLUE')
        #self.bt_chupai.SetBackgroundColour('white')
        self.bt_chupai.SetFont(wx.Font(35, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.bt_chupai.Bind(wx.EVT_BUTTON,self.chupai)
        self.bt_chupai.Hide()
        self.panel3.Hide()
    def xunhuan(self,token):

        url = "http://api.revth.com/game/open"
        headers = {'x-auth-token': token}
        response = requests.request("POST", url, headers=headers)
        cardslist = dict(response.json()).get('data').get('card')

        cardslist = cardslist.replace('1', '')
        print(cardslist)
        cards = suanfa.AllCard(cardslist)
        cards.GetFinalCards()

        str1 = cards.first
        print(str1)
        str2 = cards.middle
        print(str2)
        str3 = cards.final
        print(str3)
        chupai = [str1, str2, str3]

        id = dict(response.json()).get('data').get('id')
        shuchu = {"id": id, "card": chupai}
        shuchu = json.dumps(shuchu)
        url1 = "http://api.revth.com/game/submit"
        payload1 = str(shuchu)
        headers1 = {
            'content-type': "application/json",
            'x-auth-token': token
        }
        response = requests.request("POST", url1, data=payload1, headers=headers1)
        print(response.text)
    def kaishixunhuan(self,event):
        for i in range(100):

                self.xunhuan(self.token)
    def chupai(self,event):
        url = "http://api.revth.com/game/submit"
        payload = str(self.shuchu)
        headers = {
            'content-type': "application/json",
            'x-auth-token': self.token
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        self.bt_chupai.Hide()
        self.bt_ksyx.Show()
        for i in range(3):
            self.tdtp[i].Destroy()
        for i,item in enumerate(self.zdtp):
            self.zdtp[i].Destroy()
        for i, item in enumerate(self.ddtp):
            self.ddtp[i].Destroy()
        self.tdtp=[]
        self.zdtp=[]
        self.ddtp=[]
    def qupai(self, event) :
        self.bt_ksyx.Hide()
        self.bt_chupai.Show()
        url = "http://api.revth.com/game/open"
        headers = {'x-auth-token': self.token}
        response = requests.request("POST", url, headers=headers)
        cardslist=dict(response.json()).get('data').get('card')
        a=cardslist.replace("1", "")
        cards = suanfa.AllCard(a)#调用ai模块，创建类实例并进行排序
        cards.GetFinalCards()
        chupai = [cards.first,cards.middle,cards.final]
        print(chupai)
        id=dict(response.json()).get('data').get('id')
        self.shuchu = {"id": id, "card": chupai}
        self.shuchu=json.dumps(self.shuchu)
        pattern = r'[*#$&]\d{2}|[*#$&][2-9AQKJ]'
        match1=re.findall(pattern, cards.first)
        match2 = re.findall(pattern, cards.middle)
        match3 = re.findall(pattern, cards.final)
        fangzhitoudun=[]
        fangzhizhongdun=[]
        fangzhididun=[]
        for i in range(3):
            if match1[i][:1]=='*':
                fangzhitoudun.append(tupianzidian.get('meihua'+match1[i][1:]))
            elif match1[i][:1]=='$':
                fangzhitoudun.append(tupianzidian.get('heitao'+match1[i][1:]))
            elif match1[i][:1]=='#':
                fangzhitoudun.append(tupianzidian.get('fangpian'+match1[i][1:]))
            else:
                fangzhitoudun.append(tupianzidian.get('hongtao'+match1[i][1:]))
        for i,item in enumerate(fangzhitoudun):
            a=wx.StaticBitmap(self.panel3,-1,fangzhitoudun[i],pos=(300+100*i,50))
            self.tdtp.append(a)
        for i in range(5):
            if match2[i][:1]=='*':
                fangzhizhongdun.append(tupianzidian.get('meihua'+match2[i][1:]))
            elif match2[i][:1]=='$':
                fangzhizhongdun.append(tupianzidian.get('heitao'+match2[i][1:]))
            elif match2[i][:1]=='#':
                fangzhizhongdun.append(tupianzidian.get('fangpian'+match2[i][1:]))
            else:
                fangzhizhongdun.append(tupianzidian.get('hongtao'+match2[i][1:]))
            if match3[i][:1]=='*':
                fangzhididun.append(tupianzidian.get('meihua'+match3[i][1:]))
            elif match3[i][:1]=='$':
                fangzhididun.append(tupianzidian.get('heitao'+match3[i][1:]))
            elif match3[i][:1]=='#':
                fangzhididun.append(tupianzidian.get('fangpian'+match3[i][1:]))
            else:
                fangzhididun.append(tupianzidian.get('hongtao'+match3[i][1:]))
        for i,item in enumerate(fangzhizhongdun):
            b=wx.StaticBitmap(self.panel3,-1,fangzhizhongdun[i],pos=(220+100*i,150))
            self.zdtp.append(b)
        for i,item in enumerate(fangzhididun):
            c=wx.StaticBitmap(self.panel3,-1,fangzhididun[i],pos=(220+100*i,250))
            self.ddtp.append(c)
    def returnduizhan(self,event):
        self.panel3.Hide()
        self.bt_history.Show()
        self.bt_rank.Show()
        self.bt_room.Show()
        self.bt_game.Show()
    def ingame(self,event):
        self.bt_history.Hide()
        self.bt_rank.Hide()
        self.bt_room.Hide()
        self.bt_game.Hide()
        self.panel3.Show()
    def xiangxi(self,event):
        self.bt_history.Hide()
        self.bt_rank.Hide()
        self.bt_room.Hide()
        self.bt_game.Hide()
        self.panel2.Show()
    def returnroom(self, event):
        self.panel2.Hide()
        self.bt_history.Show()
        self.bt_rank.Show()
        self.bt_room.Show()
        self.bt_game.Show()
    def searchroom(self,event):
        roomid=self.text_room.GetValue()
        url = "http://api.revth.com/history/"+str(roomid)
        headers = {'x-auth-token': self.token}
        response = requests.request("GET", url, headers=headers)
        list1=dict(response.json()).get('data').get('detail')
        for i in range(4):
            self.grid2.SetCellValue(i, 0, str(list1[i].get('player_id')))
            self.grid2.SetCellValue(i, 1, str(list1[i].get('card')))
            self.grid2.SetCellValue(i, 2, str(list1[i].get('name')))
            self.grid2.SetCellValue(i, 3, str(list1[i].get('score')))
    def wangqiduizhan(self,event):
        self.bt_history.Hide()
        self.bt_rank.Hide()
        self.bt_room.Hide()
        self.bt_game.Hide()
        self.static_id.Show()
        self.text_id.Show()
        self.grid1.Show()
        self.bt_zuo.Show()
        self.bt_you.Show()
        self.search.Show()
        self.bt_returnwangqi.Show()
    def btzuo(self,event):
        self.limit-=1
        if self.limit<0:
            self.limit+=1

        a = self.text_id.GetValue()
        url = "http://api.revth.com/history"
        querystring = {"page": self.limit, "limit": 10, "player_id": int(a)}
        headers = {'x-auth-token': self.token}
        response = requests.request("GET", url, headers=headers, params=querystring)
        dict1 = dict(response.json())
        if dict1.get('status') != 0:
            wx.MessageBox('id或token错误！')
        else:
            list1 = dict1.get('data')
            for i, itm in enumerate(list1):
                self.grid1.SetCellValue(i, 0, str(list1[i].get('id')))
                self.grid1.SetCellValue(i, 1, str(list1[i].get('card')))
                self.grid1.SetCellValue(i, 2, str(list1[i].get('score')))
                self.grid1.SetCellValue(i, 3, str(list1[i].get('timestamp')))
    def btyou(self,event):
        self.limit+=1

        a = self.text_id.GetValue()
        url = "http://api.revth.com/history"
        querystring = {"page": self.limit, "limit": 10, "player_id": int(a)}
        headers = {'x-auth-token': self.token}

        response = requests.request("GET", url, headers=headers, params=querystring)
        dict1 = dict(response.json())
        if dict1.get('status') != 0:
            wx.MessageBox('id或token错误！')
        else:
            list1 = dict1.get('data')
            for i in range(10):
                self.grid1.SetCellValue(i, 0, ' ')
                self.grid1.SetCellValue(i, 1, ' ')
                self.grid1.SetCellValue(i, 2, ' ')
                self.grid1.SetCellValue(i, 3, ' ')
            for i, itm in enumerate(list1):
                self.grid1.SetCellValue(i, 0, str(list1[i].get('id')))
                self.grid1.SetCellValue(i, 1, str(list1[i].get('card')))
                self.grid1.SetCellValue(i, 2, str(list1[i].get('score')))
                self.grid1.SetCellValue(i, 3, str(list1[i].get('timestamp')))
    def return2(self,event):

        self.bt_returnwangqi.Hide()
        self.search.Hide()
        self.text_id.Hide()
        self.static_id.Hide()
        self.grid1.Hide()
        self.bt_zuo.Hide()
        self.bt_you.Hide()
        self.bt_history.Show()
        self.bt_rank.Show()
        self.bt_room.Show()
        self.bt_game.Show()
    def returnpaihang(self, event):
        self.bt_history.Show()
        self.bt_rank.Show()
        self.bt_room.Show()
        self.bt_game.Show()
        self.grid.Hide()
        self.bt_return.Hide()
    def paihangbang(self,event):
        self.bt_history.Hide()
        self.bt_rank.Hide()
        self.bt_room.Hide()
        self.bt_game.Hide()
        self.input()
        self.grid.Show()
        self.bt_return.Show()
    def input(self):
        url = "http://api.revth.com/rank"
        response = requests.request("GET", url)
        list2=response.json()
        list1=[]
        for i in list2:
            a=dict(i)
            list1.append(a)
        for i,item in enumerate(list1):
            self.grid.SetCellValue(i, 0, str(list1[i].get('player_id')))
            if i % 2:
                self.grid.SetCellBackgroundColour(i, 0, 'TURQUOISE')
                self.grid.SetCellBackgroundColour(i, 2, 'TURQUOISE')
                self.grid.SetCellBackgroundColour(i, 1, 'TURQUOISE')
            self.grid.SetCellValue(i, 1, str(list1[i].get('score')))
            self.grid.SetCellValue(i, 2, str(list1[i].get('name')))
            self.grid.SetCellAlignment(i, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            self.grid.SetCellAlignment(i, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            self.grid.SetCellAlignment(i, 2, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
    def vvvvt(self):
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.bt_game, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        vsizer_all.Add(self.bt_rank, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        vsizer_all.Add(self.bt_history, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        vsizer_all.Add(self.bt_room, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        self.panel.SetSizer(vsizer_all)
    def OnEraseBack(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()

        dc.DrawBitmap(self.bjt0, 0, 150)
    def searchwar(self,event):
        self.limit=0

        a=self.text_id.GetValue()
        url = "http://api.revth.com/history"
        querystring = {"page": self.limit, "limit": 10, "player_id": int(a)}
        headers = {'x-auth-token':self.token}
        response = requests.request("GET", url, headers=headers, params=querystring)
        dict1=dict(response.json())



        if dict1.get('status')!=0:
            wx.MessageBox('请求错误！')
        else:
            list1=dict1.get('data')
            if list1!=[]:
                for i in range(10):
                    if not list1[i]:
                        wx.MessageBox('此人战绩未满十条！')
                        break
                    self.grid1.SetCellValue(i, 0, str(list1[i].get('id')))
                    self.grid1.SetCellValue(i,1,str(list1[i].get('card')))
                    self.grid1.SetCellValue(i, 2, str(list1[i].get('score')))
                    self.grid1.SetCellValue(i, 3, str(list1[i].get('timestamp')))
            else:
                wx.MessageBox('该玩家未战斗过！')
    def OnEraseBack1(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()

        dc.DrawBitmap(self.bjt1, 0, 150)
if __name__=='__main__':
    app=wx.App()
    frames=MyFrame(None,-1,'sasas','122')
    frames.Show()
    app.MainLoop()
