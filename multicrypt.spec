# -*- mode: python -*-

block_cipher = None


a = Analysis(['multicrypt.py'],
             pathex=['/Users/Ron/Dropbox/Ron/src/multicrypt'],
             binaries=[],
             datas=[('wordlist/english.txt', 'wordlist')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Multicrypt',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Multicrypt')
#app = BUNDLE(exe,
#         name='Multicrypt',
#         icon='icons/multicrypt.icns',
#         bundle_identifier=None)