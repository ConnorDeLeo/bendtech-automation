# bendtech-automation
An automation tool for Bend-Tech.

# How it works
## Run process
When the script is run, you will be prompted for the name of the assembly, the default material and die, and the points you would like to add.

### `2point.py`
`2point.py` is the first iteration of my Bend-Tech automation system. It supports `2` points and up to `3` digits in each coordinate. Does not support decimals. As of `8/24/2023`, `2point.py` is currently in v1.0 and does not have a GUI.

### `encryptor.py`
`encryptor.py` is the first iteration of the Bend-Tech encryption system, see `Encryption system` below. Supports up to `3` digits, does not support decimals.

### `main.py`
`main.py` is the main iteration of the system. It takes in however many points you require and all of their locations. Does not support decimals. As of `10/20/2023`, `main.py` is in v1.1 and has a working TKinter based GUI. Only accepts `.csv | Comma Separated Value` filetypes with `3` columns and `1` row for header information. See the `Bend-Tech Automation Test.csv` file or `CSV Format` for a formatting guide. The limit for points has not been tested, and may only stop when there is a lack of memory.

## File format
The `.btax` (Bend-Tech assembly) file format is just a plain text file automatically associated with the program.

## Point format
The format within the `.btax` files is quite odd.
All coordinate numbers are encrypted using an extremely simple system (I assume to persuade people not to tamper with their files) shown below in `Encryption system`, colors are also encrypted.

## CSV Format
All point instruction files in CSV format should contain `3` columns, with a `1` row header. See below for format:
```
mat,die,name
X0,Y0,Z0
X1,Y1,Z1
X1,Y2,Z2
```

## Encryption system
### Points
The encryption system happens at the save point of a `.btax` file! The time spent decoding their encryption system is useless for now as when importing the file, it iterates all values for points by `3`.

The rules are quite odd, for digits `0-6` simply add `3` (i.e. `2` would change into `5`). Digits `7-9` are replaced with special characters, `7` to `:`, `8` to `;`, and `9` to `<`. If you're wondering "why did they choose these characters?", I'm not sure either. When reaching double digits it gets especially odd, the same rules apply to the second digit, but the digits get flipped and the first digit is added to `3` and placed behind the second digit (i.e. `10` becomes `34`, `20` becomes `35`, `90` becomes `3<`, so on and so forth). Triple digits like to switch it up a bit. When encrypting, the last digit that goes in comes out as the first digit, but with `2` added to it. The second encrypted digit is the second input digit with `3` added to it. The last encrypted digit is the first input digit with `3` added to it. For example, `100` becomes `233`, `110` becomes `243`, and `179` becomes `<:3`, weird isn't it?

### IDs
The ID always stays at `0`, encrypted to `3` using the same system as above. The parent ID does change, again using the same system as above, but linearly, doesn't seem to assign a meaningful value just a linear number.

### Colors
Colors are encrypted from the user input (in either `HSL` or `RGB`) to `hexidecimal` then into `32-bit`. Quite boring compared to the points encryption system, but a color with an `RGB` of `0,128,0` becomes `008000` in `hexidecimal` and then `-16744448` in `base 32`.

# Updates
## New versions
### `README.md`
Launched on `8/24/2023` with an explanation of Bend-Tech's number and color encryption system, file format, run process explanation, and `2point.py`.
### `2point.py`
v1.0 launched on `8/24/2023` with basic features and `3` digit support.
### `2point.py`
v1.0 moved to `/tool/test` on `9/4/2023`.
### `main.py`
v1.0 launched on `9/4/2023` with point features.
### General
Encryption happens on save of a `.btax` file inside Bend-Tech. The encryption system I wrote is temporarily useless. A possible use is for modifying existing `.btax` files.
### `README.md`
Updated on `9/4/2023` with an explanation of `main.py` and an encryption discovery. Slightly more in depth on `2point.py`.
### `main.py`
Updated to v1.1 on `10/20/2023` with a new TKinter based GUI. Accepts only `.csv` filetypes.
### `README.md`
Updated on `10/20/2023` with new features in `main.py` and an example of how to write the `.csv` point files.