import subprocess
import os
import platform
from typing import Annotated, Optional

import typer
from typer import Typer
from rich.console import Console

app = Typer()

@app.command(name="cleanup")
def cleanup(distro: str = "debian", work_dir: Annotated[Optional[str], typer.Option()] = "./work"):
    console = Console()
    if platform.system() != "Linux":
        console.print("[red]ERR[/red]: nobuild supports Linux only.")
    if os.getuid() == 0:
        subprocess.run(f"nobuild-{distro} clean --work-dir {work_dir}", shell=True)
    else:
        console.print("[red]ERR[/red]: Root privileges are required")

@app.command(name="build")
def build(distro: str = "debian", flavor: Annotated[Optional[str], typer.Option()] = None, work_dir: Annotated[Optional[str], typer.Option()] = "./work"):
    console = Console()
    if platform.system() != "Linux":
        console.print("[red]ERR[/red]: nobuild supports Linux only.")
    if os.getuid() == 0:
        if os.path.isdir("./flavors"):
            subprocess.run(f"nobuild-{distro} step --flavor {flavor} --work-dir {work_dir}", shell=True)
        else:
            subprocess.run(f"nobuild-{distro} step --work-dir {work_dir}", shell=True)
    else:
        console.print("[red]ERR[/red]: Root privileges are required")