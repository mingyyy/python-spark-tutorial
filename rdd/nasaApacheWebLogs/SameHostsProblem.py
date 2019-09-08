from pyspark import SparkContext, SparkConf


def isNotHeader(line: str):
    return not (line.startswith("host") and "bytes" in line)


if __name__ == "__main__":

	'''
    "in/nasa_19950701.tsv" file contains 10000 log lines from one of NASA's apache server for July 1st, 1995.
    "in/nasa_19950801.tsv" file contains 10000 log lines for August 1st, 1995
    Create a Spark program to generate a new RDD which contains the hosts which are accessed on BOTH days.
    Save the resulting RDD to "out/nasa_logs_same_hosts.csv" file.

    Example output:
    vagrant.vf.mmc.com
    www-a1.proxy.aol.com
    .....    

    Keep in mind, that the original log files contains the following header lines.
    host    logname    time    method    url    response    bytes

    Make sure the head lines are removed in the resulting RDD.
    '''
	conf =  SparkConf().setAppName("UnionLog").setMaster("local[1]")
	sc = SparkContext(conf=conf)
	julio = sc.textFile('in/nasa_19950701.tsv')
	agosto = sc.textFile('in/nasa_19950801.tsv')

	j = julio.filter(isNotHeader)
	a = agosto.filter(isNotHeader)

	jhost = j.map(lambda line: line.split('\t')[0])
	ahost= a.map(lambda line: line.split('\t')[0])


	result = jhost.intersection(ahost)
	result.saveAsTextFile('out/nasa_logs_same_hosts.csv')
