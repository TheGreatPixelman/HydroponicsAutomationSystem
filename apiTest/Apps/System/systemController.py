from flask import Blueprint
from .Models.system import systemInfo

app_system = Blueprint('app_system', __name__)
@app_system.route("/system")
def system_info():
    mem = systemInfo.getMemoryInfo()
    disk = systemInfo.getDiskUsage()
    cpu = systemInfo.getCpuFrequency()
    return { "memory": mem, "disk": disk, "cpu": cpu}

@app_system.route("/system/memoryinfo", methods=['GET'])
def system_memory_info():
    return systemInfo.getMemoryInfo(), 200

@app_system.route("/system/diskusage", methods=['GET'])
def system_disk_usage():
    return systemInfo.getDiskUsage(), 200

@app_system.route("/system/cpufreq", methods=['GET'])
def system_cpu_freq():
    return systemInfo.getCpuFrequency(), 200