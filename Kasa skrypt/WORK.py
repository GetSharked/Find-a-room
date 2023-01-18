import shutil

shutil.copy('1.txt', '../')

str = 'C:\MW_CI_Logs\\2023-01-12_14-51-34\logs\\node0\\1011_startup\startup_DEFAULT'

dest = str - str[-29:-1]
print(str)