## ml-netclean

<br>

#### 👉🏼 this package cleanses complex networks data, extracted from the [ml-graph-network-analyser](https://github.com/autistic-symposium/ml-graph-network-analyser)
#### 👉🏼 the final cleansed data files can then be ingested into the [mlnet-complex-networks](https://github.com/autistic-symposium/mlnet-complex-networks) project


<br>

----

### overview


#### 1. cleansing the data

* here we get all the outputs from **[ml-graph-network-analyser](https://github.com/autistic-symposium/ml-graph-network-analyser)** and put them together into vector files (separated by network type and sampling groups)
* these files must have a header (or missing values must be completed with `'-'`)

<br>

#### 2. organizing the data

* here, the files above are organized into vector files for each network
* an additional column for the classes is added
* the header is removed from these files
* missing values are completed with `0`

<br>

####  3. generating the final files

* here, the vectors files are read from the previous step to create a unified file for all the data

