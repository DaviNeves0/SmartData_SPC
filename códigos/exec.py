from cx_Freeze import setup, Executable

base = "Win32GUI"
 
setup(name='SmartData',
    version='1.0',
    description='Análise de fontes',
    options={'build_exe': {'packages': ['pandas', 'numpy', 'plotly','xlrd', 'jinja2', 'PIL']}},
    executables = [Executable(script='SmartData.py'
                              ,base=base,
                              icon='./icones/icon.ico')
                   ]
      )
