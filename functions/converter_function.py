

def converter_voice_msg(audio):
    import subprocess

    CurrentFileName = audio
    FinalFileName = 'Твоє голосове повідомлення.mp3'

    try:
        subprocess.call(['ffmpeg', '-i', f'{CurrentFileName}', f'{FinalFileName}'])

    except Exception as e:
        print(e)
        print('Error While Converting Audio')

    return FinalFileName









