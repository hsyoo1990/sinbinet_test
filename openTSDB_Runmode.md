# (After installation) OpenTSDB Run mode

### root Connection
### Apply profile After adding
```sh
$ source /etc/profile
```
### hbase Run
In directory [hbase-1.0.1.1]
```sh
$ ./bin/start-hbase.sh 
```

### openTSDB Run
in directory [opentsdb]
```sh
$ env COMPRESSION=NONE HBASE_HOME=/usr/local/data/hbase-1.0.1.1 ./src/create_table.sh
$ ./build/tsdb tsd --port=4242 --staticroot=build/staticroot --cachedir=/usr/local/data --auto-metric
```

### Tcollector Run - Execution of one terminal anymore
in directory [tcollector]
```sh
$ ./startstop start
$ tail -f /var/log/tcollector.log
```
##### The connection with 'http://192.168.x.x:4242' in the web address bar
