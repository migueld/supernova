import os
import pickle
import sys
import traceback

import xbmcgui
import xbmc

CONTROL_MODULE_TITLE          = 4001
CONTROL_MAIN_LIST             = 4000
CONTROL_BREADCRUMB_POSITION_0 = 3000
CONTROL_BREADCRUMB_POSITION_1 = 3001
CONTROL_BREADCRUMB_POSITION_2 = 3002

STATE_MODULE_WINDOW           = 0
STATE_MODULE_MEDIA_LIST       = 1

class MediaModuleWindow(xbmcgui.WindowXML):
    def initVariables(self, mediaType):
        self.state = STATE_MODULE_WINDOW
        self.mediaType = sys.argv[1]
        
    def onAction(self, action):
        if action.getId() == xbmcgui.ACTION_PREVIOUS_MENU:
            self.close()
        
def main():
    try:
        window = MediaModuleWindow('custom50_VideoModule.xml', 'Q:\skin\CenterStage')
        window.doModal()
    except:
        xbmc.log('Exception (main): ' + str(sys.exc_info()[0]))
        traceback.print_exc()
    

if __name__ == "__main__":
    main()