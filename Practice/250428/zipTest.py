import zipfile

#비주얼코드를 기준으로 열었던 폴더. 즉, 현재 하이어라키에서 가장 상위에 해당하는 곳을 기준으로 path를 잡을 것
with zipfile.ZipFile("Practice/myFile.zip", "w") as mzip:
    mzip.write("Practice/myError.py")
    mzip.write("Practice/pickle.pickle")

with zipfile.ZipFile("Practice/myFile.zip") as mzip:
    mzip.extractall()