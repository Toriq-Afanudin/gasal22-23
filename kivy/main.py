from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatIconButton as MDB


class Test(MDApp):
    def build(self):
        return MDB(text="Hello",pos_hint={"center_x":0.5,"center_y":0.5},icon="language-python")
    
if __name__=="__mai