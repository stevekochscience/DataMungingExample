CircStatsYear.py is an example of a data munging script I've used recently at work. Previously, someone was processing exported text files from an old library circulation system (Millennium) and creating an Excel spreadsheet summary by manually searching the text files and then copying by hand. This was tedious and subject to error. I was unable to connect to the Millennium database programmatically. The end product also needed to be viewable in Excel. So, the script I created reads the exported text files and creates a new CSV file that will open in Excel and look the same as the previous Excel summaries.

* The exported millennium files have been renamed to "2013_01.txt" etc. (01 = January)
* These files should be in the directory named in fnambase
* The year should be specified in the YEAR string
* The output file will be based on year, e.g. "2013.csv"

I have included the input files for 12 months of 2013. I have also included what should be the output CSV file as `2013_ex.csv`. If the code runs correctly, the output file, `2013.csv` should be identical.

To run the code, type `python CircStatsYear.py`

I have included this code as an example for the 2014 April "data munging" session for the ABQ Python Meetup. I didn't add any extra commenting or try to make the code efficient or anything--so it should have lots of deficiencies and room for criticism! But it's a real example of something that works (for now!) and saves people time at the Library. :)
