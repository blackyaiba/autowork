import os
import shutil

cw_path = r'\\192.168.128.10\报关\报关文件'
cws_contents = os.walk(cw_path)
cwlist = []
for root, dirs, cwspdf in cws_contents:
    for bgdtxt in cwspdf:
        # print('baoguandantxt: ', bgdtxt)
        baoguandanlist = os.path.splitext(bgdtxt)[0]
        # print('baoguandanlist: ', baoguandanlist)
        cwlist.append(baoguandanlist)

#print('bgdlist:', bgdlist)

ifbgdexist=os.path.exists(cw_path)

jg_path = r'C:\Users\shilanqian\Desktop\5月结关'
jgs_contents = os.walk(jg_path)
for root2, jgs, files in jgs_contents:
    for jg in jgs:
        #print('jg:', jg)
        singlejg = os.path.splitext(jg[14:22])[0]
        #print('singlejg:', singlejg)
        if singlejg in cwlist:
                if os.path.exists(cw_path + '\\' + singlejg + '.pdf'):
                    shutil.copy(cw_path + '\\' + singlejg + '.pdf', jg_path + '\\' + jg + '\\' + singlejg + '场位' + '.pdf')
                    print(singlejg+'.pdf'+'场位图已放入')
                else:
                    print(singlejg+'.pdf'+'场位图缺失')
