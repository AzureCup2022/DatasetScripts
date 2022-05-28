# locato_data

Data collector of Azure Cup Locato Project. The output format is the json with parameters name, color and data, which is the list of json objects of long, lat, radius and intensity.

```json
{ name: "Pollution in the area", color: "red", data: [ { lat: 14.496728031692513, long: 50.02016417623482 radius: 12.5, intensity: 0.401 }, ] }
```

## Usage
Specify arguments (elments of list of folders in ./data/geoportalpraha you want to be processed). Collect the data by running the shell command

```sh
python collect_data.py
```

## Output files
Output files are generated in the root directory with the *.json* extension. The name of the generated file is the same as its source folder. 

### Data Sources
Noise: 

 - https://www.geoportalpraha.cz/en/data/opendata/0AABB791-6C9B-4C9E-9262-2E3C48633EE5
 - https://www.geoportalpraha.cz/en/data/opendata/F2207E6B-A08F-4BF3-97FF-9695D32D6384
 - https://www.geoportalpraha.cz/en/data/opendata/BEE29CD7-98BA-4EB9-AB3D-079E6E338563
 - https://www.geoportalpraha.cz/en/data/opendata/86489214-950D-4347-941E-C714F5F9E55B

Safety:

 - https://www.geoportalpraha.cz/en/data/opendata/4A14E013-3B9D-4270-BEBE-64944C3DFA19
 - https://www.geoportalpraha.cz/en/data/opendata/D7283D97-3909-4684-BA99-8FECCACBC2A6

Bad Atmosphere:
 - https://www.geoportalpraha.cz/en/data/opendata/5BB4E2C5-9D4B-4B2B-BF0A-E0B98EE6013A

ToDo
 - https://docs.microsoft.com/en-us/azure/open-datasets/dataset-catalog ( Taxi locations, Genomics Data Lake or US Population by Country 