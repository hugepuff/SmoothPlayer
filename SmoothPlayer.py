###################
## Smooth Player WebPage Generator
###################
## V1.2
## With Pyinstaller single-file mode, update function to extract the smooth player vplayer_latest.xap from single exe file
###################
## V1.1
## Use specific server address
###################
## V1.0
## Only for specific Virtual server, more updates will be added if requires
## Rewrite Function addressReplace()
####################
## Wei Chen
## weiche2@cisco.com
####################

import shutil, os
#DATA Dictionary define
Dict_FTPtoHTTP={}
Dict_FTPtoHTTP["\\\\abr-nas2.cisco.com\\scratch\\"]='http://sbc-esx7-vm1.cisco.com/freenas/'

#FUNCTION for Pyinstaller
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

#FUNCTION address replacement
def addressReplace(addrDict,folderLoc):
#    folderLoc=folderLoc.replace("\\\\abr-nas2.cisco.com\\scratch\\",'http://sbc-esx7-vm1.cisco.com/freenas/')
#    folderLoc=folderLoc.replace('\\','/')
#    folderLoc+='/'
# stand address should be folder/name or folder\name. so we need to add a \
    folderLoc+='\\'
# check if the server is in the list
    for ftpAddr in addrDict.keys():
        if ftpAddr in folderLoc:
#test-- if we found that in the dict            print("good!")
            folderLoc=folderLoc.replace(ftpAddr,addrDict.get(ftpAddr))
            folderLoc=folderLoc.replace('\\','/')
            break    
    return folderLoc

#FUNCTION createHTML
def generateWebPage(address,filename):
    fileWebPage = open(filename[:-4]+".html",'w')
    fileWebPage.writelines("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n")
    fileWebPage.writelines("<html xmlns=\"http://www.w3.org/1999/xhtml\" >\n")
    fileWebPage.writelines("\n")
    fileWebPage.writelines("<head>\n")
    fileWebPage.writelines("    <title>Smooth Streaming Player</title>\n")
    fileWebPage.writelines("    <style type=\"text/css\">\n")
    fileWebPage.writelines("    html, body {\n")
    fileWebPage.writelines("        height: 100%;\n")
    fileWebPage.writelines("        overflow: auto;\n")
    fileWebPage.writelines("    }\n")
    fileWebPage.writelines("    body {\n")
    fileWebPage.writelines("        padding: 0;\n")
    fileWebPage.writelines("        margin: 0;\n")
    fileWebPage.writelines("    }\n")
    fileWebPage.writelines("    #silverlightControlHost {\n")
    fileWebPage.writelines("        height: 100%;\n")
    fileWebPage.writelines("        text-align:center;\n")
    fileWebPage.writelines("    }\n")
    fileWebPage.writelines("    </style>\n")
    fileWebPage.writelines("    <script type=\"text/javascript\">\n")
    fileWebPage.writelines("        function onSilverlightError(sender, args) {\n")
    fileWebPage.writelines("            var appSource = \"\";\n")
    fileWebPage.writelines("            if (sender != null && sender != 0) {\n")
    fileWebPage.writelines("              appSource = sender.getHost().Source;\n")
    fileWebPage.writelines("            }\n")
    fileWebPage.writelines("\n")
    fileWebPage.writelines("            var errorType = args.ErrorType;\n")
    fileWebPage.writelines("            var iErrorCode = args.ErrorCode;\n")
    fileWebPage.writelines("\n")
    fileWebPage.writelines("            if (errorType == \"ImageError\" || errorType == \"MediaError\") {\n")
    fileWebPage.writelines("              return;\n")
    fileWebPage.writelines("            }\n")
    fileWebPage.writelines("\n")
    fileWebPage.writelines("            var errMsg = \"Unhandled Error in Silverlight Application \" +  appSource + \"\\n\" ;\n")
    fileWebPage.writelines("")
    fileWebPage.writelines("            errMsg += \"Code: \"+ iErrorCode + \"    \\n\";\n")
    fileWebPage.writelines("            errMsg += \"Category: \" + errorType + \"       \\n\";\n")
    fileWebPage.writelines("            errMsg += \"Message: \" + args.ErrorMessage + \"     \\n\";\n")
    fileWebPage.writelines("\n")
    fileWebPage.writelines("            if (errorType == \"ParserError\") {\n")
    fileWebPage.writelines("                errMsg += \"File: \" + args.xamlFile + \"     \\n\";\n")
    fileWebPage.writelines("                errMsg += \"Line: \" + args.lineNumber + \"     \\n\";\n")
    fileWebPage.writelines("                errMsg += \"Position: \" + args.charPosition + \"     \\n\";\n")
    fileWebPage.writelines("            }\n")
    fileWebPage.writelines("            else if (errorType == \"RuntimeError\") {  \n")
    fileWebPage.writelines("                if (args.lineNumber != 0) {\n")
    fileWebPage.writelines("                    errMsg += \"Line: \" + args.lineNumber + \"     \\n\";\n")
    fileWebPage.writelines("                    errMsg += \"Position: \" +  args.charPosition + \"     \\n\";\n")
    fileWebPage.writelines("                }\n")
    fileWebPage.writelines("                errMsg += \"MethodName: \" + args.methodName + \"     \\n\";\n")
    fileWebPage.writelines("            }")
    fileWebPage.writelines("\n")
    fileWebPage.writelines("            throw new Error(errMsg);\n")
    fileWebPage.writelines("        }\n")
    fileWebPage.writelines("    </script>\n")
    fileWebPage.writelines("</head>\n")
    fileWebPage.writelines("<body>\n")
    fileWebPage.writelines("    <form id=\"form1\" runat=\"server\" style=\"height:100%\">\n")
    fileWebPage.writelines("    <div id=\"silverlightControlHost\">\n")
    fileWebPage.writelines("        <object data=\"data:application/x-silverlight-2,\" type=\"application/x-silverlight-2\" width=\"100%\" height=\"100%\">\n")
    fileWebPage.writelines("          <param name=\"source\" value=\"vplayer_latest.xap\"/>\n")
    fileWebPage.writelines("          <param name=\"onError\" value=\"onSilverlightError\" />\n")
    fileWebPage.writelines("          <param name=\"background\" value=\"white\" />\n")
    fileWebPage.writelines("          <param name=\"minRuntimeVersion\" value=\"4.0.50401.0\" />\n")
    fileWebPage.writelines("          <param name=\"autoUpgrade\" value=\"true\" />\n")
    fileWebPage.writelines("          <param name=\"enableGPUAcceleration\" value=\"true\" />\n")
    fileWebPage.writelines("                  <param name=\"InitParams\" value=\"IsStartPositionOffset=false,AutoPlay=true,mediaurl="+address+fileName+"/manifest\" />\n")
    fileWebPage.writelines("          <a href=\"http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50401.0\" style=\"text-decoration:none\">\n")
    fileWebPage.writelines("               <img src=\"http://go.microsoft.com/fwlink/?LinkId=161376\" alt=\"Get Microsoft Silverlight\" style=\"border-style:none\"/>\n")
    fileWebPage.writelines("          </a>\n")
    fileWebPage.writelines("        </object><iframe id=\"_sl_historyFrame\" style=\"visibility:hidden;height:0px;width:0px;border:0px\"></iframe></div>\n")
    fileWebPage.writelines("    </form>\n")
    fileWebPage.writelines("</body>\n")
    fileWebPage.writelines("</html>\n")
    fileWebPage.writelines("\n")
    fileWebPage.close()
#########################
#program runs starts here
#########################
#To find how many htmls need to create and what are those names. 
#Return the location of this current folder.
folderLocation = os.getcwd()
#Return the file list of the current folder
#3.3 fileList = os.listdir(path=folderLocation) 
fileList = os.listdir(folderLocation)
#prepare name to write into HTML
folderLocation = addressReplace(Dict_FTPtoHTTP,folderLocation)
#!!UPDATE POTENTIAL create a dictionary for store those new servers
# create a file result to list all ism file
#test--fileIsmvList = open('ismv_list.txt', 'w')
#iterate the file list
for fileName in fileList:
#choose ism file only
    if fileName[-3:] == "ism":
        generateWebPage(folderLocation, fileName)
#test--        fileName = folderLocation + fileName + "\n"
#test--        fileIsmvList.write(fileName)
#test--fileIsmvList.close()
#export Smooth player
playerFileName = "vplayer_latest.xap"
playerRelativeDir = ""
PlayerRelativeAddr = os.path.join(playerRelativeDir,playerFileName)
playerInternalFileAddr = resource_path(PlayerRelativeAddr)
shutil.copyfile(playerInternalFileAddr,PlayerRelativeAddr)
