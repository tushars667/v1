from pathlib import Path
from random import Random
from math import sin,cos,pi
p=Path(__file__).parent/'assets'; p.mkdir(exist_ok=True)
r=Random(86)

def svg(body,w=900,h=1300,defs='',bg=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff1ba"/><stop offset=".24" stop-color="#aa7937"/><stop offset=".46" stop-color="#eec988"/><stop offset=".72" stop-color="#795127"/><stop offset="1" stop-color="#f8d79d"/></linearGradient><linearGradient id="stone" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#c8aa7c"/><stop offset=".5" stop-color="#947356"/><stop offset="1" stop-color="#533f35"/></linearGradient><radialGradient id="moon"><stop stop-color="#fff7c3" stop-opacity=".9"/><stop offset=".42" stop-color="#ffe7a0" stop-opacity=".26"/><stop offset="1" stop-color="#ffd46d" stop-opacity="0"/></radialGradient><linearGradient id="dark" x2="0" y2="1"><stop stop-color="#0a2623"/><stop offset=".66" stop-color="#162e2a"/><stop offset="1" stop-color="#061411"/></linearGradient><filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="7"/></filter><pattern id="lattice" width="26" height="26" patternUnits="userSpaceOnUse"><path d="M13 0L26 13 13 26 0 13Z" fill="none" stroke="#bda174" stroke-width=".8" opacity=".48"/></pattern>{defs}</defs>{bg}{body}</svg>'''

stars=''.join(f'<circle cx="{r.randint(20,880)}" cy="{r.randint(15,960)}" r="{r.choice([.6,1,1.6,2.2])}" fill="#f3d8a1" opacity="{r.uniform(.25,.76):.2f}"/>' for _ in range(220))

def spire(x,y,scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})"><rect x="-70" y="0" width="140" height="245" fill="#8c7153" stroke="#d6ae6b" stroke-width="4"/><path d="M-80 0Q-70-60 0-90Q70-60 80 0Z" fill="#bc9459" stroke="#e9c184" stroke-width="4"/><path d="M-50-2Q-43-40 0-57Q43-40 50-2" fill="none" stroke="#f3d6a5" stroke-width="2"/><path d="M0-91V-118M-14-105Q0-134 14-105" fill="none" stroke="#ddb77b" stroke-width="4"/><rect x="-36" y="34" width="72" height="146" fill="#192b28" stroke="#ead0a5" stroke-width="4"/><path d="M-36 65Q0-7 36 65" fill="#192b28" stroke="#e4bb73" stroke-width="4"/><rect x="-36" y="65" width="72" height="108" fill="url(#lattice)"/></g>'

def lotus(x,y,s,fill='#dbac6f'):
    petals=''.join(f'<ellipse cx="0" cy="-27" rx="10" ry="29" transform="rotate({a})" fill="{fill}" opacity=".72" stroke="#6f4d31" stroke-width="1" />' for a in range(0,360,45))
    return f'<g transform="translate({x} {y}) scale({s})">{petals}<circle r="11" fill="#f6cf92"/><circle r="4" fill="#69472d"/></g>'

def palace_scene():
    parts=['<rect width="900" height="1300" fill="url(#dark)"/>', '<ellipse cx="450" cy="485" rx="340" ry="380" fill="url(#moon)"/>','<circle cx="450" cy="382" r="128" fill="#e2d0a2" opacity=".78"/>',stars]
    parts += ['<path d="M0 930Q130 790 280 895T600 850T900 885V1300H0Z" fill="#0a211e"/>', '<path d="M0 1110Q160 1010 340 1115T900 1070V1300H0Z" fill="#09221d"/>']
    parts += [spire(123,680,.9),spire(777,680,.9)]
    parts += ['<rect x="180" y="654" width="540" height="542" fill="#826548" stroke="#d3b27d" stroke-width="6"/>','<rect x="208" y="696" width="484" height="480" fill="url(#lattice)" opacity=".7"/>']
    parts += ['<path d="M170 662Q190 560 280 560Q337 480 450 477Q563 480 621 560Q710 560 730 662Z" fill="#ac8752" stroke="#eacc96" stroke-width="7"/>', '<path d="M224 639Q250 566 320 572Q352 514 450 513Q548 514 580 572Q650 566 676 639" fill="none" stroke="#e6bc7e" stroke-width="2"/>']
    # temple central jharokha arch
    parts += ['<path d="M273 1196V895Q273 806 335 763Q349 711 450 693Q551 711 565 763Q627 806 627 895V1196Z" fill="#112c27" stroke="url(#gold)" stroke-width="13"/>','<path d="M297 1196V901Q297 814 358 779Q380 733 450 722Q520 733 542 779Q603 814 603 901V1196" fill="none" stroke="#bb9764" stroke-width="4"/>','<path d="M323 1196V917Q323 849 380 799Q397 756 450 752Q503 756 520 799Q577 849 577 917V1196Z" fill="#153630" opacity=".93"/>']
    for x in range(210,700,63):
        parts += [f'<path d="M{x} 690V1158" stroke="#dbbd83" stroke-width="2" opacity=".2"/>']
    for x in (178,722):
        parts += [f'<rect x="{x-19}" y="671" width="38" height="527" fill="#d1a770" stroke="#623d26" stroke-width="3"/>',f'<path d="M{x-30} 665H{x+30}L{x+22} 690H{x-22}Z" fill="#e6bf83"/>']
    parts += ['<rect x="0" y="1157" width="900" height="143" fill="#102821"/><path d="M0 1157H900" stroke="#c09664" stroke-width="3"/>']
    # glowing steps
    for i in range(5):
        y=1180+i*29
        parts += [f'<path d="M{200-i*51} {y}H{700+i*51}" stroke="#b38e54" stroke-width="{2+i*.6}" opacity="{.75-i*.1}"/>']
    # foreground floral botanics
    for side in ('left','right'):
        x=36 if side=='left' else 864; flip=1 if side=='left' else -1
        parts += [f'<g transform="translate({x} 1130) scale({flip} 1)"><path d="M0 176Q100 8 122-123M0 145Q155 88 176 14M3 135Q82 7 18-85" stroke="#967b46" stroke-width="5" fill="none"/>']
        for j in range(8):
            xx=r.randint(0,170); yy=r.randint(-165,170)
            parts += [f'<path d="M{xx} {yy}q-35-18-28-44q35 4 28 44Z" fill="#365a48" stroke="#927748" stroke-width="1"/>',f'<path d="M{xx} {yy}q32-22 33-44q-34 0-33 44Z" fill="#51765c" stroke="#927748" stroke-width="1"/>']
        for j in range(6):
            xx=r.randint(12,135); yy=r.randint(-110,140); parts += [lotus(xx,yy,r.uniform(.31,.53), '#a66e69' if j%2 else '#cc9c68')]
        parts+=['</g>']
    # falling petals near edge
    for i in range(22):
        x=r.choice([r.uniform(0,150), r.uniform(750,900)]); y=r.uniform(380,1150)
        parts += [f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r.uniform(2,6):.1f}" ry="{r.uniform(5,11):.1f}" fill="#e4bc7e" opacity="{r.uniform(.26,.65):.2f}" transform="rotate({r.randrange(180)} {x:.1f} {y:.1f})"/>']
    return svg(''.join(parts))

(p/'palace.svg').write_text(palace_scene())

def scene(name, top,bottom,theme,moon=False):
    d=f'<linearGradient id="sky" x2="0" y2="1"><stop stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient>'
    arr=['<rect width="900" height="1100" fill="url(#sky)"/>']
    if moon:
        arr+=['<circle cx="710" cy="244" r="122" fill="url(#moon)"/>','<circle cx="710" cy="244" r="61" fill="#fbdfb4" opacity=".88"/>']
    for i in range(130):
        x=r.randint(0,900); y=r.randint(0,980)
        arr += [f'<circle cx="{x}" cy="{y}" r="{r.uniform(.3,2.2):.1f}" fill="#fae0b4" opacity="{r.uniform(.1,.65):.2f}"/>']
    # ornate arches
    arr+=['<path d="M0 0H900V1100H0Z" fill="none" stroke="#e6c284" stroke-opacity=".22" stroke-width="30"/>', '<path d="M94 1100V347Q94 198 199 172Q234 79 450 52Q666 79 701 172Q806 198 806 347V1100" stroke="url(#gold)" stroke-width="25" fill="none" opacity=".9"/>','<path d="M132 1100V358Q132 224 232 203Q274 120 450 92Q626 120 668 203Q768 224 768 358V1100" stroke="#deba81" stroke-width="2" fill="none" opacity=".8"/>']
    # woven canopy corner
    for x in range(145,850,92):
        arr+= [f'<path d="M{x} 130q-22 32 0 66q22-34 0-66" fill="{theme}" opacity=".65" stroke="#f5d6a3" stroke-width="1.4"/>']
    for i in range(13):
        x=42+i*68; y=r.randint(220,480)
        arr += [f'<circle cx="{x}" cy="{y}" r="{r.randint(3,6)}" fill="#ffe4a1" opacity=".76"/>', f'<path d="M{x} 0V{y}" stroke="#d9b573" stroke-opacity=".2"/>']
    if name=='sufi':
        arr += ['<path d="M80 790Q450 685 820 794V1100H80Z" fill="#101d39"/>','<path d="M90 871Q450 802 810 870" stroke="#dfaa6f" stroke-width="3" fill="none"/>']
        # strings canopy lights
        for j in range(3):
            y=490+j*45
            arr+=[f'<path d="M74 {y}Q450 {y+120} 824 {y}" stroke="#d9ae75" stroke-width="2" fill="none"/>']
            for i in range(15):
                x=75+i*53; ly=y+112*sin(pi*i/14)
                arr += [f'<circle cx="{x}" cy="{ly:.1f}" r="7" fill="#f5c877" opacity=".9"/><circle cx="{x}" cy="{ly:.1f}" r="16" fill="#f5c877" opacity=".15"/>']
        # swirling silhouette fabric
        arr+=['<path d="M340 800Q420 605 492 750Q560 820 719 864Q445 1063 236 877Z" fill="#9f2f5b" stroke="#e6a687" stroke-width="4"/><path d="M410 725Q412 670 450 672Q480 678 480 738" fill="#bd876e"/><circle cx="441" cy="648" r="29" fill="#c4977b"/><path d="M421 631Q450 590 470 627" fill="#201a26"/>','<path d="M273 840L333 652L382 646L431 858" fill="#a98357" stroke="#f1dba6" stroke-width="3"/><circle cx="353" cy="626" r="27" fill="#c49475"/>']
    elif name=='haldi':
        arr += ['<circle cx="450" cy="464" r="242" fill="#e8b854" opacity=".16"/>','<path d="M0 830Q450 680 900 845V1100H0Z" fill="#87663c"/>']
        for i in range(17):
            x=83+i*44; y=320+42*sin(i*.75)
            arr += [f'<circle cx="{x}" cy="{y:.1f}" r="17" fill="{r.choice(["#e9a828","#facf55","#cf791e"])}" stroke="#e8b26b" stroke-width="2"/>']
        for x in (180,720):
            arr += [f'<path d="M{x-98} 819L{x-77} 583Q{x} 466 {x+77} 583L{x+98} 819Z" fill="#e7b248" stroke="#f9e0a4" stroke-width="6"/>',f'<path d="M{x-96} 814L{x+96} 814" stroke="#ac6528" stroke-width="4"/>']
        # festive canopy
        arr+=['<path d="M230 750Q450 520 670 750Z" fill="#d99532" stroke="#f9d99b" stroke-width="6"/>']
        for x in range(250,700,60):
            arr+=[f'<path d="M{x} 700l25 44-27 7" fill="#9c4d38" opacity=".8"/>']
        for i in range(90):
            x=r.randint(80,820); y=r.randint(510,1020)
            arr += [f'<ellipse cx="{x}" cy="{y}" rx="4" ry="10" fill="{r.choice(["#f8cc6c","#e68a3e","#f8e4a5","#ab5f43"])}" opacity=".85" transform="rotate({r.randint(0,180)} {x} {y})"/>']
    elif name=='baraat':
        arr+=['<path d="M0 820Q260 735 450 782T900 755V1100H0Z" fill="#1d3228"/>']
        for i in range(6):
            x=130+i*125
            arr += [f'<path d="M{x} 820v-200" stroke="#e9bc6d" stroke-width="4"/><path d="M{x} 600l-31-35 31-42 31 42Z" fill="{r.choice(["#a44c3f","#b7894d","#7f8a58"])}" stroke="#edc48e" stroke-width="3"/>']
        # horse styled silhouette with plume
        arr+=['<path d="M170 862Q225 775 332 785L442 749Q478 734 518 760L553 684L620 683L662 734L634 762L578 756L557 901L534 919L509 818L450 858L361 864L312 984L281 979L292 860L231 891L223 995L195 996L180 898Z" fill="#eee2c8" stroke="#b68f61" stroke-width="7"/>','<path d="M563 676Q602 617 631 665Q605 652 601 718Z" fill="#c16a54"/>','<path d="M324 770l50-103 42 12 48 96" fill="#8c3f41" stroke="#e1ab72" stroke-width="6"/><circle cx="395" cy="642" r="34" fill="#ba8d69"/><path d="M365 634Q400 586 429 638" fill="#e8cf96"/>']
    elif name=='reception':
        arr+=['<path d="M74 903Q450 763 826 903V1100H74Z" fill="#3f1f2b"/>','<path d="M195 890V555Q211 434 450 420Q689 434 705 555V890" fill="none" stroke="#c4916d" stroke-width="25"/>','<path d="M238 881V563Q251 491 450 478Q649 491 662 563V881" fill="none" stroke="#f2cb9d" stroke-width="3"/>']
        for j in range(30):
            th=j*pi*2/30;x=450+260*cos(th);y=666+251*sin(th)
            if y<960 and 80<x<820:arr += [lotus(round(x,1),round(y,1),.45,'#cb7486' if j%2 else '#e6b49d')]
        arr+=['<path d="M356 872Q390 706 430 738L458 875" fill="#d1a37e"/><circle cx="402" cy="704" r="28" fill="#d3a381"/>','<path d="M420 870L472 719L516 735L553 870Z" fill="#e0ba78"/><circle cx="490" cy="697" r="30" fill="#c49470"/>']
        for x in range(220,770,110):
            arr += [f'<path d="M{x} 890v-78" stroke="#ab8a61" stroke-width="3"/><path d="M{x-11} 810q11-47 22 0Z" fill="#ffdd9b"/><circle cx="{x}" cy="800" r="22" fill="url(#moon)"/>']
    elif name=='wedding':
        arr+=['<path d="M85 867H815V1100H85Z" fill="#201d2a"/>']
        for x in (220,680):
            arr += [f'<rect x="{x-20}" y="365" width="40" height="540" fill="#ae835d" stroke="#f3cca1" stroke-width="6"/><path d="M{x-45} 360H{x+45}" stroke="#e5bd88" stroke-width="15"/>']
        arr+=['<path d="M177 378L235 260H665L723 378Z" fill="#944f50" stroke="#efb97e" stroke-width="9"/>']
        for x in range(215,701,54):
            arr += [lotus(x,340,.28,'#dba17f')]
        arr+=['<ellipse cx="450" cy="950" rx="214" ry="58" fill="#b9875e" opacity=".28"/>','<path d="M361 970L393 874H513L539 970Z" fill="#a16b4a" stroke="#d8aa6b" stroke-width="8"/>','<path d="M446 913Q387 873 427 830Q408 773 462 728Q458 798 500 814Q549 876 466 924Z" fill="#f9bc62"/><path d="M444 900Q411 857 454 815Q461 854 479 865Q485 888 444 900Z" fill="#fff0bd"/>','<circle cx="453" cy="843" r="87" fill="url(#moon)" opacity=".8"/>']
        for i in range(35):
            x=r.randint(100,790);y=r.randint(500,1020)
            arr += [f'<ellipse cx="{x}" cy="{y}" rx="3" ry="6" fill="#f7d6a1" opacity=".7" transform="rotate({r.randrange(180)} {x} {y})"/>']
    # front bottom flora
    for i in range(18):
        x=r.choice([r.randint(30,245),r.randint(655,870)]); y=r.randint(900,1140)
        arr += [lotus(x,y,r.uniform(.22,.47),r.choice(['#ce8c81','#e4b678','#caab80']))]
    return svg(''.join(arr),900,1100,d)

for nm,a,b,t,moon in [ ('sufi','#081535','#192347','#c97ba0',True),('haldi','#9b572c','#f7c779','#edab4a',False),('baraat','#173d30','#789071','#dca96d',False),('reception','#391a2b','#8b4d51','#edb6b0',False),('wedding','#181528','#49404f','#cc9070',True)]:
    (p/f'{nm}.svg').write_text(scene(nm,a,b,t,moon))
# simple divine motif: handmade ganesha line icon
(p/'ganesha.svg').write_text(svg('''<g fill="none" stroke="url(#gold)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" transform="translate(450 605)"><path d="M-97-78Q-165-212-241-138Q-287-47-173 0Q-212 58-147 115M97-78Q165-212 241-138Q287-47 173 0Q212 58 147 115"/><path d="M-87-145Q0-226 87-145M-123 24Q-125-78-61-130Q0-153 61-130Q125-78 123 24"/><path d="M0-115Q20-67 3-17Q-18 33 30 81Q74 134 6 167Q-55 173-45 118"/><path d="M-96-5Q-67-23-49-4M49-4Q67-23 96-5"/><path d="M-188 155Q-97 85-39 169Q0 185 39 169Q97 85 188 155M-162 163Q-200 235-91 264Q0 292 91 264Q200 235 162 163"/><path d="M-86-222L-37-265L0-218L37-265L86-222"/><circle cx="0" cy="-194" r="11" fill="#d2a45d" stroke="none"/></g><g fill="#e0ba77"><circle cx="340" cy="590" r="8"/><circle cx="560" cy="590" r="8"/></g>''',900,1100,bg='<rect width="900" height="1100" fill="none"/>'))
print('created:',*[f.name for f in p.glob('*.svg')])
