```cpp file:"blast"
// 建库：
makeblastdb -in ${file.fasta} -dbtype nucl -out ${db_name}
 -dbtype = nucl(核酸序列) or prot(蛋白质序列)
// 注： 使用库时 需要 路径名 + 数据库名 

// 检验：
blastdbcmd -info -db ${file_name}\${db_name}

// 匹配
tblastn -query protein.fasta -db ${file_name}\${db_name} -out ${results.txt} 
// 可添加参数 表明 匹配百分比， 默认并没有固定的匹配长度
-qcov_hsp_perc 100
// 控制结果展示的内容，默认为0；为1和6时展示了匹配的位置，其他还没看。
-outfmt <Integer, (>= 0 and  =< 18)>
// 控制排序属性，默认按照e-value排序。当outfmt> 4时不可使用该参数
-sorthits <Integer, (>=0 and =<4)>

-sorthits <Integer, (>=0 and =<4)>
   Sorting option for hits:
   alignment view options:
     0 = Sort by evalue,
     1 = Sort by bit score,
     2 = Sort by total score,
     3 = Sort by percent identity,
     4 = Sort by query coverage
   Not applicable for  > 4
-outfmt <String>
   alignment view options:
     0 = Pairwise,
     1 = Query-anchored showing identities,
     2 = Query-anchored no identities,
     3 = Flat query-anchored showing identities,
     4 = Flat query-anchored no identities,
     5 = BLAST XML,
     6 = Tabular,
     7 = Tabular with comment lines,
     8 = Seqalign (Text ASN.1),
     9 = Seqalign (Binary ASN.1),
    10 = Comma-separated values,
    11 = BLAST archive (ASN.1),
    12 = Seqalign (JSON),
    13 = Multiple-file BLAST JSON,
    14 = Multiple-file BLAST XML2,
    15 = Single-file BLAST JSON,
    16 = Single-file BLAST XML2,
    18 = Organism Report
```