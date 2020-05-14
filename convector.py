import os
from moviepy.editor import VideoFileClip
print("Введите номер читающего:")
nam = int(input())
print("Введите с какой строки начали читать:")
line = int(input())
print("Ваши видео уже переименнованы?(Y/N):")
nm = input()
print("Ваши видео уже в mp4(Y/N):")
mp = input()




def rename(path,form,line):
    listOfFiles = os.listdir(path)

    countOfFiles = len(listOfFiles)

    os.chdir(path)

    for i in range(0, countOfFiles):
        os.rename(path + listOfFiles[i], str(nam) + "." + str(i + line) + form)


def convectormp4(path,path2,line):
    listOfFiles = os.listdir(path)

    countOfFiles = len(listOfFiles)

    def sortlen(list):
        return len(list)

    sortlen(listOfFiles)
    listOfFiles.sort(key=sortlen)

    for i in range(0, countOfFiles):

        clip = VideoFileClip(path + listOfFiles[i])

        clip.write_videofile(path2 + str(nam) + "." + str(i + line) + '.mp4')


def convectorwap(path,line):
    listOfFiles = os.listdir(path)

    countOfFiles = len(listOfFiles)

    def sortlen(list):
        return len(list)

    sortlen(listOfFiles)
    listOfFiles.sort(key=sortlen)

    for i in range(0, countOfFiles):
        clip = VideoFileClip(path + listOfFiles[i])
        clip.audio.write_audiofile(path + str(nam) + "." + str(i+line) + '.wav', ffmpeg_params=["-ac", "1"], fps=16000)

if nm == "N" and mp == "N":
    print("Введите формат оригинальной записи(.mov,.webp, и ид(с точкой)")
    form = input()
    print("Введите абсолютный адрес папки с видео(все слеши такие /. Пример: C:/Users/Andrey/PycharmProjects/speech): ")
    path = input()
    path = path + "/"
    print("Введите абсолютный адрес папки для конвертированных видео(все слеши такие /. Пример: C:/Users/Andrey/PycharmProjects/speech): ")
    path2 = input()
    path2 = path2 + "/"
    listOfFiles = os.listdir(path)
    print("Проверьте, в списке названия файлов идут в правильном порядке?(Y/N):")
    print(listOfFiles)
    er = input()
    if er == "Y":
        rename(path,form,line)
        convectormp4(path, path2,line)
        convectorwap(path2,line)


if nm == "Y" and mp == "Y":
    print("Введите абсолютный адрес папки с видео(все слеши такие /. Пример: C:/Users/Andrey/PycharmProjects/speech): ")
    path = input()
    path = path + "/"
    convectorwap(path,line)

if nm == "N" and mp == "Y":
    print("Введите формат оригинальной записи(.mov,.webp, и ид(с точкой)")
    form = input()
    print("Введите абсолютный адрес папки с видео(все слеши такие /. Пример: C:/Users/Andrey/PycharmProjects/speech): ")
    path = input()
    path = path + "/"
    print("Проверьте, в списке названия файлов идут в правильном порядке?(Y/N):")
    listOfFiles = os.listdir(path)
    print(listOfFiles)
    er = input()
    if er == "Y":
        rename(path,form,line)
        convectorwap(path,line)


if nm == "Y" and mp == "N":
    print("Введите абсолютный адрес папки с видео(все слеши такие /. Пример: C:/Users/Andrey/PycharmProjects/speech): ")
    path = input()
    path = path + "/"
    print("Введите абсолютный адрес папки для конвертированных видео(все слеши такие /. Пример: C:/Users/Andrey/PycharmProjects/speech): ")
    path2 = input()
    path2 = path2 + "/"
    convectormp4(path, path2,line)
    convectorwap(path2,line)




