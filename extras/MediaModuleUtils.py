import os
import pickle
import sys
import traceback

import xbmcgui
import xbmc

class MediaModuleWindow(xbmcgui.WindowXML):
    CONTROL_MODULE_TITLE          = 4010
    CONTROL_MAIN_LIST             = 4000
    CONTROL_BREADCRUMB_BUTTON0    = 3000

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

    def pushBreadcrumb(self, name):
        xbmc.lock()
        try:
            # Create background
            # Create label
            # Push to list
            # Add to window
            # Add animation
            self.breadcrumbs.append(crumb)
        finally:
            xbmc.unlock()
        return
        
    def popBreadcrumb(self):
        if len(self.breadcrumbs) == 0:
            print 'Trying to pop nonexistent breadcrumb.'
            return
            
        xbmc.lock()
        try:
            crumb = self.breadcrumbs[-1]
            self.remove(-1)
            self.removeControl(crumb.label)
            self.removeControl(crumb.button)
            del crumb.label
            del crumb.button
            
            # crumb.setAnimation(...)
            # crumb.runAnimation(...)
            # 
            # onAnimationComplete should catch
            # remove from list
            # Run animation
            # Wait until done
            # remove from window
            # Destroy background
            # Destroy label
        finally:
            xbmc.unlock()
        return

    def onAnimationComplete(self, control):
        if control:
            self.removeControl(control)
            del control
        return
        
    def onInit(self):
        xbmcgui.lock()
        
        try:
            self.state = self.STATE_MODULE_WINDOW
            self.mediaType = sys.argv[1]
            self.breadcrumbs = []
        
            # self.controlGroup = xbmcgui.ControlGroup(0,0,125,100);
            # self.controlGroup.addControl(xbmcgui.ControlLabel(0, 0, 125, 75, 'Status', angle=45))
            # self.addControl(self.controlGroup)
            
            moduleTitleImage = self.getControl(MediaModuleWindow.CONTROL_MODULE_TITLE)
            moduleTitleImage.setImage(self.mediaType.capitalize() + '-Headline.png')
        
            self.mainList = self.getControl(MediaModuleWindow.CONTROL_MAIN_LIST)
            self.replaceList(self.mainList, self.LIST_ITEMS[self.mediaType])

            # <control type="button" id="3000">
            #     <animation effect="slide" tween="cubic" time="600" delay="200" start="-105,0" end="0,0" acceleration="+1.5">WindowOpen</animation>
            #     <pulseonselect>no</pulseonselect>
            #     <posx>0</posx>
            #     <posy>55</posy>
            #     <width>105</width> 
            #     <height>27</height>
            #     <hitrect x="0" y="55" w="90" h="28" />
            #     <aspectratio aligny="top">keep</aspectratio>
            #     <texturefocus>Module-Breadcrumb-Button-MainMenu-Selected.png</texturefocus>
            #     <texturenofocus>Module-Breadcrumb-Button-MainMenu-Normal.png</texturenofocus>
            #     <onclick>ReplaceWindow(0)</onclick>
            #     <onleft>3006</onleft>
            #     <onright>3001</onright>
            #     <onup>5000</onup>
            #     <ondown>5000</ondown>
            #     <enable>Control.IsVisible(3001)</enable>
            # </control>
            # 
            self.button = 0
        finally:
            xbmcgui.unlock()

    def onAction(self, action):
        if action.getId() == xbmcgui.ACTION_PREVIOUS_MENU:
            self.close()
        elif action.getId() == xbmcgui.ACTION_SELECT_ITEM:
            if (self.getFocus().getId() == self.mainList.getId()):
                self.onClick(self.mainList.getSelectedItem())
    
    def onClick(self, controlId):
        if controlId == self.mainList.getId():
            print "On Click: " + str(controlId)
            self.pushBreadcrumb('MainMenu')
        return

    def onFocus(self, controlId):
        print "On Focus: " + str(controlId)
        self.button = xbmcgui.ControlButton(88, 55, 105, 27, '', focusTexture='Module-Breadcrumb-Button-MainMenu-Selected.png', noFocusTexture='Module-Breadcrumb-Button-MainMenu-Normal.png')
        print "Bread Crumb: "
        self.breadcrumb = self.getControl(MediaModuleWindow.CONTROL_BREADCRUMB_BUTTON0)
        print self.breadcrumb
        self.insertControl(self.button, self.breadcrumb, True)
        return
    
    def replaceList(self, listController, items):
        listController.reset()
        for item in items:
            listController.addItem(item)

def main():
    try:
        window = MediaModuleWindow('template_MediaModule.xml', 'Q:\skin\CenterStage')
        window.doModal()
        del window
    except:
        xbmc.log('Exception (main): ' + str(sys.exc_info()[0]))
        traceback.print_exc()

if __name__ == "__main__":
    main()