#SnowflakePy

The aim of this project is to create a database equivalent to snowflake in Python. I am greatly inspired by the data storage capability and implementation of Snowflake and the brilliant idea of using S3 as the main storage layer. I don't really know what is the files and folder structures that Snowflake utilizes to store the data but i would like to do a similar implementation of it using Python as my processing layer


###Files and folder structure:

<details>
<summary> Click on the dropdown for folder Structure</summary>

```plaintext
project_namespace/
│
├── database1/
│   ├── Table1/
│   │   ├── Column1/
│   │   │   ├── metadata.csv
│   │   │   ├── partition1.csv
│   │   │   ├── partition2.csv
│   │   │   └── partition3.csv
│   │   ├── Column2/
│   │   │   ├── metadata.csv
│   │   │   ├── partition1.csv
│   │   │   ├── partition2.csv
│   │   │   └── partition3.csv
│   │   └── Column3/
│   │       ├── metadata.csv
│   │       ├── partition1.csv
│   │       ├── partition2.csv
│   │       └── partition3.csv
│   │
│   └── Table2/
│       ├── Column1/
│       │   ├── metadata.csv
│       │   ├── partition1.csv
│       │   ├── partition2.csv
│       │   └── partition3.csv
│       ├── Column2/
│       │   ├── metadata.csv
│       │   ├── partition1.csv
│       │   ├── partition2.csv
│       │   └── partition3.csv
│       └── Column3/
│           ├── metadata.csv
│           ├── partition1.csv
│           ├── partition2.csv
│           └── partition3.csv
│
├── database2/
│   ├── Table3/
│   │   ├── Column1/
│   │   │   ├── metadata.csv
│   │   │   ├── partition1.csv
│   │   │   ├── partition2.csv
│   │   │   └── partition3.csv
│   │   ├── Column2/
│   │   │   ├── metadata.csv
│   │   │   ├── partition1.csv
│   │   │   ├── partition2.csv
│   │   │   └── partition3.csv
│   │   └── Column3/
│   │       ├── metadata.csv
│   │       ├── partition1.csv
│   │       ├── partition2.csv
│   │       └── partition3.csv
│   │
│   └── Table4/
│       ├── Column1/
│       │   ├── metadata.csv
│       │   ├── partition1.csv
│       │   ├── partition2.csv
│       │   └── partition3.csv
│       ├── Column2/
│       │   ├── metadata.csv
│       │   ├── partition1.csv
│       │   ├── partition2.csv
│       │   └── partition3.csv
│       └── Column3/
│           ├── metadata.csv
│           ├── partition1.csv
│           ├── partition2.csv
│           └── partition3.csv
│
└── database3/
    ├── Table5/
    │   ├── Column1/
    │   │   ├── metadata.csv
    │   │   ├── partition1.csv
    │   │   ├── partition2.csv
    │   │   └── partition3.csv
    │   ├── Column2/
    │   │   ├── metadata.csv
    │   │   ├── partition1.csv
    │   │   ├── partition2.csv
    │   │   └── partition3.csv
    │   └── Column3/
    │       ├── metadata.csv
    │       ├── partition1.csv
    │       ├── partition2.csv
    │       └── partition3.csv
    │
    └── Table6/
        ├── Column1/
        │   ├── metadata.csv
        │   ├── partition1.csv
        │   ├── partition2.csv
        │   └── partition3.csv
        ├── Column2/
        │   ├── metadata.csv
        │   ├── partition1.csv
        │   ├── partition2.csv
        │   └── partition3.csv
        └── Column3/
            ├── metadata.csv
            ├── partition1.csv
            ├── partition2.csv
            └── partition3.csv
```
</details>

