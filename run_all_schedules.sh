#!/bin/bash

names=(
    "tabu_gamma=1_L=1"
    "tabu_gamma=1_L=10"
    "tabu_gamma=1_L=15"
    "tabu_gamma=1_L=20"
    "tabu_gamma=1_L=25"
    "tabu_gamma=1_L=30"
    "tabu_gamma=10_L=1"
    "tabu_gamma=10_L=10"
    "tabu_gamma=10_L=15"
    "tabu_gamma=10_L=20"
    "tabu_gamma=10_L=25"
    "tabu_gamma=10_L=30"
    "tabu_gamma=15_L=1"
    "tabu_gamma=15_L=10"
    "tabu_gamma=15_L=15"
    "tabu_gamma=15_L=20"
    "tabu_gamma=15_L=25"
    "tabu_gamma=15_L=30"
    "tabu_gamma=2_L=1"
    "tabu_gamma=2_L=10"
    "tabu_gamma=2_L=15"
    "tabu_gamma=2_L=20"
    "tabu_gamma=2_L=25"
    "tabu_gamma=2_L=30"
    "tabu_gamma=20_L=1"
    "tabu_gamma=20_L=10"
    "tabu_gamma=20_L=15"
    "tabu_gamma=20_L=20"
    "tabu_gamma=20_L=25"
    "tabu_gamma=20_L=30"
    "tabu_gamma=5_L=1"
    "tabu_gamma=5_L=10"
    "tabu_gamma=5_L=15"
    "tabu_gamma=5_L=20"
    "tabu_gamma=5_L=25"
    "tabu_gamma=5_L=30"
)

for name in "${names[@]}"
do 
    echo "Running script for $name"
    python3 convert.py --fname "schedules/$name"
    python3 main.py --runs 3 --scheduler "schedules/$name"
done

Running script for tabu_gamma=1_L=1
Running script for tabu_gamma=1_L=10
Running script for tabu_gamma=1_L=15
Running script for tabu_gamma=1_L=20
Running script for tabu_gamma=1_L=25
Running script for tabu_gamma=1_L=30
Running script for tabu_gamma=10_L=1
Running script for tabu_gamma=10_L=10
Running script for tabu_gamma=10_L=15
Running script for tabu_gamma=10_L=20
Running script for tabu_gamma=10_L=25
Running script for tabu_gamma=10_L=30
Running script for tabu_gamma=15_L=1
Running script for tabu_gamma=15_L=10
Running script for tabu_gamma=15_L=15
Running script for tabu_gamma=15_L=20
Running script for tabu_gamma=15_L=25
Running script for tabu_gamma=15_L=30
Running script for tabu_gamma=2_L=1
Running script for tabu_gamma=2_L=10
Running script for tabu_gamma=2_L=15
Running script for tabu_gamma=2_L=20
Running script for tabu_gamma=2_L=25
Running script for tabu_gamma=2_L=30
Running script for tabu_gamma=20_L=1
Running script for tabu_gamma=20_L=10
Running script for tabu_gamma=20_L=15
Running script for tabu_gamma=20_L=20
Running script for tabu_gamma=20_L=25
Running script for tabu_gamma=20_L=30
Running script for tabu_gamma=5_L=1
Running script for tabu_gamma=5_L=10
Running script for tabu_gamma=5_L=15
Running script for tabu_gamma=5_L=20
Running script for tabu_gamma=5_L=25
Running script for tabu_gamma=5_L=30