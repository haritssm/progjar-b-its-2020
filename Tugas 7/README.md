# Tugas 7 Pemrograman Jaringan
## Performance Test Menggunakan Apache Benchmark

Performance Test ini dilakukan pada web server yang sama dengan Tugas 6. Berikut hasil dari Performance Test.

| __No. Test__ | __Concurrency Level__ | __Time Taken for Test__ | __Complete Request__ | __Failed Request__ | __Total Transferred__ | __Request per Second__ | __Time per Request__ | __Transfer Rate__ |
|--------------|-----------------------|------------------------|----------------------|--------------------|-----------------------|------------------------|----------------------|-------------------|
| 1            | 1                     | 0.046 sec              | 10                   | 0                  | 1350 Bytes            | 215.27 [#/sec]          | 4.645 [ms]          | 28.38 Kb/sec       |     
| 2            | 5                     | 0.234 sec              | 10                   | 0                  | 1350 Bytes            | 42.75 [#/sec]          | 116.965 [ms]          | 23.393 Kb/sec      |
| 3            | 10                    | 0.158 sec              | 10                   | 0                  | 1350 Bytes            | 63.40 [#/sec]          | 157.740 [ms]         | 8.36 Kb/sec       |
| 4            | 1                     | 1.350 sec              | 50                   | 0                  | 6750 Bytes            | 37.02 [#/sec]          | 27.010 [ms]          | 4.88 Kb/sec       |
| 5            | 10                    | 1.799 sec              | 50                   | 0                  | 6750 Bytes            | 27.79 [#/sec]         | 359.887 [ms]          | 3.66 Kb/sec      |
| 6            | 50                    | 2.662 sec              | 50                   | 0                  | 6750 Bytes            | 18.78 [#/sec]          | 2661.802 [ms]         | 2.48 Kb/sec       |
| 7            | 1                     | 12.460 sec              | 100                  | 0                  | 13500 Bytes           | 8.03 [#/sec]          | 124.597 [ms]          | 1.06 Kb/sec       |
| 8            | 10                    | 18.161 sec              | 100                  | 0                  | 13500 Bytes           | 5.51 [#/sec]          | 1816.112 [ms]         | 0.73 Kb/sec       |
| 9           | 50                    | 27.798 sec              | 100                  | 0                  | 13500 Bytes           | 3.60 [#/sec]          | 13898.917 [ms]        | 0.47 Kb/sec       |
| 10           | 100                   | 36.637 sec              | 100                  | 0                  | 13500 Bytes           | 2.73 [#/sec]          | 36636.662 [ms]        | 0.36 Kb/sec       |
