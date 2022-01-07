import sys
import zipfile
import io


data = io.BytesIO()

for line in sys.stdin:
    if '' == line.rstrip():
        break

    data.write(bytes.fromhex(line))

z = zipfile.ZipFile(data)

cnt = 0
vol = 0
for info in z.infolist():
    vol += info.file_size
    if not info.is_dir():
        cnt += 1

print(cnt, vol)
