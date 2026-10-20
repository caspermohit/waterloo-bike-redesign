import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def solve(rows,vals):
 m=[list(map(float,r))+[float(v)]for r,v in zip(rows,vals)]
 for i in range(3):
  z=m[i][i];m[i]=[v/z for v in m[i]]
  for j in range(3):
   if j!=i:
    z=m[j][i];m[j]=[a-z*b for a,b in zip(m[j],m[i])]
 return [m[i][3]for i in range(3)]
rows=[[993,349,1],[1230,377,1],[1470,56,1]]
ax=solve(rows,[160,350,535]);ay=solve(rows,[472,489,250]);A=[ax[0],ay[0],ax[1],ay[1],ax[2],ay[2]]
def mapped(x,y):return [ax[0]*x+ax[1]*y+ax[2],ay[0]*x+ay[1]*y+ay[2]]
def matrix(a):return a
def similarity(a,b,c,d):
 ux,uy=b[0]-a[0],b[1]-a[1];vx,vy=d[0]-c[0],d[1]-c[1];den=ux*ux+uy*uy;s=(vx*ux+vy*uy)/den;r=(ux*vy-uy*vx)/den
 return [s,r,-r,s,c[0]-s*a[0]+r*a[1],c[1]-r*a[0]-s*a[1]]
seat=mapped(1164,137);bb=[350,489];seat_top=[seat[i]+(seat[i]-bb[i])*.50 for i in range(2)]
parts={
'rear':{'box':[38,8,437,426],'matrix':similarity([256,225],[456,225],[160,472],[310,472])},
'front':{'box':[529,8,438,427],'matrix':similarity([745,226],[945,226],[639,472],[789,472])},
'frame':{'box':[970,8,540,400],'matrix':matrix(A)},
'fork':{'box':[135,432,237,345],'matrix':similarity([197,521],[330,763],[545,282],[639,472])},
'saddle':{'box':[600,476,308,290],'matrix':similarity([807,747],[745,562],seat,seat_top)},
'cockpit':{'box':[1005,561,482,161],'matrix':similarity([1194,688],[1261,600],[523,220],[539.75,198])},
'drive':{'box':[70,776,775,237],'matrix':similarity([144,842],[555,866],[160,472],[350,489])}}
(ROOT/'tools/photo-parts-v8.json').write_text(json.dumps({'source':'assets/bicycle-photo-parts-v8.png','size':[1536,1024],'parts':parts,'mounts':{'rear':[160,472],'front':[639,472],'bottomBracket':bb,'seatCollar':seat,'headTop':mapped(1460,23),'headBottom':mapped(1481,87)}},indent=2))
print('mounts',seat,mapped(1460,23),mapped(1481,87))
js='''// Complete photographic components, aligned by mechanical mounts. No subtraction masks.
(()=>{const spec='''+json.dumps(parts)+''';
let defs='<defs>';for(const[id,p]of Object.entries(spec)){defs+=`<clipPath id="photo-piece-${id}" clipPathUnits="userSpaceOnUse">${id==='rear'?'<circle cx="256" cy="225" r="208"/>':id==='front'?'<circle cx="745" cy="226" r="208"/>':`<rect x="${p.box[0]}" y="${p.box[1]}" width="${p.box[2]}" height="${p.box[3]}"/>`}</clipPath>`}defs+='</defs>';
window.realisticBicyclePart=id=>{const p=spec[id];return `${id==='rear'?defs:''}<g transform="matrix(${p.matrix.join(' ')})"><g clip-path="url(#photo-piece-${id})"><image href="/assets/bicycle-photo-parts-v8.png" x="0" y="0" width="1536" height="1024"/></g></g>`};
window.bicycleAssembledPhoto='';
})();
'''
(ROOT/'dist/realistic-bicycle.js').write_text(js)
