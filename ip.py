import subprocess

cmd="cmd.exe"
begin=101
end=200
while begin<end:

    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p.stdin.write("ping 192.168.211."+str(begin)+"\n")

    p.stdin.close()
    p.wait()
    begin+=1
    print"execution result:%s"%p.stdout.read()
