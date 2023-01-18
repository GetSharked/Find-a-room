from GUI import GUI
from Arkusz import Arkusz
import webbrowser


GUI.Interfejs(GUI)
Arkusz.Interface(Arkusz)
Arkusz.WpiszCeneNaTeraz(Arkusz)

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open('https://docs.google.com/spreadsheets/d/1CjPKKB2bpZ3dmhVqhs2xUj-Z6CFTeim0rHAv8MVHeoI/edit#gid=0')