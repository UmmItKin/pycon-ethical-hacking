FROM kalilinux/kali-rolling

RUN apt update && \
    apt install -y \
    sudo vim nano tmux curl wget git \
    nmap masscan whatweb \
    sqlmap dirb nikto wafw00f \
    ffuf gobuster wfuzz \
    wpscan \
    metasploit-framework \
    hydra hashcat john seclists \
    recon-ng sublist3r theharvester amass \
    tcpdump \
    bettercap \
    mitmproxy \
    python3 python3-pip \
    && apt clean

RUN useradd -m labuser && echo "labuser:lab123" | chpasswd && \
    usermod -aG sudo labuser

RUN mkdir /lab && chown labuser:labuser /lab
