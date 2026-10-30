"""Rebuild bill-checker/index.html from CMS public files.

Usage: python make.py <data-dir>
<data-dir> must hold dl/PPRRVU2026_Oct_nonQPP.csv and dl/OPPSCAP_Oct.csv (from the CMS RVU26D zip)
and clfs/PUF_CLFS_CY2026_Q4V1.csv (from the CMS 26CLABQ4 zip).
Each January, swap in the new year's files, conversion factor and GPCI values.
"""
import csv, json, os, sys
D=os.path.join(sys.argv[1] if len(sys.argv)>1 else '.', '')
W,PE,MP=1.000,0.965,1.686  # GPCI2026 MI locality 01 Detroit
CF=33.4009
def f(x):
    try: return float(x)
    except: return 0.0
cap={}
for r in csv.reader(open(D+'dl/OPPSCAP_Oct.csv',encoding='latin-1')):
    if len(r)>6 and r[3]=='08202' and r[4]=='01':
        cap[(r[0],r[1])]=(f(r[5]),f(r[6]))
pfs={}; ncap=0
rows=list(csv.reader(open(D+'dl/PPRRVU2026_Oct_nonQPP.csv',encoding='latin-1')))
for r in rows[10:]:
    if len(r)<26 or not r[0]: continue
    code,mod,st=r[0].strip().upper(),r[1].strip().upper(),r[3].strip()
    k=code+('-'+mod if mod else '')
    if st in ('A','R','T'):
        w,npe,fpe,mp=f(r[5]),f(r[6]),f(r[8]),f(r[10])
        fac=None if r[9].strip()=='NA' else round((w*W+fpe*PE+mp*MP)*CF,2)
        non=None if r[7].strip()=='NA' else round((w*W+npe*PE+mp*MP)*CF,2)
        c=cap.get((code,mod))
        if c:
            ncap+=1
            if fac is not None: fac=min(fac,c[0])
            if non is not None: non=min(non,c[1])
        pfs[k]=[st,fac,non]
    else:
        pfs[k]=[st]
clfs={}
for r in csv.DictReader([l for l in open(D+'clfs/PUF_CLFS_CY2026_Q4V1.csv',encoding='latin-1')][4:]):
    if r['MOD'].strip(): continue
    c=r['HCPCS'].strip().upper()
    if c not in clfs or r['EFF_DATE']>clfs[c][1]:
        clfs[c]=(round(f(r['RATE']),2),r['EFF_DATE'])
clfs={k:v[0] for k,v in clfs.items()}
print(len(pfs),len(clfs),ncap,file=sys.stderr)
for t in ['99213','99214','71046','71046-26','93000','80053','85025','36415','99285','J1100']:
    print(t,pfs.get(t),clfs.get(t),file=sys.stderr)
data=json.dumps({'pfs':pfs,'clfs':clfs},separators=(',',':'))
here=os.path.dirname(os.path.abspath(__file__))
tpl=open(os.path.join(here,'template.html')).read()
open(os.path.join(here,'index.html'),'w').write(tpl.replace('__DATA__',data))
