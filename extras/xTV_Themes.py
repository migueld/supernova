
import xbmc, xbmcgui
import urllib,re

base_url = "http://skin-downloads.googlecode.com/svn/trunk/Skin%20Themes/xTV_themes.xml"
base_download = "http://skin-downloads.googlecode.com/svn/trunk/Skin%20Themes/xTV"
def ping(host):
    import socket,time
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    t1=float(0)
    t2=float(0)
    t1 = float(time.time()*1000)
    try:
        s.connect(( host, 80 ))
        t2 = float(time.time()*1000)
        s.close()
        del s
        return int((t2 - t1))
    except socket.error, (errcode, errmsg):
        t2 = time.time()
        if errcode == 111:
            return int((t2 - t1))
        else:
            return None


def DownloaderClass(url,dest,name):
    dp = xbmcgui.DialogProgress()
    dp.create("xTV Themes","Downloading Theme:",name)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
    try:
        dp.close()
        xbmcgui.Dialog().ok('xTV Themes',"Theme Installed","  ","Go to Appereance Settings to apply.")
        return 1
    except:
        dp.close()
        xbmc.executebuiltin('XBMC.Notification(xTV Themes,Download Cancelled)')
        return 0

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/float(filesize), 100)
        dp.update(int(percent))
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled():
        raise IOError

def getList():
    WebSock = urllib.urlopen(base_url)  # Opens a 'Socket' to URL
    WebHTML = WebSock.read()            # Reads Contents of URL and saves to Variable
    WebSock.close()
    try:
        ItemList = re.compile('<themename>(.*)</themename><path>(.*)</path><filename>(.*)</filename>', re.IGNORECASE).findall(WebHTML) # Using find all mentions of
    except:
        return [],[],[]
    filename_list = []
    path_list = []
    themename_list = []
    for x in ItemList:
        filename_list.append(x[2])
        path_list.append(x[1])
        themename_list.append(x[0])
    return themename_list,filename_list,path_list

def main():
    themename_list,filename_list,path_list = getList()
    if not themename_list == []:
        retval = xbmcgui.Dialog().select('xTV Themes',themename_list)
        if retval == -1:
            return
        else:
            DownloaderClass(path_list[retval],"Q:\\skin\XTV\media\\" + filename_list[retval],themename_list[retval])
    

if __name__ == "__main__":
    main()

