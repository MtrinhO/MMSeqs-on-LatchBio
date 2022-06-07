#Append dockerfile to have ./mmseqs

#Boilerplate
import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile

#Place all input file parameters into an ordered list that is fed to subprocess

@small_task
def search_task(fastaq1: LatchFile, fastaq2: LatchFile, output: str, search_type: str) -> LatchFile: 

    # A reference to our output. This needs to match exactly what MMSEQS easy-search would output
    tmp_output = Path(output).resolve()
    tmp_output.touch()

    #Exact command line args that would be used in terminal
    _easysearch_cmd = [
        "mmseqs",
        "easy-search",
        fastaq1.local_path,
        fastaq2.local_path,
        str(tmp_output),
        "tmp",
         "--search-type",
        search_type,
    ]

    subprocess.run(_easysearch_cmd)

    return LatchFile(str(tmp_output), "latch:///" + output)

@workflow
def easy_search(fastaq1: LatchFile, fastaq2: LatchFile, output: str, search_type: str) -> LatchFile:
    """Description...
    markdown header
    ----

    > Regular markdown constructs work as expected.
    # Mmseqs2: easy-search workflow
    * Perform quick and comprehensive searches between two FASTA/FASTQ files of interest*
    __metadata__:
        display_name: Mmseqs2 easy-search Workflow
        author:
            name: Michael Trinh
            email: michaeltrinh19@gmail.com
            github: https://github.com/MtrinhO
        repository:
        license:
    Args:
        fastaq1:
          FASTA/FASTQ file 1 to be compared to FASTA/FASTQ file 2.
        fastaq2:
          FASTA/FASTQ file 2 to be compared to FASTA/FASTQ file 1.
        output:
          Filename of the tmp image (.m8 format) that will be outputted
        search_type:
          Integer (2 or 3) that represents the type of FASTA/FASTQ inputs that easy-search is looking at. (2 = Polypeptide, 3 = Nucleotide)
    """
    return search_task(fastaq1=fastaq1, fastaq2=fastaq2, output=output, search_type=search_type)