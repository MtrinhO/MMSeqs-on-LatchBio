#Append dockerfile to have ./mmseqs

#Boilerplate
import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile
from latch.types import LatchDir

#Place all input file parameters into an ordered list that is fed to subprocess

@small_task
def start_cluster(fastaq1: LatchFile) -> LatchFile: 
    
    #Exact command line args that would be used in terminal
    easycluster_cmd = [
        "mmseqs",
        "easy-cluster",
        fastaq1.local_path,
        "clusterRes",
        "tmp"
    ]

    subprocess.run(easycluster_cmd)

    return LatchFile("latch:///easycluster.sh")

@workflow
def easycluster(fastaq1: LatchFile) -> LatchFile:
    """Perform quick clustering on a FASTA/FASTQ entry.
    ----
    > Regular markdown constructs work as expected.
    # Mmseqs2: easy-cluster workflow
    
    __metadata__:
        display_name: Mmseqs2 easy-search Workflow (Latch adaptation)
        author:
            name: Michael Trịnh 
            email: michaeltrinh19@gmail.com
            github: https://github.com/MtrinhO
        repository: https://github.com/MtrinhO/MMSeqs-on-LatchBio/tree/easycluster
        license: GNU General Public License v3.0
    Args:
        fastaq1:
          Your FASTA sequence to be clustered
    """
    return start_cluster(fastaq1=fastaq1)