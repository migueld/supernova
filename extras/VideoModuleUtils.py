import xbmc, xbmcgui

def setVisibility(oldId, newId):
    window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    oldControl = window.getControl(int(oldId))
    newControl = window.getControl(int(newId))
    oldControl.setVisible(False)
    newControl.setVisible(True)
    window.setFocusId(newId)
    
def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "switch":
            if len(sys.argv) == 4:
                setVisibility(sys.argv[2], sys.argv[3])
            else:
                print "Error: `" + command + "` requires controlId as arguments (only ", sys.argv, ")." 
        else:
            print "Error: `" + command + "` not recognized." 

    # <onclick>RunScript(Q:\skin\CenterStage\extras\VideoModuleUtils.py,library)</onclick>

if __name__ == "__main__":
    main()

