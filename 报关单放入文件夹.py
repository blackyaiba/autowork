import os
import shutil

bgd_path = r'\\192.168.128.10\报关\出口报关单'
baoguandans_contents = os.walk(bgd_path)
bgdlist = []
for root, dirs, bgdspdf in baoguandans_contents:
    for bgdtxt in bgdspdf:
        # print('baoguandantxt: ', bgdtxt)
        baoguandanlist = os.path.splitext(bgdtxt)[0]
        # print('baoguandanlist: ', baoguandanlist)
        bgdlist.append(baoguandanlist)

#print('bgdlist:', bgdlist)

ifbgdexist=os.path.exists(bgd_path)

jg_path = r'C:\Users\shilanqian\Desktop\5月结关'
jgs_contents = os.walk(jg_path)
for root2, jgs, files in jgs_contents:
    for jg in jgs:
        #print('jg:', jg)
        singlejg = os.path.splitext(jg[4:13])[0]
        #print('singlejg:', singlejg)
        if singlejg in bgdlist:
                if os.path.exists(bgd_path + '\\' + singlejg + '.pdf'):
                    shutil.copy(bgd_path + '\\' + singlejg + '.pdf', jg_path + '\\' + jg + '\\'+singlejg+'报关单'+'.pdf')
                    print(singlejg+'.pdf'+'报关单已放入')
                else:
                    print(singlejg+'.pdf'+'报关单缺失')