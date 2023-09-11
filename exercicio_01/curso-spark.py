# apt-get install openjdk-8-jdk-headless -qq > /dev/null
# wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz
# tar xf spark-3.1.2-bin-hadoop2.7.tgz
# pip install pyspark
# pip install -q findspark

#----------------------------------------------------------------------------------------

import os

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/home/spark-3.1.2-bin-hadoop2.7"

import findspark

findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[*]').appName("Iniciando com Spark").config('spark.ui.port', '4050').getOrCreate()

import zipfile

zipfile.ZipFile('/home/matheus/Documentos/MeusProjetos/Big-Data/exercicio_01/curso-spark/empresas.zip','r').extractall('/home/matheus/Documentos/MeusProjetos/Big-Data/exercicio_01/curso-spark/')

path = "/home/matheus/Documentos/MeusProjetos/Big-Data/exercicio_01/curso-spark/empresas"
empresas = spark.read.csv(path, sep=";", inferSchema=True)

empresas.printSchema()
empresas.count()
empresas.limit(3).toPandas()