# TeCoR-UAV

## Environment
- Python: 3.10
- Mysql：8.x
- Install: `pip install -r requirements.txt`

## Directory Structure

~~~text
.
├─ c_c/
|  ├─3DObstacle_avoidance              # Obstacle-Avoidance Path Planning
|  ├─change_geatpy_source_code         # Primary Algorithm Module
|  ├─compare                           # Compared Algorithms
|  ├─expe_run_script                   # Experiment Execution Scripts
|  |  ├─expe_ab_Hierarchical.py        # Ablation: Hierarchical Architecture Scripts
|  |  ├─expe_ab_init.py                # Ablation: Population Initialization Scripts
|  |  ├─expe_ab_Obstacle_avoidance.py  # degradation of obstacle-free initial paths under obstacle constraints
|  |  ├─expe_ab_op.py                  # Ablation: Genetic Operator Scripts
|  |  ├─expe_compare.py                # Comparison Experiment Scripts
|  ├─route_planning                    # Main Algorithm Dependency Utilities
|  ├─run_script                        # Population-Initialization Dependency Utilities
|  ├─tools                             # General-Purpose Utilities
|  ├─ps_env.py                         # Problem Modeling Scripts
├─ mappo/                              # MAPPO for Comparison
├─ hv_compute/                         # Hypervolume (HV) Computation Scripts
├─ data/                               # Data Directory
│  ├─ Urban40/                         # Minimal Reproducible Subset(bundled with the repository)
│  └─ other_data/                      # Full Dataset
└─ README.md
~~~

## Running
### 1) Create DB and import data
- 1.1 Create DB
`mysql -u root -p -e "CREATE DATABASE ur_orders40 DEFAULT CHARSET utf8mb4`
- 1.2 Import the Urban40 scenario’s tables and data into the database
`mysql -u root -p ur_orders40 < data/Urban40/all.sql`

### 2) Configure DB connection
- In `c_c/tools/MySqlConn.py`, change `database : <your-created-database>`

### 3) Run experiments
~~~text
(1) python c_c/expe_run_script/expe_ab_Hierarchical.py                # Hierarchical Architecture
(2) python c_c/expe_run_script/expe_ab_init.py                       # Ablation: Population Initialization
(3) python c_c/expe_run_script/expe_ab_op.py                          # Ablation: Genetic Operator
(4) python c_c/expe_run_script/expe_ab_Obstacle_avoidance.py          # There are precedence constraints between I/O and database write operations; run the steps strictly in the order specified in main(), and do not run other experiments in parallel while this script is executing (it modifies the database).
(5) python c_c/expe_run_script/expe_compare.py                        # Comparison Experiment
~~~
### 4) Switch to other scenarios
- Database creation: Create the database locally and import the SQL for the target scenario.
- Connection: In `c_c/tools/MySqlConn.py`, change the "database" field to the new database name; modify port/username/password if they differ.
- Statistics/parameters: Update the relevant settings in `c_c/tools/return_all_num.py` for this scenario.
- Distance matrix file: The main algorithm depends on each scenario’s distance.xlsx. Place the file in the corresponding directory:
      Mountain terrain: `c_c/3DObstacle_avoidance/moun/distance.xlsx`
      Urban terrain: `c_c/3DObstacle_avoidance/urban/distance_terrain.xlsx`
