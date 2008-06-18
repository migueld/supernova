import os
import pickle
import sys
import traceback

import xbmcgui
import xbmc

class MediaModuleWindow(xbmcgui.WindowXML):
    CONTROL_MODULE_TITLE          = 4010
    CONTROL_MAIN_LIST             = 4000
    CONTROL_BREADCRUMB_POSITION_0 = 3000
    CONTROL_BREADCRUMB_POSITION_1 = 3001
    CONTROL_BREADCRUMB_POSITION_2 = 3002

    STATE_MODULE_WINDOW           = 0
    STATE_MODULE_MEDIA_LIST       = 1

    LIST_ITEMS = {
        'movies': [ 
            xbmcgui.ListItem('Library', 'Library', 'Icons/Movies-Library.png', 'Icons/Movies-Library.png'),
            xbmcgui.ListItem('Actors', 'Actors', 'Icons/Movies-Actors.png', 'Icons/Movies-Actors.png'),
            xbmcgui.ListItem('Directors', 'Directors', 'Icons/Movies-Directors.png', 'Icons/Movies-Directors.png'),
            xbmcgui.ListItem('Genres', 'Genres', 'Icons/Movies-Genres.png', 'Icons/Movies-Genres.png'),
            xbmcgui.ListItem('Playlists', 'Playlists', 'Icons/Movies-Playlists.png', 'Icons/Movies-Playlists.png'),
            xbmcgui.ListItem('DVD', 'DVD', 'Icons/Movies-Disc.png', 'Icons/Movies-Disc.png')
        ],
        'music': [
        ]
    }

    def onInit(self):
        self.state = self.STATE_MODULE_WINDOW
        self.mediaType = sys.argv[1]
        
        moduleTitleImage = self.getControl(MediaModuleWindow.CONTROL_MODULE_TITLE)
        moduleTitleImage.setImage(self.mediaType.capitalize() + '-Headline.png')
        
        self.mainList = self.getControl(MediaModuleWindow.CONTROL_MAIN_LIST)
        self.replaceList(self.mainList, self.LIST_ITEMS[self.mediaType])
        
        self.breadcrumb0 = self.getControl(MediaModuleWindow.CONTROL_BREADCRUMB_POSITION_0)
        self.breadcrumb1 = xbmcgui.ControlButton(0, 55, 105, 27, '', 'Module-Breadcrumb-Button-MainMenu-Selected.png', 'Module-Breadcrumb-Button-MainMenu-Normal.png')

        self.breadcrumb1.setAnimations([('WindowOpen', 'effect=slide tween=cubic time=600 delay=200 start=-100,0 end=0,0 acceleration=1.5')])
        # <control type="button" id="3000">
        #         <pulseonselect>no</pulseonselect>
        #   <hitrect x="0" y="55" w="90" h="28" />
        #     <aspectratio aligny="top">keep</aspectratio>
        #   <onclick>ReplaceWindow(0)</onclick>
        #   <onleft>3002</onleft>
        #   <onright>3001</onright>
        #     <onup>5000</onup>
        #     <ondown>5000</ondown>
        #     </control>

    
    def replaceList(self, listController, items):
        listController.reset()
        for i in items:
            listController.addItem(i)
        
    def onFocus(self, control):
        print "On Focus"
        print control
        return
        
    def onAction(self, action):
        if action.getId() == xbmcgui.ACTION_PREVIOUS_MENU:
            self.close()
        elif action.getId() == xbmcgui.ACTION_SELECT_ITEM:
            if (self.getFocus().getId() == self.mainList.getId()):
                self.onClick(self.mainList.getSelectedItem())
    
    def onClick(self, control):
        print "On Click"
        print control
        return
        
def main():
    try:
        window = MediaModuleWindow('template_MediaModule.xml', 'Q:\skin\CenterStage')
        window.doModal()
    except:
        xbmc.log('Exception (main): ' + str(sys.exc_info()[0]))
        traceback.print_exc()
    

if __name__ == "__main__":
    main()