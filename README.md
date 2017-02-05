## Note
This API is used to load Visual StoryTelling Dataset ([VIST](http://visionandlanguage.net/VIST/index.html)).
The dataset currently contains Description-in-Isolation (DII) and Story-in-Sequence (SIS) annotations.

## Download Dataset
```bash
# Change OUT_PATH to your preference directory, note the dataset is of big size ~300GB.
python download.py
# Download Description-in-Isolation dataset
wget http://visionandlanguage.net/VIST/json_files/description-in-isolation/DII-with-labels.tar.gz
# Download Story-in-Sequence dataset
wget http://visionandlanguage.net/VIST/json_files/story-in-sequence/SIS-with-labels.tar.gz
```

## Usage
The "vist.py" is able to load both DII and SIS datasets.
```bash
# locate your vist_directory, which contains images and annotations
vist_dir = '/playpen/data/vist'
# SIS instance
sis = vist.Story_in_Sequence(vist_dir)
# DII instance
dii = vist.Description_in_Isolation(vist_dir)
```





