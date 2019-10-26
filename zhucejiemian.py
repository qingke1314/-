import wx
import requests
class MyFrame2(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'注册界面',pos=(230,150),size=(800,550),style = wx.DEFAULT_FRAME_STYLE)

        self.panel = wx.Panel(self)
        # self.panel.SetBackgroundColour('AQUAMARINE')
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        #self.bt_up = wx.Button(self.panel, label='登录')
        #self.bt_up.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        #self.bt_up.SetFont(font)
        #self.bt_up.SetBackgroundColour('TURQUOISE')
        bmp2 = wx.Image("90/kk2.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        # self.bt_zc = wx.Button(self.panel, label='注册')
        self.bt_zc = wx.BitmapButton(self.panel, -1, bmp2, pos=(360, 250), size=(110, 50))
        self.bt_zc.SetBackgroundColour('white')
        self.bt_zc.Bind(wx.EVT_BUTTON,self.Onclickzhuce)
        font1 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.title = wx.StaticText(self.panel, label='请输入用户名和密码')
        self.title.SetBackgroundColour('white')
        self.title.SetFont(font1)
        self.label_user = wx.StaticText(self.panel, label='用户名：')
        self.label_user.SetBackgroundColour('white')
        self.label_user.SetFont(font)
        self.text_user = wx.TextCtrl(self.panel, style=wx.TE_LEFT, value=wx.EmptyString)
        self.text_user.SetBackgroundColour('white')
        self.label_pwd = wx.StaticText(self.panel, label='密  码：')
        self.label_pwd.SetFont(font)
        self.label_pwd.SetBackgroundColour('white')
        self.text_pwd = wx.TextCtrl(self.panel, style=wx.TE_LEFT | wx.TE_PASSWORD)
        self.text_pwd.SetBackgroundColour('white')
        self.setvv()
        image = wx.Image('90/back.png', wx.BITMAP_TYPE_PNG)
    def Onclickzhuce(self,event):
        msg = ''
        username = self.text_user.GetValue()
        password = self.text_pwd.GetValue()
        url = "http://api.revth.com/register"
        payload = "{\"username\":\"" + str(username) + "\",\"password\":\"" + str(password) + "\"}"
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        dict1 = dict(response.json())
        if dict1.get('status') == 1001:
            msg = '该用户名已经被注册了~'
        elif dict1.get('status') == 1002:
            msg = '学号已经绑定咯...'
        elif dict1.get('status') == 1004:
            msg = 'token过期咯'
        elif dict1.get('status') == 1003:
            msg = '教务处认证失败！'
        elif dict1.get('status')==0:
            msg='注册成功！'
        else:
            msg = '未知错误。'
        wx.MessageBox(msg)
    def setvv(self):
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        #hsizer_button.Add(self.bt_up, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_zc, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=75)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=195)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=195)
        #vsizer_all.Add(hsizer_button, proportion=0, flag=wx.TOP | wx.ALIGN_CENTER, border=45)
        self.panel.SetSizer(vsizer_all)
    def OnEraseBack(self,event):
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                rect = self.GetUpdateRegion().GetBox()
                dc.SetClippingRect(rect)
            dc.Clear()
            bmp = wx.Bitmap("90/dljm.png")
            dc.DrawBitmap(bmp, 0, 0)