import os 
import subprocess

#os.chdir("sources")

# Info
try:
    print("**** Running Fontmake ******************************")
    subprocess.call(['fontmake', '-g', 'sources/ha.glyphs', '-o', 'ttf',])
except:
    print("Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

# Info
print("**** Moving fonts to fonts directory *******************")
subprocess.call(['cp', 'master_ttf/ha.ttf', 'fonts/',])
print("**** [+] Done")

# Info
print("**** Removing build directories  ***********************")
subprocess.call(['rm', '-rf', 'master_ttf', 'master_ufo',])
print("**** [+] Done")


