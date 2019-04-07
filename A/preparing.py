import os
from pathlib import Path


f = open(Path(os.path.abspath(__file__)).parent.__str__() + '/index.h', 'tw', encoding='utf-8')
f.write('int wtf(int);')
f.close()
