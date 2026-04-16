"""system.py — CPU, RAM, and VRAM stats for the Overview resource bar."""
from __future__ import annotations

import asyncio
import shutil
import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


def _nvidia_vram() -> dict | None:
    """Query nvidia-smi for VRAM. Returns None if the GPU / driver is unavailable."""
    if not shutil.which("nvidia-smi"):
        return None
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=memory.used,memory.total",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=3,
        )
        if result.returncode != 0:
            return None
        line = result.stdout.strip().split("\n")[0]
        used, total = [int(x.strip()) for x in line.split(",")]
        return {"used_mb": used, "total_mb": total}
    except Exception:
        return None


@router.get("/stats")
async def system_stats() -> dict:
    """
    Return current resource usage:
      { cpu_pct, ram: { used_mb, total_mb }, vram: { used_mb, total_mb } | null }
    psutil is required for CPU and RAM; absent = zeros. nvidia-smi absent = vram null.
    """
    cpu_pct = 0.0
    ram: dict | None = None
    try:
        import psutil  # soft dependency
        cpu_pct = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        ram = {
            "used_mb":  mem.used  // (1024 * 1024),
            "total_mb": mem.total // (1024 * 1024),
        }
    except ImportError:
        pass

    loop = asyncio.get_event_loop()
    vram = await loop.run_in_executor(None, _nvidia_vram)

    return {"cpu_pct": cpu_pct, "ram": ram, "vram": vram}
