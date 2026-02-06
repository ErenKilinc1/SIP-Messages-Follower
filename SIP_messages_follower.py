import paramiko
import time
import re

ROUTER_IP = 'Router_IP'
USERNAME = 'user.name'
PASSWORD = 'your_password'
ARANAN_NO = 'Aranan_NO'
ARAYAN_NO = 'Arayan_No'


def stream_sip_logs():
    ssh = None
    remote_conn = None

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ROUTER_IP, username=USERNAME, password=PASSWORD)

        remote_conn = ssh.invoke_shell()
        for cmd in ["terminal length 0", "terminal monitor", "logging debug-trace", "debug ccsip messages"]:
            remote_conn.send(cmd + "\n")
            time.sleep(0.5)

        print(f"--- SIP KODU FİLTRELEME ---\n")
        print(f"Filtre -> {ARAYAN_NO} veya {ARANAN_NO} içeren paketler yakalanıyor...\n")

        buffer = ""
        while True:
            if remote_conn.recv_ready():
                output = remote_conn.recv(65535).decode('utf-8', errors='ignore')
                buffer += output

                packets = re.split(r'(?=\n\d+: .*?: //.*?/SIP/Msg/ccsipDisplayMsg:)', buffer)

                if len(packets) > 1:
                    to_process = packets[:-1]
                    buffer = packets[-1]

                    for packet in to_process:
                        # Numaralar paket içersinde mi değil mi diye bakılır.
                        if ARANAN_NO in packet or ARAYAN_NO in packet:
                            clean_packet = re.sub(r'^[A-Za-z0-9-_]+#', '', packet, flags=re.MULTILINE)
                            lines = [l.strip() for l in clean_packet.splitlines() if l.strip()]

                            print("\n".join(lines))
                            print("-" * 70)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nTakip durduruldu.")

    finally:
        if remote_conn:
            remote_conn.send("undebug all\n")
            remote_conn.send("no logging debug-trace\n")
            time.sleep(0.5)
        if ssh:
            ssh.close()

if __name__ == "__main__":
    stream_sip_logs()