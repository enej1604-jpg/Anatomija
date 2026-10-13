from PIL import Image; import numpy as np, glob, json, os
out={}
for f in sorted(glob.glob('img/*.jpeg')):
    name=os.path.basename(f)[:-5]
    im=Image.open(f).convert('RGB'); a=np.array(im).astype(int)
    m=(abs(a[:,:,0]-200)<=6)&(abs(a[:,:,1]-200)<=6)&(abs(a[:,:,2]-202)<=6)
    H,W=m.shape
    boxes=[]
    # horizontal lines: rows with long runs; check in left half and right half separately
    for x0,x1 in [(0,W//2),(W//2,W)]:
        seg=m[:,x0:x1]
        rows=[y for y in range(H) if seg[y].sum()>400]
        # cluster rows
        lines=[]
        for y in rows:
            if lines and y-lines[-1][-1]<=2: lines[-1].append(y)
            else: lines.append([y])
        ys=[l[0] for l in lines]
        # find x extent of each line
        ext=[]
        for y in ys:
            xs=np.where(seg[y])[0]; ext.append((y,xs.min()+x0,xs.max()+x0))
        # pair consecutive lines with similar extents as top/bottom
        i=0
        while i+1<len(ext):
            (ya,xa,xb),(yb,xc,xd)=ext[i],ext[i+1]
            if abs(xa-xc)<5 and abs(xb-xd)<5 and yb-ya>60:
                boxes.append((xa,ya,xb,yb)); i+=2
            else: i+=1
    boxes.sort(key=lambda b:(b[1]//50,b[0]))
    res=[]
    for k,(x0,y0,x1,y1) in enumerate(boxes,1):
        im.crop((x0+2,y0+2,x1-1,y1-1)).save(f'panels/{name}-{k}.png')
        res.append([int(x0),int(y0),int(x1),int(y1)])
    out[name]=res
    print(name,len(res),res)
json.dump(out,open('boxes.json','w'))
