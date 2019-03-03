# WAH Compression and Bitmap generation 
## CS 351 - Homework 4 - WSU Vancouver

### Overall
The program creates a sorted and unsorted bitmap index from a data file containing information about pets. Once the bitmap is created compress it using WAH 32 bit and 64 bit words. 

### Data 
Sample instance from the data file.

| Animal      | Age         | Adopted       |
| :---        |    :----:   |          ---: |
| Cat         | 12          | True          |
| Dog         | 68          | False         |
| Cat         | 68          | False         |

The attributes have the following domains:
- Animal: ['cat', 'dog', 'turtle', 'bird']
- Age: [1,100]
- Adopted: [True, False]

### Bitmap
The first four bits represent the animals

- Cat: "1000"
- Dog: "0100"
- Bird: "0010"
- Turtle: "0001"

The age is split into 10 bins raning 0-10,..., 90-100. Each bin is translated into 10 bits representing each bin.

Last two bits represent adoption status
- True: "10"
- False: "01"

### Requirements
Python 3

###  Executing
The file animals.txt is hard coded in the main section. 
Run the command
```sh
    python3 bitIndex.py
```
All the output is written to output folder. 

### Directory Tree
```
.
├── README.MD
├── bitIndex.py
├── data
│   ├── animals.txt
│   ├── animals_compressed_32.txt
│   ├── animals_compressed_sorted_32.txt
│   ├── animals_test.txt
│   ├── animals_test_bitmap.txt
│   ├── animals_test_bitmap_sorted.txt
│   └── animals_test_sorted.txt
└── output
    ├── animals_bitMap_sorted.txt
    ├── animals_bitMap_unsorted.txt
    ├── animals_bitmap.txt
    ├── animals_compressed_64.txt
    ├── animals_compressed_sorted_64.txt
    ├── animals_sorted.txt
    ├── animals_sorted_compressed_32.txt
    └── animals_unsorted_compressed_32.txt
```