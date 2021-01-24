from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    BooleanProperty,
    BoundedNumericProperty,
    ColorProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)

from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.theming import  ThemeManager
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, OneLineIconListItem, IconLeftWidget, IconRightWidget, ThreeLineAvatarIconListItem
from kivymd.uix.list_custom import ThreeLineAvatarIconListItem_custom
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix import MDAdaptiveWidget
from kivy.metrics import dp
from kivymd.icon_definitions import md_icons
from kivymd.uix.dialog import MDDialog
from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout

# how to call a func from within Class A from Class B >>>Intphone().test1()

items = []

class dContent(BoxLayout):
    pass

def show_alert_dialog(self,x,inst_refer_to):
    #dialog = None
   
    dialog = MDDialog(
        
        title="Edit:",
        type="custom",# custom type equal to 
        content_cls=dContent(),
        buttons=[
            MDFlatButton(
                text="APPLY"
                ,on_press = lambda qq: [dialog.dismiss(),Intphone().editMe(str(inst_refer_to),dialog.content_cls.ids.item.text)]
            ),
            MDFlatButton(
                text="DISCARD"
                ,on_press = lambda qq: [dialog.dismiss(),Intphone().removeMe(str(inst_refer_to))]
            ),
        ],
    )
    for x in items:
        if inst_refer_to == x.id:
            dialog.content_cls.ids.item.text = x._description1.text
    dialog.open()
    #print(inst_refer_to)
    


   




class Iventory_Scr(Screen):
    pass

class Sales_Scr(Screen):
    pass


def test():
    print("test")

class inventoryList(FloatLayout, FocusBehavior): # CUSTOM WIDGET
    
    
    _header = StringProperty("") # To edit MBlabel
    _commandlist = StringProperty("")
    _color_f = ColorProperty([1.0, 1.0, 1.0, 0])

    
    def show_alert_dialog_def(self,x,a): # how to call function outside of a class
        callme = show_alert_dialog(self,x,a)

    def on_enter(self,*args):# how to detect mouse over on widget with the FocusBehavior inherit class
        global last_touch
        last_touch = self._header
        #print(self._header)    
    
        
    def my_id(self):# Return
        me1 = self._header
        print(me1)
        return me1     
    
    def __init__(self, **kwargs):
        super(inventoryList,self).__init__(**kwargs)

        self.focus_behavior = True
        self.bg_color = (1,0,1,0.5)
        self.height = 58
        
        self._backbutton = OneLineAvatarIconListItem( bg_color = (1,0,1,0.5),on_press = lambda s: Intphone().app.createMe()) # Had to make custom height adjustment formula because of FloatLayout in a MDlist in a ScrollView
        self.add_widget(self._backbutton)

        self._backbutton.add_widget(IconRightWidget(icon="file-edit", on_press = lambda q: [self.show_alert_dialog_def(True,self.my_id())],text_color= (.2,.2,.2,1),theme_text_color= "Custom")) # how to add multiple func to >>on_press = lambda x: [self.show_alert_dialog_def(), self.my_id()]
        self._description1 = MDLabel(text= self._header,markup = True)
        self._description1.font_size = 18
    
        self._backbutton.add_widget(self._description1,index = -1)
       


       
        #print (test())
        #print(self._header)
        




class Intphone(MDApp):
   
    def build(self):
        theme_cls = ThemeManager()
       
    def createMe(self):
        global items
        global last_touch

        
        a = inventoryList(_header = f"Item{len(items)-1}")
        a.id = a._header

        self.root.ids.Inv_scr.add_widget(a)
        items.append(a)
        a._backbutton.pos = (0, 58*len(items)-35)
        a._description1.pos = (10, 58*len(items)-35)

        
        #a = inventoryList(_header = "Item3")
       
        #eval('self.show_alert_dialog()')
        
        

       
        #self.root.ids.Inv_scr.remove_widget(a)
        #print(items[len(items)-1].id)
        #print(items[len(items)-1]._header)
        #c._description1.on_press = self.show_alert_dialog()
        #print(self.root.ids.Inv_scr.index)
        #c = SV()
        #print(self.root.ids.screenNames.screens[1].add_widget(c))
        #self.root.ids.screenNames.current_screen.add_widget(c)
        #self.root.ids.Sales_scr.add_widget(c)

        #c._T.text = "aaaaaaaaaaaaaaa1111"
        #print(c._T._Header.text)
    def test1(self,e):
        print(e)

    def removeMe(self,inst_refer_to):
        for x in items:
            if inst_refer_to == x.id:
                #print(x.hgth.pop(0))
                
                items.remove(x)
                x.parent.remove_widget(x)# have to refer to widget parent to remove it
                break

        
                #x._description1.text = "ADS"
                #x._header = "ADS"
                #self.root.ids.Inv_scr.add_widget(x)
        for x in items:
            x._backbutton.pos = (0, 58*(items.index(x)+1)-35)
            x._description1.pos = (10, 58*(items.index(x)+1)-35)


    def editMe(self,inst_refer_to,item_name):
        for x in items:
            if inst_refer_to == x.id:
                x._description1.text = item_name
                #x._header = x._description1.text
        pass
        
    pass

if __name__ == '__main__':   
    Intphone().run()