# Fault localization - Defects4j

Dataset is from Defects4j, available here: (https://github.com/rjust/defects4j).


The techniques that are used are:

* Tarantula
* Ochiai
* Opt2
* Barinel
* Dstar2
* Muse
* Jaccard

Steps:

1) Open Terminal 

2) Go to Phd-FL (eg: cd Users/Desktop/Phd-FL )

3) Make sure in the Phd-FL folder consist of coverage folder, suspiciousness folder and   
   suspiciousness.py program 

4) coverage folder contains spectra(matrix) and coverage for each bug in each program.

5) The suspiciousness values can be generated using `suspiciousness.py` file. Run suspiciousness as follow:
   eg : python3 suspiciousness.py --data-dir /Users/nadhra/Downloads/Phd_research/Nadhra_paper_coding/1_Fault_Localization/coverage --output-dir /Users/nadhra/Downloads/Phd_research/Nadhra_paper_coding/1_Fault_Localization/suspiciousness --formula ochiai
   (formula 'all' can be replace with {muse,all,ochiai,tarantula,dstar2,jaccard,barinel,opt2} if only want to use specific technique and not all).

6) In suspiciousness file output will generated for formula that has been requested.

7) To extract more coverage and spectra file perform this task:
	eg: pid="Math"
	    bid="1"
            wget http://fault-localization.cs.washington.edu/data/$pid/$bid/gzoltar-files.tar.gz -O $pid-$bid-gzoltar-files.tar.gz








