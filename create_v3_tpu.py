
import subprocess
import json
import time
import os
import fire

def get_name(x):
    return x['name'].split('/')[-1]

LIST_STR= "gcloud compute tpus list --zone europe-west4-a --format json"
cmd = "gcloud alpha compute tpus tpu-vm create {node_name} --project {project_name} --zone europe-west4-a --accelerator-type v3-8 --version tpu-vm-base" 

def parse_tpu_info():
    text = call(LIST_STR).strip()
    objects = json.loads(text)
    return [get_name(x) for x in objects]

def call(cmd: str) -> str:
    return subprocess.check_output(cmd.split()).rstrip().decode()

def create_tpus(project_name:str)
    for idx in range(5):
        node_idx = idx + 1
        name = f"v3-8-node-{node_idx}"
        while name not in parse_tpu_info():
            os.system(cmd.format(node_name=name,project_name=project_name))
            time.sleep(10)
            

if __name__=="__main__":
    fire.Fire(create_tpus)