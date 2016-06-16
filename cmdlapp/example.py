

from time import sleep

from cmdlapp import CmdlApp


class Example(CmdlApp):
    def __init__(self):
        super().__init__()

        
        self.configure(
            tool_name='CmdlAppExample',
            tool_version='0.1beta')

        self.configure(
            has_cfgfile=False,
            reload_on_hup=True)
            
    
    def main_fct(self):
        while(True):
            print('Hello World!')
            sleep(1)

if __name__ == '__main__':
    Example().run()
