import os, re, shutil, sys, codecs, time, datetime
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Gets a system argument from VBA. It is then used as the date limit.
#code uses this date limit to find anything created after that date.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\.


Import_Tracker_Date= sysargv1 
#------------------------------------------------------------------------------
#--------------------------------Functions-------------------------------------

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
#
#   Function used to crawl across the directories to find the case folder.
#   It gets the date in which the case folder was created, along with
#   file path, and database and stores it into variables that are then placed
#   in a list that is returned when the function is called.
#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#------------------------------------------------------------------------------


def Folder_names (path):
    date_limit=datetime.datetime.strptime(Import_Tracker_Date,"%Y%m%d")
    folder_names=[]
    folders = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            folders.extend([name])
    for i in folders:
        f_path=path+'\\'+i
        t = os.path.getctime(f_path)
        created_date = datetime.datetime.fromtimestamp(t)
        if created_date > date_limit:
            Time= (created_date)
            Time=datetime.datetime.strftime(Time,"%Y-%m-%d")
            Db= f_path.split('\\')[1]

            if "VIP" in Db:
                Db=Db.split("Loadfiles_")[1]
            else:
                if "UK" in Db:
                    Db='Castle_UK'
                else:
                    Db=Db.split("_")[1]
            folder_names.extend([(path+'\\'+i + '+'+Db+'+' + str(Time))])
    return folder_names

#------------------------------------------------------------------------------
#-----------------------------------Main---------------------------------------
Castle="H:\\Loadfiles_Castle\\30_Loadfiles"
CastleVIP= "H:\\Loadfiles_Castle_VIP\\VIP_Loadfiles"
Donau="H:\\Loadfiles_Donau\\30_Loadfiles"
DonauVIP="H:\\Loadfiles_Donau_VIP\\30_VIP_Loadfiles"
CastleUK="H:\\Loadfiles_Castle_UK\\30_Loadfiles"


file_path= 'I:\\RDM_Share\\temp\\Andres\\Import\\Folder Checks'
timestr = time.strftime("%d.%m.%Y")


#------------------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
#       Code will "crawl" through the directories and find the folder that
#       has the case name. It will then strip the file path until the only
#       part of the string left is the actual Case ID. It will then write
#       the case ID, Date Created, Database, and File path.
#

#           Please note that the code is separated by each Database to
#           account for different naming conventions, and subfolders
#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------

#               Code for Castle
#------------------------------------------------------------------------------

path=Castle
with open(os.path.join(file_path,'Import_Folders_' + timestr + '.txt'),'w') as result:
    result.write('Folder+Database+Time+Case' + '\n')
    Caselist= Folder_names(path)
    for i in Caselist:
        if not "DU" in i:
            path2=i.split("+")[0]
            Caselist2= Folder_names(path2)
            for x in Caselist2:
                if not "DU" in x:
                    path3=x.split("+")[0]
                    Caselist3= Folder_names(path3)
                    for z in Caselist3:
                        if "DU" in z:
                            z=z.replace(" ", "")
                            case3=z.split("_(")[0]
                            case3=case3.split('\\')[5]
                            case3=case3.replace(" ", "")
                            result.write (z + '+' + case3+ '\n')
            else:
                x=x.replace(" ", "")
                case2=x.split("_(")[0]
                case2=case2.split('\\')[4]
                case2=case2.replace(" ", "")
                result.write(x+ '+' + case2+ '\n')
        else:
            i=i.replace(" ", "")
            case=i.split("_(")[0]
            case=case.split("\\")[3]
            case=case.replace(" ", "")
            result.write(i+ '+' + case+ '\n')
            
#------------------------------------------------------------------------------

#               Code for Castle VIP
#------------------------------------------------------------------------------
            
    path=CastleVIP
    Caselist= Folder_names(path)
    for i in Caselist:
        if not "DU" in i:
            path2=i.split("+")[0]
            Caselist2= Folder_names(path2)
            for x in Caselist2:
                if not "DU" in x:
                    path3=x.split("+")[0]
                    Caselist3= Folder_names(path3)
                    for z in Caselist3:
                        if "DU" not in z:
                            path4=z.split('+')[0]
                            Caselist4= Folder_names(path3)
                            for w in Caselist4:
                                if "DU" in w:
                                    w=w.replace(" ", "")
                                    case4=w.split("_(")[0]
                                    case4=case4.split('\\')[5]
                                    case4=case4.replace(" ", "")
                                    result.write (w + '+' + case4+ '\n')
                        else:
                            z=z.replace(" ", "")
                            case3=z.split("_(")[0]
                            case3=case3.split('\\')[5]
                            case3=case3.replace(" ", "")
                            result.write (z + '+' + case3+ '\n')
            else:
                x=x.replace(" ", "")
                case2=x.split("_(")[0]
                case2=case2.split('\\')[4]
                case2=case2.replace(" ", "")
                result.write(x+ '+' + case2+ '\n')

        else:
            i=i.replace(" ", "")
            case=i.split("_(")[0]
            case=case.split("\\")[3]
            case=case.replace(" ", "")
            result.write(i+ '+' + case+ '\n')

#------------------------------------------------------------------------------

#               Code for Castle UK
#------------------------------------------------------------------------------


    path=CastleUK
    Caselist= Folder_names(path)
    for i in Caselist:
        if not "UK" in i:
            path2=i.split("+")[0]
            Caselist2= Folder_names(path2)
            for x in Caselist2:
                if not "UK" in x:
                    path3=x.split("+")[0]
                    Caselist3= Folder_names(path3)
                    for z in Caselist3:
                        if "UK" in z:
                            z=z.replace(" ", "")
                            case3=z.split("_(")[0]
                            case3=case3.split('\\')[5]
                            result.write (z + '+' + case3+ '\n')
            else:
                x=x.replace(" ", "")
                case2=x.split("_(")[0]
                case2=case2.split('\\')[4]
                result.write(x+ '+' + case2+ '\n')

        else:
            i=i.replace(" ", "")
            case=i.split("_(")[0]
            case=case.split("\\")[3]
            result.write(i+ '+' + case+ '\n')

#------------------------------------------------------------------------------

#               Code for Donau
#------------------------------------------------------------------------------
    path=Donau
    Caselist= Folder_names(path)
    for i in Caselist:
        if not "DU" in i:
            path2=i.split("+")[0]
            Caselist2= Folder_names(path2)
            for x in Caselist2:
                if not "DU" in x:
                    path3=x.split("+")[0]
                    Caselist3= Folder_names(path3)
                    for z in Caselist3:
                        if "DU" in z:
                            z=z.replace(" ", "")
                            case3=z.split("_(")[0]
                            case3=case3.split('\\')[5]
                            result.write (z + '+' + case3+ '\n')
                else:
                    x=x.replace(" ", "")
                    case2=x.split("_(")[0]
                    case2=case2.split('\\')[4]
                    result.write(x+ '+' + case2+ '\n')

        else:
            i=i.replace(" ", "")
            case=i.split("_(")[0]
            case=case.split("\\")[3]
            result.write(i+ '+' + case+ '\n')

#------------------------------------------------------------------------------

#               Code for Donau VIP
#------------------------------------------------------------------------------


    path=DonauVIP
    
    Caselist= Folder_names(path)
    for i in Caselist:
        if not "DU" in i:
            path2=i.split("+")[0]
            Caselist2= Folder_names(path2)
            for x in Caselist2:
                if not "DU" in x:
                    path3=x.split("+")[0]
                    Caselist3= Folder_names(path3)
                    for z in Caselist3:
                        if "DU" in z:
                            z=z.replace(" ", "")
                            case3=z.split("_(")[0]
                            case3=case3.split('\\')[5]
                            result.write (z + '+' + case3+ '\n')
            else:
                x=x.replace(" ", "")
                case2=x.split("_(")[0]
                case2=case2.split('\\')[4]
                result.write(x+ '+' + case2+ '\n')

        else:
            i=i.replace(" ", "")
            case=i.split("_(")[0]
            case=case.split("\\")[3]
            result.write(i+ '+' + case+ '\n')
print ("Check complete!! Please find the file in:" + file_path)
