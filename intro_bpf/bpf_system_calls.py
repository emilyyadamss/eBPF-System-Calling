from bcc import BPF 
from bcc.utils import printb 

# BPF program, written in C and stored as a string. 
# handles the BPF logic 
BPF_SOURCE_CODE = r""""
TRACEPOINT_PROBE(syscalls, sys_enter_mkdirat) { 
    bpf_trace_printk("Wow, new directory: %s\n", args->pathname)} ;  
    return 0 ; 
    }
    """

# loads the BPF program and runs it
bpf = BPF(text = BPF_SOURCE_CODE) 

print("To try out, open another terminal window and create a new directory.") 
print("i.e. mkdir newFolder") 
print("CTRL-C to exit") 

# monitors and prints the trace messages 
while True: 
    try: 
        (task, pid, cpu, flags, ts, msg) = bpf.trace_fields() 
        printb(b"%s" % (pid, msg)) 
    except ValueError: 
        continue 
    except KeyboardInterrupt: 
        break 