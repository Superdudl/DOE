# -*- mode: python ; coding: utf-8 -*-
import sys
import os
import glob

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
    *[
            (f, '.')
            for f in glob.glob(os.path.join(sys.prefix, 'Library', 'bin', '*.*'))
            if os.path.isfile(f)
        ],
    ],
    datas=[('src', 'src'), ('settings', 'settings')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='СПО',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='СПО',
)
