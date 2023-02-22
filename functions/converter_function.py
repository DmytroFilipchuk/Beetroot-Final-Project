

def converter_voice_msg(audio):
    import subprocess

    current_file_name = audio
    final_file_name = 'ConvertedByFFeelMusicBot.mp3'

    try:
        subprocess.call(['ffmpeg', '-i', f'{current_file_name}', f'{final_file_name}'])

    except Exception as e:
        print(e)
        print('Error While Converting Audio')

    return final_file_name
