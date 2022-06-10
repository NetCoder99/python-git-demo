import subprocess
# -------------------------------------------------------------
def displayGitOutput(proc):
  print(proc.returncode)
  print(proc.stdout)
  print(proc.stderr)

# -------------------------------------------------------------
def isGitDirectory():
  """Check if the current directory has been initialized as a Git repo"""
  cmd_str = ["git", "status"]
  proc = subprocess.run(cmd_str,capture_output=True,text=True)
  displayGitOutput(proc)
  if proc.returncode == 0:
    return True
  elif proc.returncode == 128 and proc.stderr.startswith("fatal: not a git repository") :
    return False
  else:
    raise Exception("Uknown git status")  

# -------------------------------------------------------------
def initGitDirectory():
  """Initialize the local Git repo and add all files"""
  cmd_str = ["git", "init"]
  proc = subprocess.run(cmd_str,capture_output=True,text=True)
  displayGitOutput(proc)
  if proc.returncode == 0:
    addAllFiles()
    return True
  elif proc.returncode == 128 and proc.stderr.startswith("fatal: not a git repository") :
    return False
  else:
    raise Exception("Uknown git status")  

# -------------------------------------------------------------
def addAllFiles():
  """Add add all files to the new Git repo"""
  cmd_str = ["git", "add", "."]
  proc = subprocess.run(cmd_str,capture_output=True,text=True)
  displayGitOutput(proc)
  if proc.returncode == 0:
    return True
  elif proc.returncode == 128 and proc.stderr.startswith("fatal: not a git repository") :
    return False
  else:
    raise Exception("Uknown git status")  


  # data = proc.stdout
  # err = proc.stderr
  # result = proc.returncode
  # print(proc)
  # print(data)
  # print(result)
  # return False

