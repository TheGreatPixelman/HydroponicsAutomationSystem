import psutil

class systemInfo():

    @staticmethod
    def getMemoryInfo():
        memVal = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        return "{:.2f}".format(memVal)
    
    @staticmethod
    def getDiskUsage():
        diskUsage = psutil.disk_usage('/')
        return "{:.2f}".format(diskUsage.percent)
    
    @staticmethod
    def getCpuFrequency():
        cpuUsage = psutil.cpu_freq()
        return "{:.2f}".format(cpuUsage.current / cpuUsage.max)