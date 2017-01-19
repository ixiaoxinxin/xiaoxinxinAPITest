import os, sys
root_dir = '/'.join(os.path.realpath(__file__).split('/')[:1])
sys.path.append(root_dir)
logLevel = 2
logFile = os.path.join(root_dir,'logs')
DATABASE = {
    "ENINE" : "MogoDB",
    "HOST"  : "",
    "POST"  : "270510",
    "PWD"   : "",
    "DATABASE" : ""

}
