import tsdb_sample

def selectall():
    tsdb = tsdb_sample.select(
        "select  Identity ,Temperature, Number_02,  String_01 from metric order by "
        "Number_02 desc")
    return tsdb
if __name__ == "__main__":
    res = selectall()
    print (res)