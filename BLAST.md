```cpp file:"blast"
建库：
makeblastdb -in your_sequences.fasta -dbtype nucl -out my_blast_db
-dbtype = nucl(核酸序列) or prot(蛋白质序列)
// 注： 使用库时 需要 路径名 + 数据库名 
检验：
blastdbcmd -info -db ${file_name}\${db_name}
匹配
tblastn -query protein.fasta -db my_db\my_d -out results.txt -outfmt 6 -qcov_hsp_perc 100
```