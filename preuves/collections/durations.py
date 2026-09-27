#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calcule la duree reelle de chaque MP3 en parcourant les trames (MPEG-1 Layer III)."""
import os, struct, json, sys

BR = {1:32,2:40,3:48,4:56,5:64,6:80,7:96,8:112,9:128,10:160,11:192,12:224,13:256,14:320}
SR1 = {0:44100,1:48000,2:32000}
SR2 = {0:22050,1:24000,2:16000}
SAMPLES = {3:1152, 2:576, 0:576}   # MPEG1 / MPEG2 / MPEG2.5 Layer III

def duree(path):
    with open(path,'rb') as f:
        d = f.read()
    i, n = 0, len(d)
    if d[:3] == b'ID3':
        sz = (d[6]<<21)|(d[7]<<14)|(d[8]<<7)|d[9]
        i = 10 + sz
    total = 0.0
    while i < n - 4:
        if d[i] == 0xFF and (d[i+1] & 0xE0) == 0xE0:
            h = struct.unpack('>I', d[i:i+4])[0]
            ver = (h >> 19) & 3
            layer = (h >> 17) & 3
            if layer != 1 or ver == 1:      # on ne traite que Layer III
                i += 1; continue
            bri = (h >> 12) & 0xF; sri = (h >> 10) & 3; pad = (h >> 9) & 1
            if bri in (0, 15) or sri == 3:
                i += 1; continue
            br = BR[bri] * 1000
            sr = (SR1 if ver == 3 else SR2)[sri]
            spf = SAMPLES[ver]
            total += spf / sr
            i += int(spf / 8 * br / sr) + pad   # 144 = 1152/8 pour MPEG1
        else:
            i += 1
    return total

if __name__ == '__main__':
    aud = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'audio')
    out = {}
    for f in sorted(os.listdir(aud)):
        if f.endswith('.mp3'):
            out[f[:-4]] = round(duree(os.path.join(aud, f)), 1)
    tgt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'durations.json')
    json.dump(out, open(tgt, 'w'), ensure_ascii=False, indent=0)
    t = sum(out.values())
    print(len(out), 'pistes ·', round(t/60, 1), 'min · moy', round(t/len(out), 1), 's')
    for k, v in list(out.items())[:5]:
        print('  ', k, v)
