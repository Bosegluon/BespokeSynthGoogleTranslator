from google_trans_new import google_translator  
  
translator = google_translator()  
txt_tables=[]
f = open("tooltips.txt", "r",encoding='utf-8')
line = f.readline()
while line:
    txt_tables.append(line)
    line = f.readline() 
print(txt_tables)
sss=[]

for i in txt_tables:
    q=i[0:-1].split('~')
    sss.append(q)
ppp=[]
for i in sss:
    if i[-1]!='[todo]':
        o=translator.translate(i[-1],lang_tgt='jp') #Change to your desired language
        i[-1]=o
    sd=''
    if len(i)==1:
        
        sd="\n"
    else:
        for oioio in range(len(i)):
            if oioio!=len(i):
                sd=sd+i[oioio]+'~'
        sd=sd[0:-1]
        sd+='\n'
    print(sd)
    ppp.append(sd)
print(ppp)
f = open("tooltips_translate.txt", "w",encoding='utf-8')
f.writelines(ppp)
f.close()
