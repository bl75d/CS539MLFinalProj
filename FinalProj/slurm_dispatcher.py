#!/bin/python3.6
from simple_slurm import Slurm

slurm = Slurm(
    output=(
        'slurm_jobs/job_{}.out'.format(
            Slurm.JOB_ID)
        )
    )
r = slurm.sbatch('python main.py -p')
print(r)
# r = slurm.sbatch('python3.6 main.py -p')
# print(r)
# r = slurm.sbatch('python2.6 main.py -p')
# print(r)