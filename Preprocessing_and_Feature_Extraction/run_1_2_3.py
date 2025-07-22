from pathlib import Path
import subprocess

# Remember to set up your config.json before you run these three scripts. 



# Get the directory where this runner script is located
base_dir = Path(__file__).parent

# Define paths relative to this base directory
scripts = [
    base_dir / "1_epoch_recording.py",
    base_dir / "2_find_active_cells_ANOVA.py",
    base_dir / "3_get_tuning_matrices.py"
]

for script in scripts:
    print(f"\n--- Running {script.name} ---\n")
    subprocess.run(["python", str(script)], check=True)