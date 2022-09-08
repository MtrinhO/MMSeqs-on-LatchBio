# MMseqs2: easy-cluster

easy-cluster by default clusters the entries of a FASTA/FASTQ file using a cascaded clustering algorithm. Users may also use easy-linclust mode, where runtime scales linearly with input size. This is recommended for huge datasets.

### Usage

This workflow returns 3 files:

* ```{prefix}_all_seqs.fasta```
* ```{prefix}_cluster.tsv```
* ```{prefix}_rep_seq.fasta```

Where ```{prefix}``` may be set by the user.

MMseqs2 (Many-against-Many searching) is a software suite to search and cluster huge sequence sets. MMseqs2 is open source GPL-licensed software implemented in C++ for Linux, Mac OS and Windows.

### Arguments

* __fastaq1__: Bam file to take metrics from.
* __outdir__: Latch console destination for output files.
* __prefix__: Name for output FASTQ files.

### Dependencies

* [mmseqs2](https://github.com/soedinglab/MMseqs2)
* [conda](https://docs.conda.io/)
* [LatchBio](https://latch.bio/)