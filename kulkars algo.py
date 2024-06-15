import matplotlib.pyplot as plt
import networkx as nx
g=nx.Graph()
v=int(input())
ne=int(input())
vrt=[]
ed=[]
for x in range(v):
    vrt.append(x)
for x in range(ne):
    a,b,c=tuple(map(int,input().split()))
    ed.append((a,b,c))
mp={}
for x in range(v):
    mp[x]=x
wp={}
for a,b,c in ed:
    wp[(b,c)]=a
w=[]
for x in wp.values():
    w.append(x)
w.sort()
vis=[]
for x in w:
    c=0
    q=0
    for y in wp.items():
        i,j=y
        v1,v2=i
        if x==j:
            if mp[v1]!=mp[v2]:
                if i not in vis:
                    vis.append(i)
                for z in mp.items():
                    k,l=z
                    if q==0:
                        a=mp[v2]
                        q+=1
                    if l==a:
                        mp[k]=mp[v1]
                        c+=1
        if c!=0:
            break
min_cost=0
for x in vis:
    for i,j in wp.items():
        if x==i:
            min_cost+=j
print(min_cost)
g.add_nodes_from(vrt)
g.add_edges_from(vis)
nx.draw(g,with_labels=True)
plt.show()
