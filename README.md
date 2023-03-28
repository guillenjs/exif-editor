# Exif Editor
Script that can be used to add exif data to images. This specific script can update the title field but can be adapted for any other exif field.

## Installaton
Clone repo:
```
git clone git@github.com:guillenjs/exif-editor.git
``` 

Requires exiftool to be installed on machine:
- [Homebrew install](https://formulae.brew.sh/formula/exiftool)
- [Exiftool installs](https://exiftool.org/install.html)

## Running Script

Command: 
```
python3 update_exif.py 
```

Script requires three inputs. The csv path, image folder path, and the output folder path.
Example:
```
Enter path to CSV:
    sample.csv
Enter path to images:
    ./images
Enter output path for new images:
    ./images/edited
```




# exif-editor
