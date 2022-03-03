# CrystalReportFinder
Given a file path, it will recursively scour the subfolders and files finding all .rpt and .rrd files.

The filepath and output location can be modified on lines 6 & 7. 
This script creates a text file that is "^" delimited


Sample Output: Results.txt
```
RRD Path ^ RPT Path ^ Report Type ^ destination address(es) or path
P:\folder1\rrdFile.rrd^P:\folder1\folder2\report.rpt^SaveReport^[reportName]^P:\folder1\folder2\outputFile.xls
P:\folder1\rrdFile.rrd^P:\folder1\folder2\report.rpt^EmailReport^[reportName]^joe@mama.org
```
