import os
import csv

# Gets input for all the paths 
def get_inputs():
    allpaths = dict()
    print("Enter path to CSV:")
    allpaths['csv']= input()
    print("Enter path to images:")
    allpaths['images']= input()
    print("Enter output path for new images:")
    allpaths['output'] = input()
    
    return allpaths

# Finds image in folder with filename and path of directory as arguments
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

#Runs exiftool command
def update_exif(image_path, out_path, value, filename):
    # Command creates a new image in different folder path with updated exif data
    os.system(f'exiftool -TagsFromFile {image_path} -Title={value} -o {out_path}/{filename} {image_path}')
    print(f'----Created new image({filename}) with updated title metadata')

def main():
    paths = get_inputs()

    with open(paths['csv'], newline='') as csvfile:
        checklist = csv.DictReader(csvfile)

        # Loop through the rows in the csv file
        for row in checklist:
            filename = row['Image Filename (jpg)'] + '.jpeg'
            objectid = row['\ufeffObjectID']
            filepath = find(filename, paths['images'])

            if filepath:
                update_exif(filepath, paths["output"], objectid, filename)

if __name__ == "__main__":
    main()