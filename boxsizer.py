import wx
import requests
import zhucejiemian
import json
class MyFrame1(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'用户登录',pos=(230,120),size=(800,550),style = wx.DEFAULT_FRAME_STYLE)
        self.SetMaxSize((800,500))
        self.panel=wx.Panel(self)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        bmp1 = wx.Image("90/kk1.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #self.bt_up = wx.Button(self.panel, label='登录')
        self.bt_up=wx.BitmapButton(self.panel, -1, bmp1,pos=(300,250),size=(110,50))
        self.bt_up.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        #self.bt_up.SetFont(font)
        self.bt_up.SetBackgroundColour('white')
        bmp2=wx.Image("90/kk2.png",wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #self.bt_zc = wx.Button(self.panel, label='注册')
        self.bt_zc=wx.BitmapButton(self.panel, -1, bmp2,pos=(410,250),size=(110,50))
        self.bt_zc.Bind(wx.EVT_BUTTON, self.Onclickzhuce)
        self.bt_zc.SetFont(font)
        self.bt_zc.SetBackgroundColour('white')
        font1 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.title=wx.StaticText(self.panel,label='请输入用户名和密码')
        self.title.SetBackgroundColour('white')

        self.title.SetFont(font1)
        self.label_user=wx.StaticText(self.panel,label='用户名：')
        self.label_user.SetBackgroundColour('white')
        self.label_user.SetFont(font)
        self.text_user=wx.TextCtrl(self.panel,style=wx.TE_LEFT,value=wx.EmptyString)
        self.text_user.SetBackgroundColour('white')
        self.label_pwd=wx.StaticText(self.panel,label='密  码：')
        self.label_pwd.SetFont(font)
        self.label_pwd.SetBackgroundColour('white')
        self.text_pwd=wx.TextCtrl(self.panel,style=wx.TE_LEFT|wx.TE_PASSWORD)
        self.text_pwd.SetBackgroundColour('white')
    def setvv(self):
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)

        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=75)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=195)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=195)

        self.panel.SetSizer(vsizer_all)
    def OnclickSubmit(self,event):
        msg1=''
        username=self.text_user.GetValue()#获取用户的输入
        password=self.text_pwd.GetValue()
        url = "http://api.revth.com/auth/login"
        payload = "{\"username\":\"" + str(username) + "\",\"password\":\"" + str(password) + "\"}"
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        dict1=dict(response.json())
        a=dict1.get('status')
        if a==0:
            dict2=dict(dict1.get('data'))
            self.token=dict2.get('token')
            import zhuchuangkou
            youxi=zhuchuangkou.MyFrame(None,-1,token=dict1.get('data').get('token'),userid=dict1.get('data').get('user_id'))
            youxi.Show()
            self.Destroy()
        elif a==1005:
            msg1='用户名或密码错误'
            wx.MessageBox(msg1)
        else:
            msg1='登录失败'
            wx.MessageBox(msg1)
    def Onclickzhuce(self,event):
        zhuceframe=zhucejiemian.MyFrame2(None, -1)
        zhuceframe.Show()
    def OnEraseBack(self,event):
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                rect = self.GetUpdateRegion().GetBox()
                dc.SetClippingRect(rect)
            dc.Clear()
            bmp = wx.Bitmap("90/dljm.png")
            dc.DrawBitmap(bmp, 0, 0)
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame1(None,-1)
    frame.setvv()
    frame.Show()
    app.MainLoop()