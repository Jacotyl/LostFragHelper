
# LostFragHelper
A simple script to help with the dumping of assets from the Aquaplus game Utawarerumono: Lost Frag, which allows the game files to be easily imported and dumped via
[AssetStudio](https://github.com/Perfare/AssetStudio).

## Installation

Place the LostFragHelper.py script in the dl folder from your copied Lost Frag install, so it is in the same directory as the Background, CharacterTex, Equipment, etc folders. 


## Usage
Simply run the script via terminal in the proper folder with:
```
python LostFragHelper.py
```



After running the script, the modified files will be placed alongside their originials
with the .pack_XOR extension.

Open the dl folder in [AssetStudio](https://github.com/Perfare/AssetStudio).

It is recommended that before extracting the files via [AssetStudio](https://github.com/Perfare/AssetStudio), that the "Group exported assets by" option is changed to "container path" for the file structure to remain intact for the exported assets. 

## Planned Features
- Automated composition of sprite faces + bodies after extraction.
