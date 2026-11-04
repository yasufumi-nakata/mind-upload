#!/usr/bin/env python3
"""Render an original conceptual research diagram for link previews."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
fig,ax=plt.subplots(figsize=(12,6.3),dpi=100)
fig.patch.set_facecolor('#0b1422');ax.set_facecolor('#0b1422')
ax.set_xlim(0,1200);ax.set_ylim(0,630);ax.axis('off');fig.subplots_adjust(0,0,1,1)
ax.text(65,550,'MIND UPLOADING',color='#72e2cd',fontsize=20,weight='bold')
ax.text(65,446,'From brain data\nto testable models.',color='#e8edf7',fontsize=36,weight='bold',linespacing=1.25,va='top')
ax.text(65,208,'Measurement. Reconstruction.\nIdentification. Independent validation.',color='#b7c8dd',fontsize=18,linespacing=1.6,va='top')
ax.text(65,65,'RESEARCH GUIDE  /  NOVEMBER 2026',color='#85a4c7',fontsize=13)
positions=[(825,470),(960,498),(1060,405),(910,350),(770,355),(815,245),(1030,260),(930,188)]
for a,b in [(0,1),(0,3),(0,4),(1,2),(1,3),(2,3),(2,6),(3,4),(3,5),(3,6),(4,5),(5,7),(6,7)]:
 x,y=positions[a];u,v=positions[b];ax.plot([x,u],[y,v],color='#386280',lw=2,zorder=1)
for i,(x,y) in enumerate(positions):
 ax.scatter(x,y,s=700 if i==3 else 270,color='#72e2cd' if i%2==0 else '#94baff',edgecolor='#193a51',linewidth=4,zorder=2)
ax.add_patch(FancyBboxPatch((747,83),350,54,boxstyle='round,pad=8,rounding_size=10',facecolor='#183048',edgecolor='#446884'))
ax.text(922,103,'MEASURE → MODEL → TEST',color='#e8edf7',fontsize=15,ha='center')
fig.savefig(ROOT/'assets/og-image.png',dpi=100,facecolor=fig.get_facecolor())
fig.savefig(ROOT/'assets/og-image.svg',facecolor=fig.get_facecolor())
svg_path = ROOT/'assets/og-image.svg'
svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
plt.close(fig)
