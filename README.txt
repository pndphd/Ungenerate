This plugin replicates ArcMaps "Ungenerate" command (http://desktop.arcgis.com/en/arcmap/10.3/tools/coverage-toolbox/ungenerate.htm).
It takes a shapefile input file and produces a text file with the x,y coordinates of each polygon.  
The x,y coordinates are preceded by a ID number for each polygon and followed by the word "end" before the next polygon's coordinates
are printed.  The file ends with another "end" statement.  The following is a example output for a shape file with 4 polygons
each with 5 vertexes.

1     2923.3222656      2084.7429199
       2917.0759277      2079.6772461
       2926.8261719      2089.6940918
       2929.4162598      2089.6560059
       2918.4470215      2078.3823242
       2917.0759277      2079.6772461
END
3     2936.2717285      2087.4851074
       2929.4162598      2089.6560059
       2942.2133789      2087.4470215
       2942.0610352      2084.7048340
       2930.1779785      2087.5612793
       2929.4162598      2089.6560059
END
4     2937.0334473      2081.5056152
       2942.0610352      2084.7048340
       2941.4516602      2076.0590820
       2934.9006348      2073.7739258
       2930.1779785      2087.5612793
       2942.0610352      2084.7048340
END
END
Instruction
Peter Dudley
4/3/2017
1) Selected a vector grid form the drop down menu.
2) Select a file destination and name.  The program will append “.Data” to the file name. 
