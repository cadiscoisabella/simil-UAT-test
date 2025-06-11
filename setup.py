import os
import subprocess
import platform
from pathlib import Path

VERSION = "1.0.0"

def run_command(cmd, check=True, shell=True):
    """Run a command and return the completed process"""
    return subprocess.run(cmd, check=check, shell=shell)

def setup(versions):
    """
    Set up specified virtual environments
    Args:
        versions: List of versions to setup (e.g., ['3.8', '3.9', '3.11'] or ['all'])
    """
    is_windows = platform.system() == "Windows"
    print("Checking for uv...")
    
    try:
        if is_windows:
            run_command("where uv >nul 2>&1", check=False)
        else:
            run_command("which uv >/dev/null 2>&1", check=False)
    except:
        print("Installing uv...")
        if is_windows:
            run_command('powershell -Command "irm https://astro.build/install | iex"')
        else:
            run_command('curl -sSf https://astro.build/install.sh | sh')

    if 'all' in versions:
        versions = ['3.8', '3.9', '3.11']  # Added 3.8 to the default versions
    
    for version in versions:
        venv_dir = f".venv{version.replace('.', '')}"
        req_file = f"requirements/py{version.replace('.', '')}.txt"
        
        print(f"Creating {version} environment...")
        run_command(f"uv venv {venv_dir} --python {version}")
        
        print("Installing base packages...")
        if is_windows:
            run_command(f"{venv_dir}\\Scripts\\activate && "
                      f"uv pip install setuptools==68.0.0 && "
                      f"uv pip install -r {req_file} && "
                      "deactivate")
        else:
            # Use bash explicitly for Linux/WSL
            run_command(f"bash -c 'source {venv_dir}/bin/activate && "
                      f"uv pip install setuptools==68.0.0 && "
                      f"uv pip install -r {req_file} && "
                      "deactivate'")

    print(f"✅ Setup complete! Version: {VERSION}")

def activate(version):
    """Print activation commands for different shells"""
    venv_dir = f".venv{version.replace('.', '')}"
    is_windows = platform.system() == "Windows"
    
    if not os.path.exists(venv_dir):
        print(f"❌ Virtual environment {venv_dir} not found. Run setup first.")
        return

    print(f"\nTo activate Python {version} environment (Version: {VERSION}):")
    
    if is_windows:
        # Windows CMD
        print("\nFor Windows CMD:")
        print(f"call {venv_dir}\\Scripts\\activate.bat")
        print(f"set VERSION={VERSION}")
        
        # Windows PowerShell
        print("\nFor Windows PowerShell:")
        print(f"{venv_dir}\\Scripts\\Activate.ps1")
        print(f"$env:VERSION = \"{VERSION}\"")
    else:
        # Linux/WSL (Bash/Zsh)
        print("\nFor Bash/Zsh (Linux/WSL):")
        print(f"source {venv_dir}/bin/activate")
        print(f"export VERSION=\"{VERSION}\"")
    
    # Git Bash (works on both Windows & WSL)
    print("\nFor Git Bash:")
    print(f"source {venv_dir}/Scripts/activate" if is_windows else f"source {venv_dir}/bin/activate")
    print(f"export VERSION=\"{VERSION}\"")
    
    # Nushell (cross-platform)
    print("\nFor Nushell:")
    print(f"overlay use {venv_dir}/Scripts/activate.nu" if is_windows else f"overlay use {venv_dir}/bin/activate.nu")
    print(f"$env.VERSION = \"{VERSION}\"")
    
    print("\nAfter activation, verify with:")
    print("python --version")
    print("echo $VERSION  # or %VERSION% in CMD")

def clean(versions):
    """
    Clean up specified virtual environments
    Args:
        versions: List of versions to clean (e.g., ['3.8', '3.9', '3.11'] or ['all'])
    """
    is_windows = platform.system() == "Windows"
    
    if 'all' in versions:
        versions = ['3.8', '3.9', '3.11']  # Added 3.8 to the default versions
    
    for version in versions:
        venv_dir = f".venv{version.replace('.', '')}"
        try:
            if is_windows:
                run_command(f"rmdir /s /q {venv_dir}", check=False)
            else:
                run_command(f"rm -rf {venv_dir}", check=False)
            print(f"Removed {venv_dir}")
        except:
            print(f"⚠️ Could not remove {venv_dir} (may not exist)")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Manage Python environments")
    subparsers = parser.add_subparsers(dest='command')
    
    # Setup command with version argument
    setup_parser = subparsers.add_parser('setup', help='Set up virtual environments')
    setup_parser.add_argument(
        'versions',
        nargs='*',
        default=['all'],
        choices=['3.8', '3.9', '3.11', 'all'],  # Added 3.8 to choices
        help='Python versions to setup (default: all)'
    )
    
    # Activate commands
    activate_parser = subparsers.add_parser('activate', help='Activate environment')
    activate_parser.add_argument('version', choices=['3.8', '3.9', '3.11'], help='Python version')  # Added 3.8
    
    # Clean command with version argument
    clean_parser = subparsers.add_parser('clean', help='Remove virtual environments')
    clean_parser.add_argument(
        'versions',
        nargs='*',
        default=['all'],
        choices=['3.8', '3.9', '3.11', 'all'],  # Added 3.8 to choices
        help='Versions to clean (default: all)'
    )
    
    args = parser.parse_args()
    
    if args.command == 'setup':
        setup(args.versions)
    elif args.command == 'activate':
        activate(args.version)
    elif args.command == 'clean':
        clean(args.versions)
    else:
        parser.print_help()