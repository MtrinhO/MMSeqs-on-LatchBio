#Append dockerfile to have ./mmseqs

#Boilerplate
import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile
from latch.types import LatchDir

#Place all input file parameters into an ordered list that is fed to subprocess

@small_task
def start_easysearch(fastaq1: LatchFile, fastaq2: LatchFile, output: str, search_type: int) -> LatchFile: 

    # A reference to our output. This needs to match exactly what MMSEQS easy-search would output
    output = output + ".m8"
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
        str(search_type),
        "--remove-tmp-files"
    ]

    subprocess.run(_easysearch_cmd)

    return LatchFile("/root/" + str(tmp_output) ,"latch:///" + str(tmp_output))

@workflow
def easysearch(fastaq1: LatchFile, fastaq2: LatchFile, output: str, search_type: int) -> LatchFile:
    """Perform quick and comprehensive searches between two FASTA/FASTQ files of interest.
    markdown header
    ----

    > Regular markdown constructs work as expected.
    # Mmseqs2: easy-search workflow
    
    __metadata__:
        display_name: Mmseqs2 easy-search Workflow (Latch adaptation)
        author:
            name: Michael Trịnh 
            email: michaeltrinh19@gmail.com
            github: https://github.com/MtrinhO
        repository: https://github.com/MtrinhO/MMSeqs-on-LatchBio/tree/easysearch
        license: GNU General Public License v3.0
    Args:
        fastaq1:
          Your first of two FASTA/FASTQ file arguments. To be compared to sequence 2.
        fastaq2:
          Your first of two FASTA/FASTQ file arguments. To be compared to sequence 1.
        output:
          Filename of the tmp image (.m8 format) that will be outputted
        search_type:
          Integer (2 or 3) that represents the type of FASTA/FASTQ inputs that easy-search is looking at. (2 = Polypeptide, 3 = Nucleotide)
    """
    return start_easysearch(fastaq1=fastaq1, fastaq2=fastaq2, output=output, search_type=search_type)