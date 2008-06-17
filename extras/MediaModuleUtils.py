import os
import pickle
import sys
import traceback

import xbmcgui
import xbmc

ACTION_MOVE_LEFT              = 1  
ACTION_MOVE_RIGHT             = 2
ACTION_MOVE_UP                = 3
ACTION_MOVE_DOWN              = 4
ACTION_PAGE_UP                = 5 
ACTION_PAGE_DOWN              = 6
ACTION_SELECT_ITEM            = 7
ACTION_HIGHLIGHT_ITEM         = 8
ACTION_PARENT_DIR             = 9
ACTION_PREVIOUS_MENU          = 10
ACTION_SHOW_INFO              = 11
ACTION_PAUSE                  = 12
ACTION_STOP                   = 13
ACTION_NEXT_ITEM              = 14
ACTION_PREV_ITEM              = 15
ACTION_CONTEXT_MENU           = 117

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
        if action.getId() == ACTION_PREVIOUS_MENU:
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