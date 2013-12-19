# -*- mode: python -*-
a = Analysis(['SmoothPlayer.py'],
             pathex=['C:\\Users\\weiche2\\workspace\\python\\SmoothPlayer'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas += [('vplayer_latest.xap','vplayer_latest.xap','DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SmoothPlayer.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='images.ico')
