"""Original ambient instrumental generated for this invitation. No copyrighted recordings."""
import numpy as np
from scipy.signal import fftconvolve
import soundfile as sf
from pathlib import Path
sr=24000; duration=48; N=sr*duration
rng=np.random.default_rng(119)
L=np.zeros(N,dtype=np.float64);R=np.zeros(N,dtype=np.float64)

def add(t,y,pan=0):
 s=int(t*sr);e=min(N,s+len(y));
 if e<=s:return
 y=y[:e-s]; L[s:e]+=y*np.sqrt((1-pan)/2);R[s:e]+=y*np.sqrt((1+pan)/2)

def env(n,a=.04,r=.45):
 t=np.arange(n)/sr
 return np.minimum(1,t/max(a,.001))*np.minimum(1,(n/sr-t)/max(r,.001))

# tanpura-like floating open-fifth drone
for freq,lev in [(146.832,.028),(220,.021),(293.665,.016)]:
 t=np.arange(N)/sr
 vib=.002*np.sin(2*np.pi*.17*t)
 w=2*np.pi*freq*(t+vib)
 signal=lev*(np.sin(w)+.27*np.sin(w*2)+.12*np.sin(w*3)+.06*np.sin(w*4))
 signal*=.75+.22*np.sin(2*np.pi*.051*t+.2)
 add(0,signal,-.3 if freq<200 else .3)

notes={'D3':146.83,'G3':196.,'A3':220.,'B3':246.94,'C#4':277.18,'D4':293.665,'E4':329.63,'F#4':369.99,'G4':392,'A4':440,'B4':493.88,'C#5':554.37,'D5':587.33,'E5':659.25,'F#5':739.99}

def string(freq,span=2.8):
 n=int(span*sr);t=np.arange(n)/sr
 mod=(.9+np.sin(2*np.pi*1.9*t)*.05)
 wav=(np.sin(2*np.pi*freq*t)+.7*np.sin(2*np.pi*2.008*freq*t)+.48*np.sin(2*np.pi*3.005*freq*t)+.16*np.sin(2*np.pi*4.001*freq*t))
 return wav*np.exp(-t*2.0)*np.minimum(t/.011,1)*mod*.047

def flute(freq,span):
 n=int(span*sr);t=np.arange(n)/sr
 w=2*np.pi*freq*t + 0.32*np.sin(2*np.pi*5.1*t)*(1-np.exp(-t*6))
 signal=(np.sin(w)+.23*np.sin(2*w)+.085*np.sin(3*w))
 breath=rng.standard_normal(n)
 # low-pass noise for breathiness
 breath=np.convolve(breath,np.ones(45)/45,'same')
 signal+=.05*breath
 return signal*env(n,.25,.32)*.068

# soft arpeggiated gold plucks
bpm=75; beat=60/bpm
chords=[['D4','F#4','A4','D5'],['B3','D4','F#4','B4'],['G3','B3','D4','G4'],['A3','C#4','E4','A4']]
for bar in range(15):
 chord=chords[bar%4]
 for j,idx in enumerate([0,2,1,3,2,1,0,2]):
  when=bar*4*beat+j*beat*.5
  if when>duration-2:continue
  y=string(notes[chord[idx]],2.3)
  add(when,y,.4*np.sin(bar*1.2+j*1.8))
  if j in (0,4):add(when+.06,string(notes[chord[0]]/2,2.5)*.35,-.4)
# sparse reed melody in original sequence
mel=[('D4',0,2),('F#4',2,1.5),('A4',4,2),('B4',7,1.2),('A4',9,1.7),('F#4',11.3,2),('E4',14.3,1.6),('D4',16.2,2.6),('A4',19,1.2),('B4',21,1.2),('C#5',23,1.7),('D5',25,3),('B4',29,2.4),('A4',33,1.8),('F#4',36,2),('E4',39.5,2),('D4',42.3,3.1)]
for note,when,span in mel:add(when,flute(notes[note],span),-.25 if when%2 else .2)
# subtle low warm skin drum heartbeat
for when in np.arange(0,duration,4*beat):
 n=int(.32*sr);t=np.arange(n)/sr
 k=np.sin(2*np.pi*(90-22*t)*t)*np.exp(-t*19)*.016
 add(when,k,-.18)
# Stereo ambience generated with synthetic impulse response, avoid external recordings
for track,seed in ((L,44),(R,45)):
 rg=np.random.default_rng(seed); ir=np.zeros(int(1.5*sr));
 for delay,amp in [(0.043,.10),(.081,.073),(.15,.06),(.28,.032),(.53,.022),(.89,.011)]:
  j=int(delay*sr);ir[j]=amp
 tail=rg.standard_normal(len(ir))*np.exp(-np.arange(len(ir))/sr*4)*.00015
 ir+=tail
 wet=fftconvolve(track,ir,'full')[:N]
 track+=wet
mix=np.stack([L,R],1)
mix*=.92/max(np.max(np.abs(mix)),1)
# smooth fade in and out, seamless enough since intro track loops
fadein=np.minimum(np.arange(N)/sr/2,1)
fadeout=np.minimum((N-1-np.arange(N))/sr/3,1)
mix*=np.minimum(fadein,fadeout)[:,None]
path=Path(__file__).parent/'assets'/'celebration-soundscape.wav'
sf.write(path,mix,sr,subtype='PCM_16')
print(path,path.stat().st_size)
