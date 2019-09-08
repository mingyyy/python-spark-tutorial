import sys
from pyspark import SparkContext

if __name__ == "__main__":

    '''
    Create a Spark program to read the first 100 prime numbers from in/prime_nums.text,
    print the sum of those numbers to console.
    Each row of the input file contains 10 prime numbers separated by spaces.
    '''
    sc = SparkContext('local[1]', "textfile")
    lines = sc.textFile('in/prime_nums.text')
    nums = lines.flatMap(lambda line: line.split('\t'))
    s = nums.reduce(lambda x, y: int(x)+int(y))
    print(f'Sum of first 100 prime number is: {s}')

