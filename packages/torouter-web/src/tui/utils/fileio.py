import os

def write(files):
  tmpfiles = []
  for file in files:
    tmpfile = "/tmp/" + file[0].split("/")[-1:][0] + ".tmp"
    tmpfiles.append((tmpfile,file[0]))
    # open the tmp file for write
    f = open(tmpfile, 'w')
    # write the data (file[1]) to the temp file
    f.write(file[1])
    f.close()

  # rename all the file. This operation is atomic
  for file in tmpfiles:
    os.rename(file[0], file[1])

# for testing
#files = [('/tmp/file1','blablbal'),('/tmp/file2','The content'),('/tmp/file3','The content 3')]
#write(files)

