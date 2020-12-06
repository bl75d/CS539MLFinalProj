from slurm import Slurm

slurm = Slurm(
    output=(
        'slurm_jobs/job_{}.out'.format(
            Slurm.JOB_ID)
        )
    )
r = slurm.sbatch('python main.py -p')
print(r)
r = slurm.sbatch('python main.py -p')
print(r)
r = slurm.sbatch('python main.py -p')
print(r)