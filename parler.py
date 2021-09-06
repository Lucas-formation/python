import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Entrer le mot ou la phrase à dire : ")
    s = input()
    speaker.Speak(s)