#Append dockerfile to have ./mmseqs

#Boilerplate
import subprocess
from pathlib import Path
import os

from latch import medium_task, workflow
from latch.types import LatchFile
from latch.types import LatchDir

@medium_task
def start_cluster(fastaq1: LatchFile, outdir: LatchDir, prefix: str = "test") -> LatchDir: 

    tmp_dir = Path("/root/tmp/").resolve()
    os.mkdir("/root/results/")
    local_dir = Path("/root/results/").resolve()

    #Exact command line args that would be used in terminal
    easycluster_cmd = [
        "mmseqs",
        "easy-cluster",
        str(fastaq1.local_path),
        prefix,
        str(tmp_dir)
    ]

    _mv_cmd = [
        "mv",
        f"/root/{prefix}_all_seqs.fasta",
        f"/root/{prefix}_cluster.tsv",
        f"/root/{prefix}_rep_seq.fasta",
        str(local_dir)
    ]

    subprocess.run(easycluster_cmd)
    subprocess.run(_mv_cmd)
    
    return LatchDir(str(local_dir), outdir.remote_path)
    #return LatchDir("/root/", outdir.remote_path)


@workflow
def easy_cluster(fastaq1: LatchFile, outdir: LatchDir, prefix: str = "test") -> LatchDir:
    """Perform quick clustering on a FASTA/FASTQ entry.
    
    MMseqs2: easy-cluster
    ----
    ### Description

    easy-cluster by default clusters the entries of a FASTA/FASTQ file 
    using a cascaded clustering algorithm.

    This workflow returns 3 files:

    * ```{prefix}_all_seqs.fasta```
    * ```{prefix}_cluster.tsv```
    * ```{prefix}_rep_seq.fasta```

    Where ```{prefix}``` may be set by the user.

    MMseqs2 (Many-against-Many searching) is a software suite to search 
    and cluster huge sequence sets. MMseqs2 is open source GPL-licensed 
    software implemented in C++ for Linux, Mac OS and Windows.

    __metadata__:
        display_name: easy_cluster
        author:
            name: Michael Trịnh & Murto Hilali
            email: michaeltrinh19@gmail.com & hilali.murto@gmail.com
            github: https://github.com/MtrinhO
        repository: https://github.com/MtrinhO/MMSeqs-on-LatchBio/tree/easycluster
        license: GNU General Public License v3.0
    Args:
        fastaq1:
          Your FASTA/FASTQ sequence to be clustered.

          __metadata__:
            display_name: FASTA/FASTQ File

        outdir:
          Your output directory.

          __metadata__:
            display_name: Output Directory

        prefix:
          Output file name prefix.

          __metadata__:
            display_name: Filename Prefix
    """
    return start_cluster(fastaq1=fastaq1, outdir=outdir, prefix=prefix)